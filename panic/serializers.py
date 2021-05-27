from rest_framework import serializers
from .models import Panic

class PanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panic
        fields = ('id', 'profile',  'cur_lat', 'cur_lng', 'date')