from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view


from django.contrib.auth.models import User

from tasks.models import Task, Sublist, Item
from tasks.serializers import (
    TaskSerializer, UniqueTaskSerializer, 
    SublistSerializer, SimpleSublistSerializer, ItemSerializer)
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
    serializer_class = UniqueTaskSerializer
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

class SublistList(APIView):
    name='sublist-list'
    permission_classes = [IsAuthenticated] 

    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get_context(self, request):
        return {'request':request}


    def post(self, request, pk, format=None):
        task = self.get_object(pk)
        tasks = TaskSerializer(task, context=self.get_context(request))        
        if task.check_user(request.user):
            serializer = SimpleSublistSerializer(data={**request.data, "task":tasks.data.get('url', None)}, context=self.get_context(request))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)    
        raise AccessFunctionException

class SublistDetail(APIView):
    name='sublist-detail'
    permission_classes = [IsAuthenticated] 

    def get_object(self, pk):
        try:
            return Sublist.objects.get(pk=pk)
        except Sublist.DoesNotExist:
            raise Http404

    def get_context(self, request):
        return {'request':request}


    def get(self, request, pk, format=None):
        sublist = self.get_object(pk)
        if sublist.check_user(request.user):
            serializer = SimpleSublistSerializer(sublist, context=self.get_context(request))
            return Response(serializer.data)
        raise AccessFunctionException
    
    def delete(self, request, pk, format=None):
        sublist = self.get_object(pk)         
        if sublist.check_user(request.user):
            sublist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise AccessFunctionException


class ItemList(APIView):
    name='items-list'
    permission_classes = [IsAuthenticated] 

    def get_object(self, pk):
        try:
            return Sublist.objects.get(pk=pk)
        except Sublist.DoesNotExist:
            raise Http404

    def get_context(self, request):
        return {'request':request}


    def post(self, request, pk, format=None):
        item = self.get_object(pk)
        items = SublistSerializer(item, context=self.get_context(request))        
        if item.check_user(request.user):
            serializer = ItemSerializer(data={**request.data, "sublist":items.data.get('url', None)}, context=self.get_context(request))
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)    
        raise AccessFunctionException

class ItemDetail(APIView):
    name='item-detail'
    permission_classes = [IsAuthenticated] 

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get_context(self, request):
        return {'request':request}


    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        if item.check_user(request.user):
            serializer = ItemSerializer(item, context=self.get_context(request))
            return Response(serializer.data)
        raise AccessFunctionException
    
    def delete(self, request, pk, format=None):
        item = self.get_object(pk)         
        if item.check_user(request.user):
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        raise AccessFunctionException

class ItemCheck(APIView):
    name='item-check'
    permission_classes  =[IsAuthenticated]

    def get_context(self,request):
        return {'request':request}


    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404
    

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        if item.check_user(request.user):
            item.get_check()
            serializer = ItemSerializer(item, context=self.get_context(request))
            return Response(serializer.data,status.HTTP_200_OK)
        raise AccessItemException

class ItemUncheck(ItemCheck):
    name = 'item-uncheck'
    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        if item.check_user(request.user):
            item.get_uncheck()
            serializer = ItemSerializer(item, context=self.get_context(request))
            return Response(serializer.data,status.HTTP_200_OK)
        raise AccessItemException






@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'tasks': reverse('tasks-list', request=request, format=format),
        'users': reverse('users-list', request=request, format=format),
    })