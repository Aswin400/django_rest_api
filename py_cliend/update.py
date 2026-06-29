import requests

url_point = "http://127.0.0.1:8000/api/products/3/update/"
data = {
    'title' : 'None .. title',
    'content' : None
}
get_response = requests.put(url_point,json = data)

print(get_response.json())
print(get_response.status_code)