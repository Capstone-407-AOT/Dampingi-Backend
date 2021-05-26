from django.shortcuts import render
from rest_framework import permissions, viewsets,  views
from .serializers import ReportSerializer
from .models import Report

# Create your views here.

class ReportView(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer