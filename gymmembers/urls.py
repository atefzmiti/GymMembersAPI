from django.urls import path,include
from django.conf.urls import url
from . import views



urlpatterns = [
    path('newmember', include('views.insert_member')),
    path('getmembers', include('views.getListmembers')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # path('newmember', views.insert_member),
]