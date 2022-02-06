from rest_framework import serializers,routers,viewsets
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


router = routers.DefaultRouter()
router.register(r'newmember', UserViewSet)
