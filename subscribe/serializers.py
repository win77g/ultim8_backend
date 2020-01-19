from .models import *
from rest_framework import serializers


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ('id','email')
