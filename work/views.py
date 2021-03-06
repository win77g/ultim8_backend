from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from work.serializers import *
# Create your views here.

# сериаизация заголовка
class WorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
