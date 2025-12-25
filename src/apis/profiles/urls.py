from django.urls import path

from src.apis.profiles.views import ProfileView

urlpatterns = [
    path('get-profile/', ProfileView.as_view(), name='get-profile'),
]
