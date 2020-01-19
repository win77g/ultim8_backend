from .models import Work
from rest_framework import serializers


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('id','name','title','image','slug','description','description_short','top')
