from django.contrib import admin
from .models import CustomerOrder, OrderDetail, ShippingAdress

class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('customer_order', 'product', 'quantity', 'unit_price')
    search_fields = ('customer_order__id', 'product__name')
    list_filter = ('customer_order',)

class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'name', 'contact_email', 'delivery_address', 'paid', 'order_date', 'is_complete')
    search_fields = ('customer__username', 'name', 'contact_email')
    list_filter = ('order_date', 'is_complete')

class ShippingAdressAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'adress', 'city', 'zip')
    search_fields = ('user__username', 'name', 'email')
    list_filter = ('city',)

admin.site.register(CustomerOrder, CustomerOrderAdmin)
admin.site.register(OrderDetail, OrderDetailAdmin)
admin.site.register(ShippingAdress, ShippingAdressAdmin)
