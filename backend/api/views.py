from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def api_view(request,*args,**kwargs) : 
    data = request.body
    print(data)
    get_data = request.GET # this is using getting url params 
    print(get_data)
    headers = {}
    headers['headers'] = dict(request.headers)
    print(headers)
    print('default',request.headers.get('content_type'))
    return JsonResponse({'name' : 'Aswin'})