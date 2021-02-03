from rest_framework import serializers
from tasks.models import Task, Sublist, Item

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:         
        model = Task
        fields = ('url','name','description','user','create','check')  
