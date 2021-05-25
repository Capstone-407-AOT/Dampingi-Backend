from django.db import models
import uuid
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save, post_delete

# Create your models here.
class Profile(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    zip_code = models.CharField(max_length=5, validators=[MinLengthValidator(5)], blank=False)

    def __unicode__(self):
        return u'Profile of user: {0}'.format(self.user.email)
    
    def __str__(self):
        return self.user.username

class Emergency(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    first_name = models.CharField(max_length=120, blank=False)
    last_name = models.CharField(max_length=120, blank=False)
    phone_number = models.CharField(max_length=120, blank=False)
    email = models.CharField(max_length=120, blank=False)
    profile = models.ForeignKey(Profile, related_name='emergency', on_delete=models.CASCADE)

    def __str__(self):
        return "Emergency Contact" + self.first_name


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(create_profile, sender=User)


def delete_user(sender, instance=None, **kwargs):
    try:
        instance.user
    except User.DoesNotExist:
        pass
    else:
        instance.user.delete()
post_delete.connect(delete_user, sender=Profile)