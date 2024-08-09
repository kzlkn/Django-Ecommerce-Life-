# Burada çalısşıldı 
from django.urls import reverse, reverse_lazy


from django.shortcuts import redirect, render
#from hesap.forms import Custom_Login_Form21

 #https://docs.djangoproject.com/en/5.0/ref/contrib/sites/
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes,force_str
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from payment.forms import ShippingForm
from payment.models import ShippingAdress,CustomerOrder,OrderDetail
import logging
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import User


from account.forms import Custom_Login_Form21,User_günccelle
from django.contrib.auth import login,aauthenticate,logout # bu ra önemli
from .forms import KulaniciOlustur

from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.views.generic.edit import CreateView

from django.contrib.sites.shortcuts import get_current_site
from .token import activation_token_generator

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from pyexpat.errors import messages
from django.shortcuts import redirect, render

# Note:  This code develop and  formatted with  AI and Udemy Tutorial https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/learn/lecture/34403790#overview.
#sources : https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
#https://stackoverflow.com/questions/71724412/using-models-and-views-in-django
#https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef
#https://forum.djangoproject.com/t/form-is-valid-always-false-where-prefilled-form-used/26512
#https://stackoverflow.com/questions/68090161/django-form-is-valid-error-but-only-after-if-request-method-post
#https://forum.djangoproject.com/t/customize-django-auth-login-functionality/24022
#https://stackoverflow.com/questions/56231547/register-form-in-django-wont-post-the-request-method

logger = logging.getLogger(__name__) # programın çalışması sırasında meydana gelen olayları kaydeden. logger hataları kaydeder 

def decode_uid(uidb64):#Base64 ile kodlanmış kullanıcı
    try:
        return force_str(urlsafe_base64_decode(uidb64)) # Base64 ile kodlanmış uidb64 string'ini çözer force_str degeri stringe çevirir
    except (TypeError, ValueError, OverflowError) as e: #OverflowError hatalarını yakalar. eror türlerini yakalar 
        logger.error(f"Error decoding uid: {e}") # log mesajını yazar ve en
        return None # en sonde none döner

def get_user(user_id):# kuulanıcı kimligi
    try:
        return User.objects.get(pk=user_id) # id ile diger idiyle eşleşen kulanıcıyı getirir 
    except User.DoesNotExist: # eger kulanıcı yokda none 
        return None # node dönder 

def email_kntrl(request, uidb64, token):
    user_id = decode_uid(uidb64) # uidb64'ü çözer ve userın  kimlgini alır.
    if user_id is None: # eger yoksa
        return redirect('email-unpss') # buraya gider
    
    user = get_user(user_id) # eşlesen kulanıcı gelsin
    if user is not None and activation_token_generator.check_token(user, token): # kulanıcı var token gçerli olursa 
        user.is_active = True # kulanıcımız aktif olur 
        user.save() # kaydedilir veri tbanına 
        return redirect('email-passed') # bu htmle gidilr
    
    return redirect('email-unpss') # yoksa buraya gidiilr
 
 


# bu kod genel olarak haynı prenssip 
def email_passed(request): # funsionumiz request parametreisini alır
    # djagonun render funsionu 
    return render(request, 'account/registration/email_kntrl-passed.html') # render funksionutla istnileren html yönlendirilir 

def email_gonder(request):# funsionumiz request parametreisini alır
    # djagonun render funsionu 
    return render(request, 'account/registration/email_kntrl-gonder.html')# render funksionutla istnileren html yönlendirilir 

def email_UNpss(request):# funsionumiz request parametreisini alır
    # djagonun render funsionu
    return render(request, 'account/registration/email_kntrl-UNpss.html')# render funksionutla istnileren html yönlendirilir  
 
 
 







#-------****************BURAYA TEKRAR BAKKKK*************-----------------------



from django.contrib import messages




@login_required(login_url='custom-login-view') # giripş yapmamişssa login sayfaya git
def userProfileM(request): # http request alır 
    
    user_form = User_günccelle(instance=request.user) #maevcut giriş yapmıs kullanıcının bilgilerini içeren form örneği oluşturur
    
    
    if request.method == 'POST': # istek post ise 
        
        user_form = User_günccelle(request.POST, instance=request.user) # formun geçerliligi kontrol edilir
        if user_form.is_valid(): # valid ile geçerli mi diye bakılır
            user_form.save() # kaydedyer profılı gnceller 
            
            
            #mesajlar önemli
            messages.success(request, 'Your profile was successfully updated!') # succsse messer bu olr
            
            return redirect('Anaekran') # ana ekran gier
        else:  # hata varsa eror verir
            messages.error(request, 'Please correct the error below.') # error bu 
    return render(request, 'account/UserProfile.html', {'user_form': user_form}) # sayfaya yönlendirir 






@login_required(login_url='custom-login-view') # login yapanlar 
def hesapsil(request):
    
    user= User.objects.get(id=request.user.id) # userden id alını
    
    if request.method == 'POST': # eger istek posstas
        user.delete()  # user silinir
        return redirect('shops') # shopa gidilir
    
    
    return render(request,'account/hesapSil.html') # yoksa  hesapsil htmle gidilir






#https://forum.djangoproject.com/t/customize-django-auth-login-functionality/24022
#https://stackoverflow.com/questions/56231547/register-form-in-django-wont-post-the-request-method

