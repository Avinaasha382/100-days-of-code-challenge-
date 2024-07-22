from twilio.rest import Client 
import os 
import dotenv 

dotenv.load_dotenv()

account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
client = Client(account_sid, auth_token)

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def generate_message(self,sheet_data,curr_lowest_price,date,destination_code):
        if curr_lowest_price == None or date == None:
            print("Flights are currently not available")
            return 
        
        if(sheet_data["lowestPrice"] >= int(curr_lowest_price)):
            message = client.messages.create(
            from_='+14842977148',  # Replace with your Twilio phone number
            to='+917200289315',  # Replace with recipient number,
            body = f"Low Price alert! Only {curr_lowest_price} to fly from LHR to {destination_code} from {date}")
            print(message.sid)
        else:
            print(sheet_data["city"],sheet_data["lowestPrice"],curr_lowest_price)
            print("A Cheaper Flight Option is not available")








