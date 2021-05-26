from django.db import models
import uuid
from jwtauth.models import Profile
from forum.models import Category

# Create your models here.
class Report(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    profile = models.ForeignKey(Profile, related_name='reports', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='reports', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=False)
    date = models.DateTimeField(null=True, blank=True)
    lat = models.CharField(max_length=120, blank=False)
    lng = models.CharField(max_length=120, blank=False)

    def __str__(self):
        return "Emergency Contact" + self.title