def KayitView(request):
    form = KulaniciOlustur() # bos form oluşturum form bölumunden

    if request.method == 'POST': # istek post ise
        
        form2 = KulaniciOlustur(request.POST) # formun geçerliligi kontrol
        
        form = KulaniciOlustur(request.POST) # veriler le form oluşturulur
        
        if form.is_valid(): # formun geçerli olup olmadığı konrol
            
            user = form.save(commit=False) # kulancı nesnesi oluşturulur ama veri tabanına 
           
            user.is_active = False #kulanıcı aktif değil olarak işaretlenir 
            
            user.save() # kullanıcı kaydedildi 

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk)) # kullanıcının idis based64 kodlanır
            token = activation_token_generator.make_token(user) # kulanıcı için aktivasyon token gelir
            current_site = get_current_site(request) # mevcut sie bilgisi alın
            subject = 'Account Verification Email' # email konus
            
            message = render_to_string('account/registration/email_kntrl.html', {
                'user': user,
                
                'domain': current_site.domain, # domain falan
                
                'uid': uidb64,  #şalona kodlanmış ıd eklenir 
                'token': token, # sablona aktivasyon eklenır
                
            })

            logger.debug(f"Current Site: {current_site}, UID: {uidb64}, Token: {token}") # hata ayıklama 
            logger.debug(f"UID: {uidb64}, Token: {token}") # hata ayıklama

            user.email_user(subject=subject, message=message, from_email=None)  # E Email gönderilir (from_email gerekli ise belirtilmeli)
            return redirect('email-gonder') # Email gönderildi onayı
    else:
        form = KulaniciOlustur() # boş form 

    context = {'form': form} # form form
    return render(request, 'account/registration/registration.html', context) #Şablon render edilip kullanıcıya gösterilir
#****************************-----------------------------


def user_logout(request):
    # çıkıs yapsın kullanıcı
    logout(request)
    # mesaja ekla başarılı diye
    #messages.add_message(request, messages.SUCCESS, 'You have been successfully logged out.')
    # shop sayfasıne git
    return redirect('shops')





def custom_login_view(request):
    form=Custom_Login_Form21() # bos form oluştur yukardakı gibi 
    
    
    if request.method == 'POST': # istek post sa 
        form = Custom_Login_Form21(data=request.POST) # verilerle post olustur 
        
        if form.is_valid(): # valid mı ona bak 
            user2 = form.get_user() # user objesi al
            
            username=request.POST.get('username') # adı al 
            
            passwordanKul=request.POST.get('password') # password al
            
            
            user = form.get_user() # fordan kulanıcı nesnesi oluştu
            
            login(request, user) # kulanıcı oturumda başlar
            return redirect("Anaekran")
    else: # else olursa
        form = Custom_Login_Form21() # bos form yap 

    return render(request, 'account/Login.html', {
        'form': form}) # render ettt













#------------

#buraya tekrarbak

@login_required(login_url='custom-login-view') # login lazım


def track(request): #reuest parametresi
    context = {}  # boş sözlük oluştur
    try:
        
        order_details = OrderDetail.objects.filter(customer_order__customer=request.user) # detayları al siparişten
        
        context['order_details'] = order_details # contextte ekle siparişs detayları
        
        
    except OrderDetail.DoesNotExist: # hata işlemi
        
        
        context['error'] = "Order details not found." # detaylar bulunmazsa hata dönder 
    except Exception as e: # baska hata özellig
        
        context['error'] = str(e) # hata dönder 

    return render(request, 'account/orders.html', context=context) # şablonları renderle 



#------?





#-----------------------------------------





















#import hesap.forms
#print(dir(hesap.forms))


@login_required(login_url='custom-login-view') # login olmadan giremez
def Anaekran(request): # request parametresi
    # bak kullanıcı uygun mu
    if not request.user.is_authenticated:
        # eger olmazsa logine aktar
        return redirect(reverse('custom-login-view'))
    # ana sayfaya aktar
    return render(request, 'account/Anaekran.html')








#https://forum.djangoproject.com/t/cant-reuse-request-user-id-while-saving-a-form/5540/2
@login_required(login_url='custom-login-view') # logisiz işlem yok 
def manage_shipping(request): # request parametresiyle detay
    
    
    #try
    try:
        shipping = ShippingAdress.objects.get(user=request.user.id) # mevcut adres alınır 

    except ShippingAdress.DoesNotExist: # eror için
        
        shipping = None # kargo yoksa none olrak ayarla 
        
        
    form = ShippingForm(instance=shipping) # kardo adresi varsa form bbunla başlar 
    
    if request.method == 'POST': # eger post ile gönderildiyse 
        form = ShippingForm(request.POST, instance=shipping) #verileriyle yeni bir form oluşturulur
        if form.is_valid(): # valıd kontrıl et 
            shipping = form.save(commit=False) #Formdan alınan verilerle kargo adresi nesnesi oluşturulur, ancak henüz veritabanına kaydedilmez.
            shipping.user = request.user # Kargo adresi nesnesine kullanıcı atanır.
            shipping.save() # kaydedilir
            return redirect('Anaekran') # sayfaya yönlendir
        
    return render(request, 'account/manageShipping.html', {'form': form}) # form mu  'manageShipping.html' şablonuna gönderir 