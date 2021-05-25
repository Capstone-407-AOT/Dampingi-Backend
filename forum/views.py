# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import logging

from rest_framework import viewsets
from .models import Category, Post, Announcement
from .serializers import CategorySerializer, PostSerializer, AnnouncementSerializer


# initiate logger
logging.getLogger(__name__)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def pre_save(self, obj):
        obj.created_by = self.request.user

    def get_queryset(self):
        """
        """
        return Post.objects.filter(reply_to__isnull=True)


class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super(AnnouncementViewSet, self).retrieve(request, *args, **kwargs)
        if self.object.mark_as_read.filter(id=request.user.id).count() is 0:
            self.object.mark_as_read.add(request.user)
        return response