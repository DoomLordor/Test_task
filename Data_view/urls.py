from django.urls import path

from . import views

urlpatterns = [
    path('', views.DataView.as_view()),
]