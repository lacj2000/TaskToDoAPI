from rest_framework import serializers
from tasks.models import Task, Sublist, Item

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:         
        model = Task
        fields = ('url','name','description','user','create','check')  



class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('url', 'text','check')


class SublistSerializer(serializers.HyperlinkedModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    class Meta:         
        model = Task
        fields = ('url','title','task', 'items')  


