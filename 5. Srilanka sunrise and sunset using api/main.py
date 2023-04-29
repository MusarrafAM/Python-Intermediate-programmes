import requests

ULR_for_iss = "http://api.open-notify.org/iss-now.json"
URL_for_sun = "https://api.sunrise-sunset.org/json"
GMT_Sri_lanka = 5.30  # Greenwich Mean Time

def utc_to_local(sunrise):
    sunrise += GMT_Sri_lanka
    if sunrise > 23:
        sunrise -= 24
    return sunrise


house_longitude = "ENTER THE house_longitude HERE"
house_latitude = "ENTER THE house_latitude HERE"
#
# response = requests.get(ULR_for_iss)
# response.raise_for_status()
# data = response.json()
#
# long = data["iss_position"]["longitude"]
# lat = data["iss_position"]["latitude"]
#
# print(long)
# print(lat)


# sunrise and sunset
parameters = {
    "lat": house_latitude,
    "lng": house_longitude,
    "formatted": 0,
}

response = requests.get(URL_for_sun, params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


print(utc_to_local(sunrise))
print(utc_to_local(sunset))







