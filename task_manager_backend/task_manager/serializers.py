from .models import TaskModel
from rest_framework import serializers


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'