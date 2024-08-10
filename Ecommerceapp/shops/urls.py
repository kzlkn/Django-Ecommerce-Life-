



from django.shortcuts import render
from django.urls import path

from . import views 

urlpatterns = [


# url ler ayarlanır burda

    path('', views.shops, name='shops'),
path('kategori/<slug:yol_adi>/', views.kategori_detay, name='kategori-detay-gorunumu'), # url vies kulanmasamda olur du mama burd akullandım
path('urun/<slug:yol_kodu>/', views.urun_detay, name='urun-detay-gorunumu'),# burda da aynı 
    #path('arama/', views.arama, name='arama'),
    #path('sepet/', views.sepet, name='sepet'),
     path('imprint/', views.imprint_view, name='imprint'),
    path('about-us/', views.about_us, name='about_us'),
    path('genel-kosullar/', views.genel_kosullar, name='genel_kosullar'),
    
    
    path('search/', views.search_results, name='search_results'),
    path('rate-product/', views.rate_product, name='rate-product'), # views yaz bdğrer code
]
    
    