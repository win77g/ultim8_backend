from .models import ArticleBlog,Comments
from rest_framework import serializers


class ArticleBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleBlog
        fields = ('id','name','image','slug','description','description_short','author','date','sidebar','commentari')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','description','name','date','article','email')
