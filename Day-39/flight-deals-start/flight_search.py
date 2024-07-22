import os 
import dotenv 
import requests 
import datetime as dt

TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
ORIGIN_CODE = "LHR"

now = dt.datetime.now()
six_months_after = now + dt.timedelta(days = 6*30)
curr_date = now.strftime("%Y-%m-%d")
six_months_after_date = six_months_after.strftime("%Y-%m-%d")

dotenv.load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self._api_key = os.getenv("amadeus_apikey")
        self._api_secret = os.getenv("amadeus_secret")
        self._token = self._get_new_token()


    def get_destination_code(self,city_name):
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

        
    
    def _get_new_token(self):
        

        header = {
            "Content-Type":"application/x-www-form-urlencoded"
        }
        data_params = {
            "grant_type":"client_credentials",
            "client_id":self._api_key,
            "client_secret":self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT,headers=header,data=data_params)
        return response.json()["access_token"]
    
    def get_lowest_price(self,destination_code):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode":ORIGIN_CODE,
            "destinationLocationCode":destination_code,
            "departureDate":curr_date,
            "returnDate":six_months_after_date,
            "adults":1
        }
        response = requests.get(url=FLIGHT_ENDPOINT,headers=headers,params=query)
        data = response.json()
        try:
            return(float(data["data"][0]["price"]["total"]),data["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0])
        except:
            return (None,None)
    
    
        
        