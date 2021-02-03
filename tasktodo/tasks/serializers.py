from rest_framework import serializers
from tasks.models import Task, Sublist, Item
from users.serializers import *


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'text','check')

class SimpleSublistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sublist
        fields = ('url','title', 'task')



class SublistSerializer(serializers.HyperlinkedModelSerializer):
    items_list = ItemSerializer(many=True, read_only=True)
    #items_list = serializers.HyperlinkedIdentityField(view_name='items', read_only=True )
    class Meta:
        model = Sublist
        fields = ('url', 'title', 'items_list')


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Task
        fields = ('url','name', 'description', 'create','user', 'check')


class UniqueTaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    sublists = SublistSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = ('url','name', 'description', 'create', 'check', 'sublists','user')
