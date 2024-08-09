



from django.core.exceptions import ValidationError
from django.core.validators import validate_email




from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.forms import AuthenticationForm
from django import forms


from django.core.validators import EmailValidator

#https://stackoverflow.com/questions/62993594/does-the-usercreationform-from-the-django-contrib-auth-forms-in-django-not-work
#https://dev.to/balt1794/registration-page-using-usercreationform-django-part-2-2fg
#Udemy Tutorial :https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class KulaniciOlustur(UserCreationForm): # usercreation sınıfını genişletiyoruz
#
    class Meta:
        # meta clası model dedde olusturdum
        model = User # User modelini kullanıyoruz
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email') # form da kulanılacak alan
        widgets = {
            'password1': forms.PasswordInput(), # pasaport aiçin alan
            'password2': forms.PasswordInput(), # pasaport için alan
        }

    def __init__(self, *args, **kwargs): # Formun başlatıcısını (initializer) tanımlar
        super(KulaniciOlustur, self).__init__(*args, **kwargs) # Üst sınıfın başlatıcısını çağırır
        email_field = self.fields['email']
        
        email_field.required = True # email alanını zorunlu hale getirir

    def clean_email(self): # email alanı için özel bir temizleme (validation) metodunu tanımlar
        email = self.cleaned_data.get("email") # Formdan girilen email değerini alır

        # Kontroll et eger email valid se
        self._validate_email(email)
        self._check_existing_email(email)
        self._check_email_length(email)

        return email # return edilir

    def _validate_email(self, email):
        try:
            
            validate_email(email) # valid mi değilmi bakıl
        except forms.ValidationError: # eror kontrol
            
            raise forms.ValidationError('Enter a valid email address.') # eror kontrol

    def _check_existing_email(self, email):
        if User.objects.filter(email=email).exists():  # email veri tabanında olup olmadıgı kontrol edilir
            raise forms.ValidationError('This email is already in use.') # varsa hata verilir

    def _check_email_length(self, email):
        if len(email) >= 350: # email uzunlugu kontrol edilir
            raise forms.ValidationError("Email is too long") # mesaj geri döner



###


class Custom_Login_Form21(AuthenticationForm):  #  AuthenticationForm sınıfını genişletiyoruz
    # burası önem li
    
    username = forms.CharField(
        
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}) # place holderlar özelleştir
    )
    # pasaport charfield içn önemli
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}) # place holderlar özelleştir
    )

class User_günccelle(forms.ModelForm):  # Django'nun ModelForm sınıfını genişleten özel bir
    
    password = None # şifre alanı formdan kaldırır

    class Meta:
        model = User # Formun hangi modelle ilişkili olduğunu belirtir
        fields = ['username', 'email'] # formda kulanılacak alanları belilrler

    def __init__(self, *args, **kwargs): # Formun başlatıcısını (initializer) tanımlar
        super(User_günccelle, self).__init__(*args, **kwargs) # Üst sınıfın başlatıcısını çağırır
        self._setup_email_field()

    def _setup_email_field(self): # email alanını ayarlayan özel bir metod
        email_field = self.fields['email']
        email_field.required = True # email doldurma zorunlu 
        email_field.validators.append(EmailValidator()) # email alanına EmailValidator ekler

    def clean(self): # Formun temizleme (validation) metodunu tanımlar
        cleaned_data = super(User_günccelle, self).clean() # Üst sınıfın temizleme metodunu çağırır
        email = cleaned_data.get('email') # Temizlenmiş verilerden email değerini alır

        if email:
            self._validate_unique_email(email)
            self._validate_email_length(email)

        return cleaned_data # Temizlenmiş verileri geri döner

    def _validate_unique_email(self, email):
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists(): # Email'in veritabanında başka bir kullanıcıya ait olup olmadığını kontrol eder
            self.add_error('email', ValidationError('This email is invalid')) # Varsa hata mesajı ekler

    def _validate_email_length(self, email):
        if len(email) >= 350: # uzunluk kontrol edilir
            self.add_error('email', ValidationError("Your email is too long")) # Varsa hata mesajı ekler
        