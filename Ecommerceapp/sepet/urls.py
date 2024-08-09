"""
URL configuration for Ecommerceapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from django.conf import settings

from django.contrib.auth import views as auth_views

from . import views



##her zaman olduğu gibi url belirlenir
urlpatterns = [
    
    
    path('', views.sepet_toplam,name='sepet-toplam'), # burada views kulanmaya bilirdi
    
    
    path('guncelle/', views.sepet_guncelle,name='sepet-guncelle'),
    
    
    path('ekle/', views.sepet_ekle,name='sepet-ekle'),
    
    
    path('sil/', views.sepet_sil,name='sepet-sil'),
    
   # path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]




