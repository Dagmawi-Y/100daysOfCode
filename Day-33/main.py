import requests
import datetime as dt

MY_LAT = 48.937470
MY_LON = 2.461450

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# lat = data["iss_position"]["latitude"]
# lon = data["iss_position"]["longitude"]

parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = dt.datetime.now()
# print(time_now)
