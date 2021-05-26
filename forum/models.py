from __future__ import unicode_literals
import logging

from django.conf import settings
from django.db import models
from django.utils.encoding import force_bytes
from django.utils.translation import ugettext_lazy as _
from jwtauth.models import Profile


# initiate logger
logging.getLogger(__name__)


class Category(models.Model):
    name = models.CharField(_('Name'), max_length=200, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = _('Categories')

    def __str__(self):
        # Use django.utils.encoding.force_bytes() because value returned is unicode
        return self.name

    def __unicode__(self):
        return u'%s' % self.name


class Post(models.Model):
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=200)
    body = models.TextField(_('Body'), )
    reply_to = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title


class Announcement(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    body = models.TextField(_('Body'), )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Profile, related_name='announcers', on_delete=models.CASCADE)
    announce_from = models.DateTimeField(_('Announce from'), null=True, blank=True)
    announce_to = models.DateTimeField(_('Announce to'), null=True, blank=True)
    mark_as_read = models.ManyToManyField(Profile, related_name='announcements')

    class Meta:
        ordering = ['-created_at', ]

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u'%s' % self.title