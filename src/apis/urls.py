from django.urls import path, include

urlpatterns = [
    path("auth/", include("src.apis.auth.urls")),
    path("profile/", include("src.apis.profiles.urls")),
]
