import requests
from picamera import PiCamera
from time import sleep

#check if camera working properly
try:
    camera = PiCamera()
except:
    print("Camera is not Enabled. Try running 'sudo raspi-config'. ")
    #Update TaskList with the camera error
    try:
        camera = PiCamera()
    except:
        #call Shutdown with Error code
        print("Camera not Working")

camera.start_preview()
sleep(2)
camera.stop_preview()

#check if connected to App
def ConnectedToApp():
    pass

#check if connected to Internet
ping_response = False
try:
    requests.get("https://www.google.com")
    #get latest forecast from weather API
    ping_response = True

except:
    print("Connection Error")
    #check if connected to App
    #else update TaskList


if(not ping_response):
    #check if stored weather data present
    with open("weather_data.json") as data:
        lines = data.readlines()
        print(lines)
    if(stored_weather_data_present):
        #set variables to values fetched
        pass
    else:
        #set variables to default values
        pass

if(weather_forecast_is_not_sunny):
    pass