
from rest_framework import generics, permissions

from django.contrib.auth.models import User



class UserList(generics.ListAPIView):
    name = 'users-list'
    permission_classes = [permissions.is_superuser]
    queryset  = User.objects.all()


class UserDetail(generics.RetrieveDestroyAPIView):
    name = 'users-detail'
    permission_classes = [permissions.is_authenticated]
    queryset  = User.objects.all()
