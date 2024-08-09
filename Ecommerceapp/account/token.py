

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


#https://forum.djangoproject.com/t/django-passwordresettokengenerator/5872


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp): #token olusturmak için kulanılacak
        user_id_str = six.text_type(user.pk) # id stringe çevrilir
        timestamp_str = six.text_type(timestamp) # zaman damgasi sirtnge çevirrilir
        is_user_active = six.text_type(user.is_active) # kulanıcını akti durumu stringe çevrilir 
        return f"{user_id_str}{timestamp_str}{is_user_active}" # bu degerler irlestirilerek hash degeri olusturulur

activation_token_generator = TokenGenerator() # TokenGenerator sınıfından bir nesne oluşturulur