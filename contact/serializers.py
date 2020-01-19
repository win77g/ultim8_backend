from .models import Quest
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = ('name','email','phone','message','control')
