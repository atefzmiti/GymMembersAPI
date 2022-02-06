"""fitnessgym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from equipments import views
from gymmembers.views import insert_member,getListmembers,update_member,getOnemember,delete_member,home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gym/',views.getequipmentsList,name='getequipmentsLit'),
    # creating members
    path('newmember/', insert_member,name='insert_member'),
    path('', home),
    # getmembers
    path('getmembers/', getListmembers, name='getListmembers'),
    # getmembers by id
    path('getmembers/<str:id>/', getOnemember, name='getListmembers'),
    path('updatemembers/<str:id>', update_member, name='update_member'),
    path('delete/<str:id>/', delete_member, name='delete_member'),

]
