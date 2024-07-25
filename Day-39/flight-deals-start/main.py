#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager



data_manager = DataManager()
email_data = data_manager.get_email()
print(email_data)
# flight_data = data_manager.get_data()

# print("Hi")

# notification_manager = NotificationManager()

# flight_search = FlightSearch()

# for i in range(len(flight_data)):
#     code = flight_search.get_destination_code(flight_data[i]["city"])
#     flight_data[i]["iataCode"] = code 

# print(flight_data)
    
# data_manager.destination_data = flight_data

# flight_price_details = []

# # data_manager.update_flight_data()

# for flight in flight_data:
#     data = flight_search.get_lowest_price(flight["iataCode"])
#     flight_price_details.append(FlightData(data[0],flight["iataCode"],data[1]))

# print(flight_price_details)

# for i in range(len(flight_data)):
#     notification_manager.generate_message(flight_data[i],flight_price_details[i].price,
#                                           flight_price_details[i].departure_date,flight_price_details[i].destination_code)


    



    





