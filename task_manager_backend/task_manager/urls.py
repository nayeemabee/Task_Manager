from django.urls import path, include
from .views import TaskModelViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', TaskModelViewSet)


urlpatterns = [

    path('', include(router.urls))
    
]
