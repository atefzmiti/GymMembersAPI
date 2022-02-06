print("hi atef , we have to complete the main project in a few days")
# from django.db import models
#
#
# class Member(models.Model):
#     id = models.IntegerField
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     age = models.IntegerField
#     discipline = models.CharField(max_length=200)
#     start_date = models.DateTimeField(max_length=200)
#     end_date = models.DateTimeField(max_length=200)
#     email=models.EmailField(max_length=200)
{   "id" : 1,
    "first_name" : "atef",
    "last_name" :"zmiti",
    "discipline" : "kickboxing",
    "start_date" : "01-01-2020",
    "end_date" : "01-01-2021",
    "email" : "zmitiatef@gmail.com"}
# @api_view(['POST'])
# def insert_member(request):
#     if request.method == "POST":
#         # data = JSONParser().parse(request.data)
#         member_serializer = MemberSerializer(data=request.data)
#         if member_serializer.is_valid():
#             member_serializer.save()
#             return Response(member_serializer.data,status=201)
#         return Response(member_serializer.data,status=400)


# @api_view(['POST'])
# def insert_member(request):
#     if request.method == "POST":
#         data = JSONParser().parse(request.data)
#         serializer = MemberSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.data,status=400)
