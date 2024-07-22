import requests 
import datetime as dt 
import json
import os 
import dotenv 

dotenv.load_dotenv()

APP_ID = os.getenv("nutri_appid")
API_KEY = os.getenv("nutri_apikey")

exercise_headers = {
    "Content-Type":"application/json",
    "x-app-id":APP_ID,
    "x-app-key":API_KEY
}

sheety_headers = {
    "Content-Type":"application/json",
    "Authorization":os.getenv("sheety_auth")
}



data_params = {
    "query":input("What exercise did you do??")
}


now = dt.datetime.now()
curr_date = now.strftime("%Y-%m-%d")
curr_time = now.strftime("%H:%M:%S")


response= requests.post(url = "https://trackapi.nutritionix.com/v2/natural/exercise",json=data_params,headers=exercise_headers)

data = json.loads(response.text)

exercise_data = data["exercises"]

for exercise in exercise_data:
    sheety_params = {
        "workout":{
            "date":str(curr_date),
            "time":str(curr_time),
            "exercise":exercise["user_input"],
            "duration":f"{exercise["duration_min"]}",
            "calories":f"{exercise["nf_calories"]}"
        }
    }

    response = requests.post(url = "https://api.sheety.co/b3ec3936a2c08bb8fe692a3c5887240f/myWorkoutTracker/workouts",
                            json=sheety_params,headers=sheety_headers)




