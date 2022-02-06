from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view

from .models import equipment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import equipmentSerializer

def index(request):
    listequipments=equipment.objects.all()
    return JsonResponse("API",safe=False)

def new(request):
    return HttpResponse('hiiii ')


@api_view(['GET'])
def getequipmentsList(request):
    if request.method == 'GET':
        listequipments = equipment.objects.all()
        serialize=equipmentSerializer(listequipments,many=True)
        return Response(serialize.data)



