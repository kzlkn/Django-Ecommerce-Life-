from django.urls import include, path, re_path
from django.contrib.auth import views as auth_views
from .views import track,KayitView, email_kntrl,manage_shipping, email_passed, email_gonder, email_UNpss, custom_login_view, Anaekran, user_logout, userProfileM, hesapsil


class CustomPasswordResetView(auth_views.PasswordResetView): # PasswordResetView sınıfını genişletiyorum 
    def get(self, request, *args, **kwargs): # get istegi aldıgında çalışacak 
        print("Using template: ", self.template_name) # hangi sablonun kulanıldıgı consola yazdır 
        return super().get(request, *args, **kwargs) # varsayılan get davranışı sürdür




# burada view kullanılmadı view kulanmadım  

urlpatterns = [
    
    
   path('ManageShipping/',manage_shipping, name='ManageShipping'),
    
    # https://forum.djangoproject.com/t/reverse-for-password-reset-confirm-not-found/9788

    # re_path('yeniparola', auth_views.PasswordResetView.as_view(template_name="hesap/sifre/sifre-yenileme.html"), name='yeniparola'),
    # re_path('yeniparolaGönderildi', auth_views.PasswordResetDoneView.as_view(template_name="hesap/sifre/sifre-yenileme-gönderildi.html"), name='yeniparolaGönderildi'),
    # re_path('yenilemeTamamlandi/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="hesap/sifre/sifre-yenileme-form.html"), name='yenilemeTamamlandi'),
    # re_path('yenilemeBasarili', auth_views.PasswordResetCompleteView.as_view(template_name="hesap/sifre/sifre-yenileme-tamamlandi.html"), name='yenilemeBasarili'),
    path('logout/', user_logout, name='logout'),
    path('reset_password', CustomPasswordResetView.as_view(template_name="account/password/password-reset.html"), name='reset_password'),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="account/password/password-reset-sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password/password-reset-form.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name="account/password/password-reset-complete.html"), name='password_reset_complete'),

    # userProfileM
    path('userProfileM/', userProfileM, name='userProfileM'),

    # hesapSil
    path('hesapsil/', hesapsil, name='hesapsil'),

    path('kayit/', KayitView, name='kayit'),
    path('email-kntrl/<str:uidb64>/<str:token>/', email_kntrl, name='email-kntrl'),
    path('email-passed/', email_passed, name='email-passed'),
    
    
    path('email-gonder/', email_gonder, name='email-gonder'),
    path('email-unpss/', email_UNpss, name='email-unpss'),
    path('user-logout', user_logout, name='user-logout'),
    path('custom-login-view/', custom_login_view, name='custom-login-view'),
    path('Anaekran/', Anaekran, name='Anaekran'),

    path('track',track,name='track')
    
]

