import requests

http_url = "http://127.0.0.1:8000/api/"

get_response = requests.post(http_url,json={'content' : 'not none','price' : '123'})
print(get_response.json())
print(get_response.status_code)