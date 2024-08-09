from django.contrib import admin

# Register your models here.

from .models import UrunKategorisi, MagazaUrunu


#admin.site.register(UrunKategorisi)


#admin.site.register(MagazaUrunu)


@admin.register(UrunKategorisi)
class UrunKategorisiAdmin(admin.ModelAdmin):
    
    list_display = ['etiket', 'yol_adi']
    prepopulated_fields = {'yol_adi': ('etiket',)} # kategöry yazdıgımızda  dırek slug gi yazacak
    
# admin panelinde ayarlmalarr olmalı
    
@admin.register(MagazaUrunu)
class MagazaUrunuAdmin(admin.ModelAdmin): # produck  yazdıgımızda  dırek slug gi yazacak
    
    list_display = ['urun_adi', 'uretici', 'fiyat', 'stok_miktari', 'stokta_var'] # displayde gösterilecek ler
    list_editable = ['fiyat', 'stok_miktari', 'stokta_var'] # etitlemali olacaklar
    prepopulated_fields = {'yol_kodu': ('urun_adi',)} # yol codu çok öen arz ediyor