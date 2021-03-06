from django.db import models
import uuid
from jwtauth.models import Profile
from datetime import datetime
# Create your models here.

class Panic(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    profile = models.ForeignKey(Profile, related_name='panic_normal', on_delete=models.CASCADE)
    cur_lat = models.CharField(max_length=120, blank=True)
    cur_lng = models.CharField(max_length=120, blank=True)
    date = models.DateTimeField(default=datetime.now, null=True, blank=True)

