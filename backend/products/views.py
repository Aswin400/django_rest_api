from rest_framework import generics
from .serilizers import ProductSerializers
from .models import Product
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class ProductGenerics(generics.RetrieveAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Product_all_Generics(generics.ListAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

class Create_Product_view(generics.CreateAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):

        print(serializer.validated_data)
        
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None : 
            content = title
        serializer.save(content=content)
        print('object instanse : ',serializer.save())
        #data_title = serializer.data['title']
        #data_content = serializer.data['content']
        data_title = serializer.data.get('title')
        data_content = serializer.data.get('content')
        print(data_title,data_content)

class List_all_view(generics.ListAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

@api_view(['GET','POST'])
def all_view_page(request,pk=None,*args,**kwargs,) : 
    method = request.method

    if method == 'GET' : 
        
        if pk is not None : 
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializers(obj,many=False).data
            return Response(data)
        
        data = Product.objects.all()
        serilizers = ProductSerializers(data,many=True).data
        return Response(serilizers)
    
    if method == 'POST' : 
        body = request.data
        serlizers = ProductSerializers(data=body)
        if serlizers.is_valid(raise_exception=True) : 
            title = serlizers.validated_data.get('title')
            content = serlizers.validated_data.get('content') or None
            print(title,content)

            if content is None : 
                content = title
            
            serlizers.save(content = content)
            print(serlizers.save())
            return Response(serlizers.data)

class Productupdateview(generics.UpdateAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_update(self, serializer)  :
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content')

      if content is None : 
          content = title
          serializer.save(content=content)
          return 
      else : 
          serializer.save()

class Productdeleteview(generics.DestroyAPIView) : 
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
