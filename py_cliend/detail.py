import requests

htt_url = "http://127.0.0.1:8000/api/products/7/"
get_response = requests.get(htt_url)

print(get_response.json().get('title'))