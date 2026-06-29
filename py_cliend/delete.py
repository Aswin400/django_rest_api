import requests

product_id = int(input('WHat is the Product_id ?\n'))

if isinstance(product_id,int) : 
    url_point = f'http://127.0.0.1:8000/api/products/{product_id}/delete/'
    get_response = requests.delete(url_point)
    if get_response.status_code == 204  :
        print(get_response.status_code,get_response.status_code == 204)
    else :
        print('haha')