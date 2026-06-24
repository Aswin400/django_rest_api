from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from products.models import Product

@csrf_exempt
def api_view(request,*args,**kwargs) : 
    product_data = Product.objects.all().order_by('?').first()
    data = {"query" : "emt"}

    if product_data : 
        data['title'] = product_data.title
        data['content'] = product_data.content
        data['price'] = product_data.price
        print(data)

    else : 
        return JsonResponse(data)
    
    return JsonResponse(data)
