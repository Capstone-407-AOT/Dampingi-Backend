from django.shortcuts import render
from rest_framework import permissions, viewsets,  views, status
from rest_framework.response import Response
from .serializers import PanicSerializer
from .models import Panic
from jwtauth.models import Emergency
from django.conf import settings
from twilio.rest import Client
from django.core.mail import send_mail

class PanicView(viewsets.ModelViewSet):
    # queryset = Panic.objects.all()
    serializer_class = PanicSerializer

    def create(self,request, *args, **kwargs):
        user = self.request.user
        emergency = Emergency.objects.filter(profile = user.profile.id)
        
        panic_save = Panic(profile = user.profile,cur_lat=request.data['cur_lat'], cur_lng=request.data['cur_lng'])
        panic_save.save()
        subject = '{fn_user} {ln_user} Mungkin Butuh Bantuanmu !!!'.format(fn_user=user.profile.first_name, ln_user=user.profile.last_name)
        for ec in emergency:
            recepient = ec.email
            message = 'Halo {fn_emergency} kami dari Dampingi ingin memberitahu bahwa anda adalah Emergency Contact dari {fn_user} dan beliau telah menekan tombol "Panic". Tolong hubungi {fn_user} mungkin saja dia butuh bantuanmu!! /n Untuk info lebih lanjut bisa hubungi dampingibe@gmail.com'.format(fn_emergency=ec.first_name, fn_user=user.profile.first_name)
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient])

        #Twilio Send SMS
        # message_to_broadcast = ("Server Test "
        #                                         "yet? Grab it here: https://www.twilio.com/quest")
        # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        # client.messages.create(to="+6287884357149",
        #                            from_="+14437207598",
        #                            body=message_to_broadcast)

        #SMTP Send Mail
        
        return Response("Pesan Berhasil Dikirim")