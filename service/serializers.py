from .models import ServiceMeinTitle,Service,ServiceImg,ServiceSecond
from rest_framework import serializers


class ServiceMeinTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceMeinTitle
        fields = ('id','firsttitle','secondtitle')

# создание юзера
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','title','description','icon')

class ServiceSecondSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceSecond
        fields = ('id','title','description','icon')



class ServiceImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImg
        fields = ('id','img',)
