import requests

endpoints = "http://127.0.0.1:8000/"
get_response = requests.get(endpoints)

post_requests = requests.post(endpoints,json={'message' : 'i am posting request'})

print(post_requests)
print(get_response.text)

