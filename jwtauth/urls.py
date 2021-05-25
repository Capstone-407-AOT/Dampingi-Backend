from django.urls import path
from .views import registration, UserProfileView

urlpatterns = [
    path('register/', registration, name='register'),
    path('user/profile/', UserProfileView, name='user_profile')
]