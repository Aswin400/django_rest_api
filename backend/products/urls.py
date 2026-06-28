from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/',views.ProductGenerics.as_view()),
    path('all/',views.Product_all_Generics.as_view())
]