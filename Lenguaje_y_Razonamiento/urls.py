"""Lenguaje_y_Razonamiento URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from PTGRIS.views import *


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^gris/$', Home.as_view(), name='home'),
    url(r'^busqueda/$', busqueda, name='busqueda'),
    url(r'^gris/busquedas/$', get_busquedas, name='get_busquedas'),
    url(r'^gris/down_csv/$', get_csv, name='get_busquedas'),
    url(r'^gris/down_json/$', get_json, name='get_busquedas'),
]
