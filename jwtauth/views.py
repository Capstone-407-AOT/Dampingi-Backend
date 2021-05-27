from django.contrib.auth import get_user_model
from rest_framework import permissions, viewsets,  views
from rest_framework import response, decorators, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer, ProfileSerializer, EmergencySerializer
from .models import Profile, Emergency
from rest_framework.exceptions import PermissionDenied


User = get_user_model()

class ProfileView(viewsets.ModelViewSet):
    # queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Profile.objects.filter(user=user)
        raise PermissionDenied()
    def put(self, request, *args, **kwargs):
        user = self.request.user
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        gender = request.data['gender']
        zip_code = request.data['zip_code']
        nik = request.data['nik']
        address = request.data['address']
        
        Profile.objects.filter(id = user.profile.id).update(first_name = first_name,
        last_name = last_name, gender = gender, zip_code = zip_code, nik = nik, address = address)


        return response.Response(status.HTTP_201_CREATED)

class EmergencyView(viewsets.ModelViewSet):
    queryset = Emergency.objects.all()
    serializer_class = EmergencySerializer


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)        
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
    return response.Response(res, status.HTTP_201_CREATED)

