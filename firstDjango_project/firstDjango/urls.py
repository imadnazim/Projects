"""firstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.urls import path
from . import views # . means current dir, this will import views here in urls

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('gate/',views.gate),
    path('count/',views.count,name='count'),  # if url change also ,we can use name
    path('about/',views.about,name='about')
]
