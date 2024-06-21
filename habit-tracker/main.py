import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "gerzidorea"
TOKEN = "akjasncieuadhf"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Days",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.put(url=graph_endpoint, json=graph_config, headers=headers)
#print(response)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#print(today.strftime("%Y%m%d"))

# ---> Para mudar a quantidade do dia atual podemos colocar um input em quantity.
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response)

# ---> Final webpage: https://pixe.la/v1/users/gerzidorea/graphs/graph1.html

pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240619"

pixel_update_data = {
    "quantity": "2",
    "optionalData": "20240619",
}

#response = requests.put(url=pixel_update_endpoint, json=pixel_update_data, headers=headers)
#print(response)

pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240619"

#response = requests.delete(url=pixel_delete_endpoint, headers=headers)
#print(response)


