import os
import requests
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

MY_LAT = 53.3498
MY_LONG = -6.2603
will_rain = False


parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}

request = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
request.raise_for_status()
weather_data = request.json()

for item in weather_data["list"]:
    if item["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+19897621130',
        to='+353833882752',
        body="Bring an umbrella!"
    )
    print(message.status)
