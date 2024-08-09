from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from .views import payment_success,payment_fail,odeme,complete_order


class CustomPasswordResetView(auth_views.PasswordResetView): # burada problem vardı
    def get(self, request, *args, **kwargs): # 
        print("Using template: ", self.template_name)
        return super().get(request, *args, **kwargs)


urlpatterns = [
    # https://forum.djangoproject.com/t/reverse-for-password-reset-confirm-not-found/9788

    # re_path('yeniparola', auth_views.PasswordResetView.as_view(template_name="hesap/sifre/sifre-yenileme.html"), name='yeniparola'),
    # re_path('yeniparolaGönderildi', auth_views.PasswordResetDoneView.as_view(template_name="hesap/sifre/sifre-yenileme-gönderildi.html"), name='yeniparolaGönderildi'),
    # re_path('yenilemeTamamlandi/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="hesap/sifre/sifre-yenileme-form.html"), name='yenilemeTamamlandi'),
    # re_path('yenilemeBasarili', auth_views.PasswordResetCompleteView.as_view(template_name="hesap/sifre/sifre-yenileme-tamamlandi.html"), name='yenile
    
    
        path('complete_order/', complete_order, name='complete_order'),
    #payment success
    path('payment_success/', payment_success, name='payment_success'),
    
    #payment fail
    path('payment_fail/', payment_fail, name='payment_fail'),
    
    
    path('odeme/', odeme, name='odeme'),

    
     
]