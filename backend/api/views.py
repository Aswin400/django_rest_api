from django.http import JsonResponse,HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from products.models import Product
from django.forms.models import model_to_dict

@csrf_exempt
def api_view(request,*args,**kwargs) : 
    product_data = Product.objects.all().order_by('?').first() # This method only convert the single elements

    data = {}
    print(f'headers : {request.headers}')

    if product_data : 
        data = model_to_dict(product_data)
        print(data)
    
    meta_data = request.META
    print(meta_data)

    return JsonResponse({'Products' : data,'headers' : dict(request.headers),'User' : request.META['USER']})

def httpapi_view(request,*args,**kwargs) : 
    lists = ['balaji','aswin','bhuvan',1]
    data = {'number' : 1,'str' : 'str'}
    return HttpResponse(str({'hi' : lists,'python objects' : data}))

def Jsonapi_view(request,*args,**kwargs) : 
    return JsonResponse({'message' : 'hi i am json '})