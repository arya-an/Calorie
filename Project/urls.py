"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from App import views
from App.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.register,name='register'),
    path('login/',views.loginpage,name='login'),
    path('userhome/',views.userhome,name='userhome'),
    path('addfood/', FoodCreate.as_view(),name='addfood'),
    path('addactivity/', ActivityCreate.as_view(),name='addactivity'),
    path('flist/',views.foodlist,name='flist'),
    path('alist/',views.activitylist,name='alist'),
    path('logout/',views.custom_logout,name='logout'),
    path('adduserfood/<int:id>',views.adduserfood,name='adduserfood'),
   
]

