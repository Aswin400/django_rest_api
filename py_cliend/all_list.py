import requests

url_point  = "http://127.0.0.1:8000/api/products/own/create/"
data = {'title' : 'Perarivalan'}

get_response = requests.post(url_point,json=data)
print(get_response.json())