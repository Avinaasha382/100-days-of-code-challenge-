import requests
import datetime as dt
import os
import dotenv

dotenv.load_dotenv()

USERNAME = "avinaasha"
TOKEN = os.getenv("pixela_token")
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":"graph1",
    "name":"reading novel",
    "unit":"mins",
    "type":"float",
    "color":"ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN
}

add_data_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

curr_date = dt.datetime.now()
curr_formatted_date = curr_date.strftime("%Y%m%d")
print(curr_formatted_date)

data_params = {
    "date":curr_formatted_date,
    "quantity":"100"
}

# response = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{curr_formatted_date}",headers = headers)
# print(response.text)

# response = requests.put(url=f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{curr_formatted_date}",headers = headers,json={"quantity":"65.4"})
# print(response.text)

# response = requests.post(url = graph_endpoint,json = graph_config,headers = headers)
# print(response.text)

response = requests.post(url = add_data_endpoint, json = data_params, headers= headers)
print(response.text)