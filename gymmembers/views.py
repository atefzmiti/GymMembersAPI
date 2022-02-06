from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Member
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MemberSerializer
from rest_framework.decorators import api_view
from rest_framework import status


def home(request):
    member = Member.objects.all()
    return render(request, 'index.html', {'members': member})


@api_view(['POST'])
def insert_member(request):
    if request.method == "POST":
        # data = JSONParser().parse(request.data)
        serializer = serializers.MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)


# creating members and inserting them to database
@api_view(['POST'])
def update_member(request, id):
    # data = JSONParser().parse(request.data)
    listmembers = Member.objects.get(id=id)
    serializer = serializers.MemberSerializer(instance=listmembers, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


# get members
@api_view(['GET'])
def getListmembers(request):
    if request.method == 'GET':
        listmembers = Member.objects.all()
        serialize = MemberSerializer(listmembers, many=True)
        return Response(serialize.data)


#             return JsonResponse(member_serializer.data)
#         return JsonResponse(member_serializer.data)

# getmember by id

@api_view(['GET'])
def getOnemember(request, id):
    if request.method == 'GET':
        listmembers = Member.objects.get(id=id)
        serialize = MemberSerializer(listmembers, many=False)
        return Response(serialize.data)


# deleting member by id
@api_view(['DELETE'])
def delete_member(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    return Response('member deleted succefully')
