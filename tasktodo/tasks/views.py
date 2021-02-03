from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


from django.contrib.auth.models import User

from tasks.models import Task, Sublist, Item
from tasks.serializers import TaskSerializer, SublistSerializer, ItemSerializer
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

class TaskCheck(APIView):
    name='task-check'
    permission_classes  =[IsAuthenticated]

    def get_context(self,request):
        return {'request':request}


    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        if task.check_user(request.user):
            task.get_check()
            serializer = TaskSerializer(task, context=self.get_context(request))
            return Response(serializer.data,status.HTTP_200_OK)
        raise AccessItemException

class TaskUncheck(TaskCheck):
    name = 'task-uncheck'
    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        if task.check_user(request.user):
            task.get_uncheck()
            serializer = TaskSerializer(task, context=self.get_context(request))
            return Response(serializer.data,status.HTTP_200_OK)
        raise AccessItemException



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('tasks-list', request=request, format=format),
        'users': reverse('users-list', request=request, format=format),
        # 'sublists': reverse('', request=request, format=format),
        # 'itens': reverse('', request=request, format=format),
    })