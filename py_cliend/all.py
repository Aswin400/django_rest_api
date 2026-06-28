import requests

htt_url = "http://127.0.0.1:8000/api/products/all/"
get_response = requests.get(htt_url)

print(get_response.json())