from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from contact.serializers import *
# Create your views here.

# сериаизация заголовка
class QuestionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Quest.objects.all()
    serializer_class = QuestionSerializer
