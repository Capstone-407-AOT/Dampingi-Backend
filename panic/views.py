from django.shortcuts import render
from rest_framework import permissions, viewsets,  views, status
from rest_framework.response import Response
from .serializers import PanicSerializer
from .models import Panic
from django.conf import settings
from twilio.rest import Client
from django.core.mail import send_mail

class PanicView(viewsets.ModelViewSet):
    # queryset = Panic.objects.all()
    serializer_class = PanicSerializer

    def get_queryset(self):
        user = self.request.user
       
        #Twilio Send SMS
        message_to_broadcast = ("Server Test "
                                                "yet? Grab it here: https://www.twilio.com/quest")
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        client.messages.create(to="+6287884357149",
                                   from_="+14437207598",
                                   body=message_to_broadcast)

        #SMTP Send Mail
        subject = 'Test Server'
        message = 'Dampingi Backend Test Serve : Tolong hubungi sayaa'
        recepient = 'sbhirama@gmail.com'
        send_mail(subject, 
            message, settings.EMAIL_HOST_USER, [recepient])
        return Panic.objects.filter(profile=user.profile)