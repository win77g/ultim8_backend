from django.shortcuts import render

from .models import *
from rest_framework import viewsets,permissions
from blog.serializers import *

# Create your views here.
def index(request):
    return render(request, 'index.html')
# сериаизация заголовка
class ArticleBlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = ArticleBlog.objects.all()
    serializer_class = ArticleBlogSerializer
    filter_fields = ('sidebar',)

# class ArticleBlogBySidebarViewSet(viewsets.ModelViewSet):
class CommentsBlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # permission_classes = [permissions.AllowAny, ]
    queryset = Comments.objects.all()
    # queryset = ArticleBlog.objects.filter(sidebar='ok')
    serializer_class = CommentsSerializer
    filter_fields = ('article',)
#
