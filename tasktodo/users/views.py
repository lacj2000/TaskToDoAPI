
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.contrib.auth.models import User

from users.serializers import UserSerializer

from django.http import Http404



class UserList(generics.ListAPIView):
    name = 'users-list'
    permission_classes = (IsAdminUser)
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetail(generics.RetrieveAPIView):
    name = 'user-detail'
    permission_classes = (IsAuthenticated)
    serializer_class = UserSerializer
    queryset = User.objects.all()
