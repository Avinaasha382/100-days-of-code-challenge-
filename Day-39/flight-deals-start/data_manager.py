import requests 
import os 
import dotenv

dotenv.load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/b3ec3936a2c08bb8fe692a3c5887240f/flightDealsFinder/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.authorization = os.getenv("sheety_auth")
        self.headers = {
            "Authorization":self.authorization
        }
        self.destination_data = {}
    
    def get_data(self):
        response = requests.get(url=SHEETY_ENDPOINT,headers=self.headers)
        response.raise_for_status()
        self.destination_data = response.json()["prices"]
        return self.destination_data
    
    def update_flight_data(self):
        for data in self.destination_data:
            data_params = {
                "price":{
                    "iataCode":data["iataCode"]
                }
            }
            requests.put(url=f"{SHEETY_ENDPOINT}/{data['id']}",json=data_params,headers=self.headers)