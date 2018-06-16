"""newtown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views as flat_views

from . import views

#NOTE: flatpages are stored in DB ONLY and need to be manually exported into production
#also means Django DB needs to be seriously backed up

urlpatterns = [
	url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls),
	url(r'^jewelry/', include('jewelry.urls')),
	url(r'^contact/',include('contact.urls')),
	url(r'^about/$',flat_views.flatpage,{'url':'/about/'},name='about'),
	url(r'^terms_of_use/$',flat_views.flatpage,{'url':'/terms_of_use/'},name='terms_of_use'),
	url(r'^privacy_policy/$',flat_views.flatpage,{'url':'/privacy_policy/'},name='privacy_policy'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
