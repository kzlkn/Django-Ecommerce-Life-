from decimal import Decimal
from shops.models import MagazaUrunu

class Sepet:
    def __init__(self, request): #objesi alır.
        self.session = request.session # self.session ile oturum (session) objesine erişir
        sepet = self.session.get('session_key', {}) #session_key adında bir oturum anahtarıyla sepeti alır 
        self.sepet = sepet # self.sepet ile bu sepeti sınıfın bir özelliği olarak saklar.


#https://stackoverflow.com/questions/70587579/itemtotal-price-itemprice-itemquantity-keyerror-quantity
#https://stackoverflow.com/questions/49355760/numbers-saved-in-django-session-automatically-rounded-down-when-computing-item-s
#source https://www.udemy.com/course/python-django-build-an-e-commerce-store-2022 
    
    
    
    def ekle(self, urun, urun_miktari=1): # parametreler alınır
        urun_detay_id = str(urun.id) # urun id sis string olrak alınır
        if urun_detay_id in self.sepet: # urun sepette varsa mikarı arttıtrılır
            
            
            self.sepet[urun_detay_id]['miktar'] += urun_miktari
        else:# yoksa  yoksa fiyat ve miktar  bilgileriyle ekler 
            self.sepet[urun_detay_id] = {'price': str(urun.fiyat), 'miktar': urun_miktari}
        self.save() # sepeti kaydeder

    def __iter__(self): # tüm urun idleri alır
        all_product_ids = self.sepet.keys() # # bu idlerle veri tabanın dan urun bilgilerini alır
        products = MagazaUrunu.objects.filter(id__in=all_product_ids)# idlre göre filte
        sepet = self.sepet.copy() 

# her urun için sepet güncellenir
        for product in products:
            sepet[str(product.id)]['product'] = product

# fiyat ve toplam turtar dödurulur 
        for item in sepet.values():
            item['price'] = Decimal(item['price'])
            item['total'] = item['price'] * item['miktar']
            yield item

    def sil(self, urun):
        urun_id = str(urun) # urun id alınır
        if urun_id in self.sepet: # urun sepette varsa siler
            del self.sepet[urun_id] 
            self.save() # kaydeder

    def __len__(self):
        return sum(item['miktar'] for item in self.sepet.values()) # sepetteki toplam ürün sayısını döner 

    def save(self): # sepetoturuma kaydeder ve degismiş olarak işsaetler 
        self.session['session_key'] = self.sepet
        self.session.modified = True

    def clear(self): #epeti temizler ve oturumu değişmiş olarak işaretler.
        self.session['session_key'] = {}
        self.session.modified = True

    def get_total(self): #epetteki ürünlerin toplam tutarını hesaplar ve döner.
        total = sum(Decimal(item['price']) * item['miktar'] for item in self.sepet.values())
        return total

    def guncelle(self, urun, miktar): #urun_id ile ürünün ID'sini alır.
#Ürün sepette varsa, miktarını günceller ve self.save() ile kaydeder.
        urun_id = str(urun)
        if urun_id in self.sepet:
            self.sepet[urun_id]['miktar'] = miktar
            self.save()
