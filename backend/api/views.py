from django.http import JsonResponse,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serilizers import ProductSerializers

@api_view(['POST'])
def apis_view(request,*args,**kwargs) : 
    data = request.data
    return Response(data)

@api_view(["GET"])
def sample_view(request,*args,**kwargs) : 
    Product_data = Product.objects.all().first()
    data = ProductSerializers(Product_data).data
    return Response(data)