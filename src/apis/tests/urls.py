from django.urls import path

from src.apis.tests.views import TestView

urlpatterns = [
    path('get-test/', TestView.as_view(), name='get-test'),
]
