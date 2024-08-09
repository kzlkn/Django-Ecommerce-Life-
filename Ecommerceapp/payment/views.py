from urllib import request
from django.http import JsonResponse
from django.shortcuts import render
from sepet.sepet import Sepet
from .models import OrderDetail, CustomerOrder, ShippingAdress
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from .forms import ShippingForm

# burada tamam
#https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/
def payment_success(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        if key == 'session_key':
            del request.session[key]
    return render(request, 'payment/Odeme-Basarili.html')

def odeme(request):
    if request.user.is_authenticated:
        context = {}
        try:
            gondermeAdress = ShippingAdress.objects.get(user=request.user.id)
            context['gondermeAdress'] = gondermeAdress
        except ShippingAdress.DoesNotExist:
            pass
        return render(request, 'payment/checkout.html', context=context)
    else:
        return render(request, 'payment/checkout.html')

def payment_fail(request):
    return render(request, 'payment/Odeme-Basarisiz.html')

@csrf_exempt
def complete_order(request):
    if request.method == 'POST':
        order_data = _extract_order_data(request)
        sepet = Sepet(request)
        total_cost = sepet.get_total()

        order = _create_order(request, order_data, total_cost)

        _save_order_details(sepet, order)

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

def _extract_order_data(request):
    return {
        'name': request.POST.get('name'),
        'email': request.POST.get('email'),
        'adress': request.POST.get('adress'),
        'city': request.POST.get('city'),
        'zipcode': request.POST.get('zip')
    }

def _create_order(request, order_data, total_cost):
    shipping_address = f"{order_data['adress']}\n{order_data['city']}\n{order_data['zipcode']}"
    if request.user.is_authenticated:
        order = CustomerOrder.objects.create(
            name=order_data['name'],
            contact_email=order_data['email'],
            delivery_address=shipping_address,
            paid=total_cost,
            customer=request.user
        )
        ShippingAdress.objects.update_or_create(
            user=request.user,
            defaults={
                'name': order_data['name'],
                'email': order_data['email'],
                'adress': order_data['adress'],
                'city': order_data['city'],
                'zip': order_data['zipcode']
            }
        )
    else:
        order = CustomerOrder.objects.create(
            name=order_data['name'],
            contact_email=order_data['email'],
            delivery_address=shipping_address,
            paid=total_cost,
            customer=None  
        )
    return order

def _save_order_details(sepet, order):
    for item in sepet:
        OrderDetail.objects.create(
            customer_order=order,
            product=item['product'],
            quantity=item.get('miktar', 0),
            unit_price=item['price']
        )
