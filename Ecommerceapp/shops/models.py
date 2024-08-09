from django.db import models
from decimal import Decimal

from django.urls import reverse
#https://stackoverflow.com/questions/64039232/django-forms-modelform-slugfield-db-index-true
#https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/
class UrunKategorisi(models.Model):  # magaza için kategory oluşturulur 
    
    etiket = models.CharField(max_length=300, db_index=True)  # kategori türü
    
    
    
    yol_adi = models.SlugField(max_length=300, unique=True)  # slug baglantı kurmak için
    
    class Meta: # ürünlerin çogalmtılması bğ nevi etiket ismi gibi
        ordering = ('etiket',)
        # etiket ismi
        verbose_name = 'Ürün Kategorisi' # tekil isim
        
        verbose_name_plural = 'Ürün Kategorileri' # admin sayfasında  cogul yapıyor
        
    def __str__(self):# urun isimniy dönsün
        return self.etiket # default olarak  numara olara döduruyour ama urunu yaraktıktan sonra ismiyle dönmesini istiyorum  (http://127.0.0.1:8000/admin/shops/urunkategorisi/)
    
    
    def get_absolute_url(self):  # url tanımı için burası
        return reverse("kategori-detay-gorunumu", args=[self.yol_adi]) # url ye isim yol ismi yazdiriyor

class MagazaUrunu(models.Model):  # hagazada ki eşyarlar için kullanulacak
    
    
    
    #https://forum.djangoproject.com/t/remove-foreign-key-field-from-model/21665/2
    kategori = models.ForeignKey(UrunKategorisi, related_name='urunler', on_delete=models.CASCADE, null=True)   # filre yapması için kullnılan code on_delete=models.CASCADE katekory removed produck also removed
    
    urun_adi = models.CharField(max_length=300) # charfield 300 luk olustur
    
    uretici = models.CharField(max_length=300, default='Generic') #yazı tyru ve 300 char
    
    
    urun_tanimi = models.TextField(blank=True) # urun detaylı anltımı icin text yeri bota kakabilr
    yol_kodu = models.SlugField(max_length=300) # yol adi çok öenli
    
    fiyat = models.DecimalField(max_digits=6, decimal_places=2) # fiay yeri çok önemli
    
    urun_resmi = models.ImageField(upload_to='urun_fotograflari2/')  # buraya unutma önemli fotolar burda olur bizim için folder yaptı
    
    stok_miktari = models.PositiveIntegerField() # positive sayı yeri
    stokta_var = models.BooleanField(default=True) # stokta var yok 
    
    
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0) # rating yer
    num_ratings = models.PositiveIntegerField(default=0) # posite sayi yeri
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0) # rating yeri
    
    
    # develop with Aİ
    def update_rating(self, new_rating): # rating funksionu nu çalıstırmak için views dall çağrılacak
        
        self.total_rating += Decimal(new_rating) # self kulanılarak sınıfın özelliklerine erişilirir sağdaiki deger sola eklenir new rating decimal olur
        self.num_ratings += 1 # 1 arrtır
        
        self.rating = self.total_rating / self.num_ratings # ortalama hesaplar
        
        self.save() # verir tabanına kaydeder 
    
    
    
    class Meta:  # değişim durumun da kullanılı
        ordering = ('urun_adi',) # yukarıkadik kodun aynısı çalışma prensii
        verbose_name = 'Magaza Urunu'
        verbose_name_plural = 'Magaza Urunleri' # admin sayfasında çogulyapıyor
        
    def __str__(self): # bude url eki sağlıyor
        return self.urun_adi # default olarak  numara olara döduruyour ama urunu yaraktıktan sonra ismiyle dönmesini istiyorum (http://127.0.0.1:8000/admin/shops/magazaurunu/)
    
    
    
    #https://stackoverflow.com/questions/70427774/django-get-absolute-url-calling-same-url-as-current-page
    def get_absolute_url(self):  # url tanımı için burası
        return reverse("urun-detay-gorunumu", args=[self.yol_kodu]) # diger kodlarda oldugu gibi çalışma prensibi 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class CustomerSupportRequest(models.Model):
#     subject = models.CharField(max_length=100, default="")
#     text = models.TextField(max_length=500)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     extended_user = models.ForeignKey(ExtendedUser, on_delete=models.CASCADE, default=None)
#     user_contact = models.CharField(max_length=100, default="")

#     class Meta:
#         ordering = ['timestamp']
#         verbose_name = 'Inquiry'
#         verbose_name_plural = 'Inquiries'

#     def __str__(self):
#         return self.subject + ' (' + self.extended_user.user.username + ')'

#     def __repr__(self):
#         return self.subject + ' (' + self.extended_user.user.username + ' / ' + str(self.timestamp) + ')'