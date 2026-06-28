from rest_framework import generics
from .serilizers import ProductSerializers
from .models import Product

class ProductGenerics(generics.RetrieveAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_all_Generics(generics.ListAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
