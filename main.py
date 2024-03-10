import googlemaps
from datetime import datetime
import math
import requests

gmaps = googlemaps.Client(key='your google api key here') #your google cloud platform api key here


def geocode(position):    
    geocode_result = gmaps.geocode(position)
    position = geocode_result[0]["geometry"]["location"]
    lat = position["lat"]
    lng = position["lng"]
    return lat,lng

def bearing_calc(lat1,lng1,lat2,lng2):
  lat1 = math.radians(lat1)
  lng1 = math.radians(lng1)
  lat2 = math.radians(lat2)
  lng2 = math.radians(lng2)
  
  bearing = math.atan2(
      math.sin(lng2 - lng1) * math.cos(lat2),
      math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(lng2 - lng1)
  )
  bearing = math.degrees(bearing)
  bearing = (bearing + 360) % 360 #it might be negative, this way we make sure it is positive
  
  return bearing

start = "Stazione Pisa centrale, Pisa, Toscana" #starting place here
start_lat,start_lng = geocode(start)

end = "Dipartimento di informatica, Pisa, Toscana" #end location here
end_lat,end_lng = geocode(end)

b = bearing_calc(start_lat,start_lng,end_lat,end_lng)

api_key = "your openweathermap api key here" #your openweathermap api key here
url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(start_lat)+"&lon="+str(start_lng)+"&appid="+str(api_key)+"&units=metric"

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json() #contains all the response nicely formatted in a json
else:
    print(f"Errore nella richiesta: HTTP {response.status_code}")

weather_cond = weather_data["weather"][0]["main"]
wind_spd = weather_data["wind"]["speed"]
wind_dir = weather_data["wind"]["deg"]
if(weather_cond=="Rain" and wind_spd > 2 and (wind_dir-36)%360 <= b <= (wind_dir+36)%360):
    print("Don't use the bike, you risk getting very wet, even with waterproof clothing")
else:
    print("You can ride your bike")

print(f"Weather conditions: {weather_cond}\nWind speed: {wind_spd}\nWind blowing from: {wind_dir}deg")