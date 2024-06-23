from django.contrib import admin
from django.urls import path

from .views import (
    UserListCreateAPIView,
    UserRetrieveUpdateDestroyAPIView,
    LoginView,
)

urlpatterns = [
    path("", UserListCreateAPIView.as_view()),
    path("<slug:pk>/", UserRetrieveUpdateDestroyAPIView.as_view()),
    path("login/", LoginView.as_view()),
]
