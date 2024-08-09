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
urlpatterns = [
    path("admin/", admin.site.urls),
    
    
    
    #
    #include kullanıldu shop urlsleriini dahil edebilmek için
    path("", include('shops.urls')),
    
    
    # burada sepet urlsini balıyoruz ana appe
    #sepet url
    path('sepet/', include('sepet.urls')),
    
    
    #hesap
    path('account/', include('account.urls')),
    
    path('payment/', include('payment.urls')),
    
    
    
    #useradmin
    
    
]



#https://stackoverflow.com/questions/5517950/django-media-url-and-media-root
#Bu kod Django'da, geliştirme sırasında medya dosyalarını (MEDIA_URL ile belirtilen) sunmak için URL desenlerine (urlpatterns) bir yol ekler.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)