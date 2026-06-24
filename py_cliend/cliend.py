import requests

url_point = "http://127.0.0.1:8000/api/"

get_response = requests.get(url_point)

print(get_response.text)