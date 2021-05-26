from rest_framework import serializers
from .models import Report

class ReportSerializer(serializers.ModelSerializer):
    class meta:
        model = Report
        fields = ('id', 'url', 'profile', 'category', 'title', 'description', 'date', 'lat', 'lng')