from django.shortcuts import render

from .models import *
from rest_framework import viewsets
from team.serializers import *
# Create your views here.

# сериаизация заголовка
class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
