import json
from .models import UrunKategorisi,MagazaUrunu
from django.views.decorators.http import require_POST
from django.shortcuts import render
# burad da tamam 

from django.shortcuts import get_object_or_404
# Create your views here.

from django.http import JsonResponse

 
   # Note:  This code develop and  formatted with  AI.
   # with help source :https://docs.djangoproject.com/en/5.0/ref/request-response/
   # https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/




def shops(request):
    # MAgaza urunu
    tum_MagazaUrunu = MagazaUrunu.objects.all() #Bu satır, veritabanındaki MagazaUrunu modelinden tüm nesneleri (ürünleri) alır. tüm veritabanı kayıtlarını bir queryset (sorgu seti) olarak döndürür.
    
    
    
    #urunyayımı
    
    context1 = {
       # 'tum_UrunKategorisi': tum_UrunKategorisi
    }
    
    context = {
        #key and value
        'tum_MagazaUrunu': tum_MagazaUrunu
    } # Bu satır, alınan ürünlerin bir sözlüğe (context) eklenmesini sağlar.
    
    
    return render(request,'shops/anasayfa.html',context) #Bu satır, Django'nun render fonksiyonunu kullanarak, isteği (request), HTML şablonunun yolunu ('shops/anasayfa.html') ve context sözlüğünü parametre olarak alır. render fonksiyonu, belirtilen şablonu kullanarak bir HTML sayfası oluşturur ve bu sayfayı içeren bir HTTP yanıtı döndürür




# def urun_kategori(request): # burada navbardaki ürünleri daha iyi hategori etmek için kukanılaca
#     #ve filtre görevi görecek
#     tum_UrunKategorisi = UrunKategorisi.objects.all()

    
#     context = {
#         'tum_UrunKategorisi': tum_UrunKategorisi
#     }
    
    
#     return render(request, 'shops/urun_kategori.html', context)





def urun_kategori(request):# burada navbardaki ürünleri daha iyi hategori etmek için kukanılaca loop yaptım navbarda
    #ve filtre görevi görecek
    tum_UrunKategorisi = UrunKategorisi.objects.all()
    
    context1 = {
         'tum_UrunKategorisi': tum_UrunKategorisi
   }
    
    context2={
        'tum_pro':tum_UrunKategorisi
        
    }
    
    return{'tum_UrunKategorisi':tum_UrunKategorisi}




#magaze urunu



#urun_detay pro info
def urun_detay(request, yol_kodu): # Bu fonksiyon, verilen yol_adi parametresine göre bir ürün kategorisini ve bu kategoriye ait ürünleri bulup, 
                                            #bunları bir HTML şablonunda göstermek için bir context içinde döndürür. 
                                            # Eğer belirtilen kategori bulunamazsa, 404 hatası döndürür.
    
    #burada ürünün detayına ulaşmak
    
    #urun_detay1 = MagazaUrunu.objects.get() #burada ürünün detayına
    
    
    urun_detay = get_object_or_404(MagazaUrunu, yol_kodu=yol_kodu)
    
    
    saved_rating = request.session.get(f'product_{urun_detay.id}_rating', 0) # defaoul 0  burda, request.session kullanıcının oturum verilerine erişim sağlar
    # get metodu, oturumdaki key anahtarına karşılık gelen değeri döner.,
    # Eger bu anahtar  yoksa, default değer gelir oda 0 dır


    # icerigimz burad belirlenir 
    icerik = {
        'urun_detay': urun_detay,
        'saved_rating': saved_rating,
    }
    return render(request, 'shops/urun_detay.html', icerik)# rende funsiyonuyla içerik htmlt dödürülür



#kategori_detay
def kategori_detay(request, yol_adi=None): # Bu fonksiyon, verilen yol_adi parametresine göre bir ürün kategorisini ve bu kategoriye ait ürünleri bulup, 
                                            #bunları bir HTML şablonunda göstermek için bir context içinde döndürür. 
                                            # Eğer belirtilen kategori bulunamazsa, 404 hatası döndürür.
    
    
    
    urun_kategorisi = get_object_or_404(UrunKategorisi, yol_adi=yol_adi)# burada belirtlen funksionla objec alınır
    #eger objemiz mevcut değilse  eror 404 dönderir harika bir funktion
    
    urunler = MagazaUrunu.objects.filter(kategori=urun_kategorisi)    # urunlerimez burada katagoriye göre filreleneir
    
    # icerigimz burad belirlenir 
    icerik = {
        'urun_detay': urun_kategorisi,
        'urunler': urunler
    }
    
    return render(request, 'shops/kategori_detay.html', icerik) # rende funsiyonuyla içerik htmlt dödürülür



#--------------------*******************************************
#buraya dikkattt-------------

from django.db.models import Q

def search_results(request): #HTTP GET isteği alarak
    
    query = request.GET.get('q') #URL'den q adlı sorgu parametresi örnek olarak http://example.com/search?q=elma, query değişkeni elma olur.
    results = [] # boş liste olmuştur burda bunu html de for loop pun içinde kullanılır
    if query:
        results = MagazaUrunu.objects.filter( #veritabanında arama yapılır.
                                             
            Q(urun_adi__icontains=query) | Q(urun_tanimi__icontains=query) # Q nesnesi, Django'nun django.db.models modülünden gelir ve karmaşık sorgular oluşturmayı sağlar.
        )   #urun_adi query içerip içermedigini kontrol eder diğerirde öyle
        
    return render(request, 'shops/search_results.html', {'results': results, 'query': query}) # render html bağlantı oluşturur

from decimal import Decimal





# Develop with help Aİ

@require_POST # yanlızca http post istekleri 

def rate_product(request): # HTTP POST istegiy başlar .  
    #request   Django HttpRequest nesnesidir.
    rating = request.POST.get('rating') # rating parametresini all
    
    
    
    product_id = request.POST.get('product_id') # id parametresini all
    
    
    
    try:
        rating = float(rating) # rating degerini floatta çevir 
    except ValueError:
        return JsonResponse({'error': 'Invalid rating value'}, status=400)
    
    ürün = MagazaUrunu.objects.get(id=product_id) # product_id eşlesen magaza ürünü al
    ürün.update_rating(rating) # rating  model.py update et 
    
    return JsonResponse({'success': 'Rating submitted successfully'}) # başarı içeren json döndürür

#---------------********************************i

def imprint_view(request):
    return render(request, 'shops/imprint.html')


def about_us(request):
    return render(request, 'shops/about_us.html')

def genel_kosullar(request):
    return render(request, 'shops/genel_kosullar.html')



#from django import templsd

#register = template.Library()

#11@register.filter # burayı sonradan kullan no need it 
#def first_two_sentences(value):
 #   sentences = value.split('. ')
  #  return '. '.join(sentences[:2]) + ('.' if len(sentences) > 2 else '')1