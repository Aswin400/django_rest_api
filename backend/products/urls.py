from django.urls import path
from . import views

urlpatterns = [
    path("<int:pk>/", views.ProductGenerics.as_view()),
    path("all/", views.Product_all_Generics.as_view()),
    path("create/", views.Create_Product_view.as_view()),
    path("all/", views.List_all_view.as_view()),
    path("<int:pk>/update/",views.Productupdateview.as_view()),
    path("<int:pk>/delete/",views.Productdeleteview.as_view()),
    path("own/", views.all_view_page),
    path("own/<int:pk>/", views.all_view_page),
    path("own/create/", views.all_view_page),
]
