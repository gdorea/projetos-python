import requests
import os
from twilio.rest import Client

api_key = "5791e486f3436f2600f0f91957f9246a"

account_sid = os.environ.get("ACCOUNT_SID_KEY")
auth_token = os.environ.get("AUTH_TOKEN_KEY")

parameters = {
    "lat": -15.595100,
    "lon": -56.092258,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella.",
                        from_='+16508307907',
                        to='+5571999932200'
                    )

    print(message.status)
