from rest_framework.serializers import HyperlinkedModelSerializer
from django.contrib.auth.models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        Model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        serializer_class 