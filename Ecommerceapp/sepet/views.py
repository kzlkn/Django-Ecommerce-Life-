
# feed back benden çok iyi yazdın buraya tekrar bakma



from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseNotAllowed



#https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022/

from .sepet import Sepet
from shops.models import MagazaUrunu
from django.views.decorators.http import require_POST


@require_POST # hhtp post istegi gerektir
def sepet_guncelle(request): # request parametresit almalı      
    # sepet oluştururlur 
    sepet = Sepet(request)

    if request.POST.get('action') == 'post': # aksionda post komutu ükicik olmalı
        
        #test için bunu yaptım
        print(request.POST)  
        
        urunid_str = request.POST.get('urun_detay_id') #)# ürün ID'si ve miktarını alırr(post istegiğndene alınır) <>> önem arz ediyor
        urunmktr_str = request.POST.get('urun_miktar')#)# ürün ID'si ve miktarını alır
        
        if urunid_str is None or urunmktr_str is None: #paramekrelererimizi olup olmadığı kontrol edilır burda biri eksik olursa eğer eror dondurur
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        try:
            urunid = int(urunid_str) # alınana değerlerir integer e çevir 
            urunmktr = int(urunmktr_str)
        except ValueError: # eğer alınan değerle sayı değilse eror dönder bize
            return JsonResponse({'error': 'Invalid input type'}, status=400)
        
        
        print(f"Sepet before update: {sepet.sepet}") # consol için test
        
        sepet.guncelle(urun=urunid, miktar=urunmktr) # sepet burada verielen parapetrelerle günçellenir
        
       
        print(f"Sepet after update: {sepet.sepet}") # güncellenmiş sepet yazdir 
        
        sepetMktr = sepet.__len__() # sepetekş toplam miktar ve toplam fiat alınır
        sepetHepsi = sepet.get_total()
        
        response = JsonResponse({'miktar': sepetMktr, 'hepsi': sepetHepsi})  # bu bilgiler Json olarak istemciye göderilkece
        print(f"Response: {response.content}")  
        return response

    return JsonResponse({'error': 'Invalid request'}, status=400) # post isteginde action post değilse hata ver 

















@require_POST # POST HTTP isteklerinde çagrılır 
def sepet_sil(request): # request nesnesi parametre
    sepet = Sepet(request)# ssepet nesnesi
    action = request.POST.get('action', '').lower()#post istegindeki action alanının degerini alır ve küçük harve dönüştürür. eger action alani post isteğinde yoksa bos string döner

    if action == 'post': # action post mu ona baklır
        urunid_str = request.POST.get('urunid') # post isteginde ur
        urun_detay_id = request.POST.get('urun_detay_id', 0) # defult 0 urun id is al
        sepet.sil(urun=urun_detay_id) # sil founktionında sepeti sil (sil funktionu sepet.py den geliyor)
        
        sepet_miktar = sepet.__len__() # sepet miktarı ve toplam para
        sepet_hepsi = sepet.get_total()
        
        
        
        response_data = { # sndurulmesi istedigimize data
        'quantity': sepet_miktar,
        'total': sepet_hepsi
    }
        
        
        return JsonResponse(response_data) # json data olarak dönder
    
    return JsonResponse({'error': 'Invalid request'}, status=400) # post isteginde action post değilse hata ver















def sepet_toplam(request):#sepettoplam request parametresi ile
    # sepet nesnes la
    
    sepet = Sepet(request)
    #sonra sepet iciçndekileri liste yap
    sepet_items = list(sepet)
    #sepettin total miktari all
    total_amount = sepet.get_total()
    
    
    #bunları render la html gönder 
    return render(request, 'sepet/sepet_toplam.html', {'sepet_items': sepet_items, 'total_amount': total_amount})










@require_POST
def sepet_ekle(request):
    sepet = Sepet(request)
    action = request.POST.get('action', '').lower() #  POST verilerinden alınan ve küçük harfe dönüştürülen bir parametredir html küçük yazıldı çünkü

    if action == 'post':
        try:
            urun_detay_id = int(request.POST.get('urun_detay_id', 0))# ürün ID'si ve miktarını alır. sayi olmalı tam sayıyadönüştürülür 
            urun_miktari = int(request.POST.get('urun_miktari', 1))
            
            if urun_detay_id <= 0 or urun_miktari <= 0:
                return JsonResponse({'error': 'Invalid product ID or quantity'}, status=400)
            
            urun = get_object_or_404(MagazaUrunu, id=urun_detay_id) ## veritabanı urunu al ürün yoksa error
            sepet.ekle(urun=urun, urun_miktari=urun_miktari)
            sepetTekisayilar = len(sepet) # sepetleteki ürünlerin sayısıs
            
            return JsonResponse({'miktar': sepetTekisayilar}) # sjson dödedet try ve exepten 
        
        except ValueError: # parametreler yanlışsa eror ver
            return JsonResponse({'error': 'Invalid input data'}, status=400)
    
    return JsonResponse({'error': 'Invalid action'}, status=400) # post isteginde action post değilse hata ver 
