import requests

url_point = "http://127.0.0.1:8000/api/"

get_response = requests.get(url_point)
post_respone = requests.post(url_point,json={'request' : 'Post'})

print(post_respone.status_code)
print(post_respone.json())
print(get_response.text)
print(get_response.json())