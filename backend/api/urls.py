from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_view),
    path('http/',views.httpapi_view),
    path('json/',views.Jsonapi_view)
]