from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Profile, Emergency

class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = ('id', 'url', 'first_name', 'last_name', 'phone_number', 'email', 'profile')

class EmergencyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = ('id', 'url', 'first_name', 'last_name', 'phone_number', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    emergency = EmergencyProfileSerializer(many=True)
    class Meta:
        model = Profile
        fields = ('id','url', 'user', 'first_name', 'last_name', 'gender', 'zip_code', 'emergency')

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2"
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        # profile = Profile(user=user)
        # profile.save()
        return user