from django.shortcuts import render
from .models import TaskModel
from .serializers import TaskModelSerializer
from rest_framework import viewsets


# Create your views here.

class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelSerializer
