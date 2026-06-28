import requests

url_point = "http://127.0.0.1:8000/api/"

get_response = requests.post(url_point,json={'id' : '123'})
print(get_response.json())