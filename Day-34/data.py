import requests

params = {
    "amount":10,
    "type":"boolean"
}

print(type(params))

response = requests.get(url = "https://opentdb.com/api.php",params = params)

question_data = response.json()["results"]

# print(question_data)