import requests

API = "http://127.0.0.1:5000"

def call_api(method, path, **kwargs):
    try:
        response = requests.request(method, API+path, timeout=15, **kwargs)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException:
        return ConnectionError("Connection error occurred")

data = call_api("GET","/products")

posted_data = {
        'name':"milk",
        "price":43254.435
    }
res = call_api("POST", "/products", json=posted_data)

print(data)
print(res)

deleted = call_api("DELETE", f"/products/1")
print(deleted)

patch = call_api("PATCH", f'/products/2', json={'name':'Burger'})
print(patch)

after = call_api("GET","/products")
print(after)