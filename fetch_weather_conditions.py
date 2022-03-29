from multiprocessing import Condition
# config.py contains the rapidapi_host location and the private rapidapi_key values, kindly enter your own values or ask me for mine :)
import config
import requests

# fetching the public ip

public_ip = requests.get('https://api.ipify.org').text

# fetching the localtime data

time_url = "https://weatherapi-com.p.rapidapi.com/timezone.json"

time_querystring = {"q":public_ip}

headers = {
    'x-rapidapi-host': config.rapidapi_host,
    'x-rapidapi-key': config.rapidapi_key
    }

response = requests.request("GET", time_url, headers=headers, params=time_querystring)

response = response.json() # converting fetched 'requests.models.Response' object to a json data object

location_data = response["location"] # fetching the single returned key from the json object

localtime = location_data.get('localtime') # fetching value of 'localtime' from the entire location data
print(f"\nDate and time: {localtime}")

time = localtime[11:] # extracting only the time part from date and time (24hr format)

# fetching the weather forecast data

#region = location_data.get('region')
region = "Panaji"
days = "3"

weather_forecast_querystring = {"q":region,"days":days}

weather_forecast_url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

response = requests.request("GET", weather_forecast_url, headers=headers, params=weather_forecast_querystring)

response = response.json() # converting fetched 'requests.models.Response' object to a json data object

weather_data_current = response["current"]

temperature_c = weather_data_current["temp_c"]
print(f"\nTemperature in Celsius: {temperature_c}")

condition = weather_data_current["condition"]
condition_text = condition["text"]
print(f"Condition: {condition_text}")

wind_kph = weather_data_current["wind_kph"]
print(f"Wind speed in kph: {wind_kph}")

cloud_cover = weather_data_current["cloud"]
print(f"Cloud cover in percentage: {cloud_cover}")

gust_kph = weather_data_current["gust_kph"]
print(f"Gust in kph: {gust_kph}")

humidity = weather_data_current["humidity"]
print(f"Humidity: {humidity}")

precip_mm = weather_data_current["precip_mm"]
print(f"Precipitation in millimeters: {precip_mm}")

# condition for rain (light rain)

if(precip_mm >= 2.5):
    print("Light rain possible.")
    # report to database
else:
    print("No rain, enjoy!")
    # no problem, go ahead
    
