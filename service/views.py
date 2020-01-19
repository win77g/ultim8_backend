from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from service.serializers import *
# Create your views here.

# сериаизация заголовка
class ServiceMeinTitleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = ServiceMeinTitle.objects.all()
    serializer_class = ServiceMeinTitleSerializer

# сериаизация главного сервисов
class ServiceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

# сериаизация главного сервисов
class ServiceSecondViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = ServiceSecond.objects.all()
    serializer_class = ServiceSecondSerializer

class ServiceImgViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = ServiceImg.objects.all()
    serializer_class = ServiceImgSerializer
