from django.urls import path
from src.apis.auth.views import CookieTokenObtainPairView, CookieTokenRefreshView

urlpatterns = [
    path("token/", CookieTokenObtainPairView.as_view(), name="token"),
    path("token-refresh/", CookieTokenRefreshView.as_view(), name="token_refresh"),
]