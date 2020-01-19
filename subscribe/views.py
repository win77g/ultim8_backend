from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from subscribe.serializers import *
# Create your views here.

# сериаизация заголовка
class SubscribeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
