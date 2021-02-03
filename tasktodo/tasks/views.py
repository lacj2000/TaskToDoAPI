from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User

from tasks.models import Task, Sublist, Item
from tasks.serializers import TaskSerializer
from tasks.exceptions import AccessItemException

from django.http import Http404


class TaskList(generics.ListCreateAPIView):
    name = 'tasks-list'
    serializer_class = TaskSerializer
    permission_classes  =[IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if bool(self.request.user):   
            return Task.objects.filter(user=self.request.user)
        raise AccessItemException

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    name = 'task-detail'
    serializer_class = TaskSerializer
    permission_classes  = [IsAuthenticated]
    
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if bool(self.request.user):
            return Task.objects.filter(user=self.request.user)
        raise AccessItemException