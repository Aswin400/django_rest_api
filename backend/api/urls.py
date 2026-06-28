from django.urls import path
from . import views

urlpatterns = [
    path('', views.apis_view),
    path('sample/',views.sample_view)]