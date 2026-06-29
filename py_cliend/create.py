import requests

htt_url = "http://127.0.0.1:8000/api/products/create/"

data = {'title' : 'rohith views','price':99}

get_response = requests.post(htt_url,json=data)

print(get_response.json())