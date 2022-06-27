import subprocess
from urllib import request
import main as main
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import fetch_weather_conditions as weather

"""
    This File is executed at bootup. At the time of writing this file, the flow is described as follows:
    startup.py => Check n/w, check rpi_stats, upload cached data, etc.
    main.py => will run from sunrise till sunset and call the sun detection every 10mins while updating status of rpi every 2mins
               At init will save values of importance and at destroy will tidy up.
"""

def rpi_stats():
    #Check status of Camera, 
    cameraDetected = subprocess.check_output(["vcgencmd", "get_camera"])
    int(cameraDetected.strip()[-1])

    if(cameraDetected):
        logs.write(f"\n{datetime.datetime.now().time()}: Camera detected\n")
        return True # return success
    else:
        logs.write(f"\n{datetime.datetime.now().time()}: Camera not detected.\n")
        return False # return failure, write error to logs

def connectionStatus():
    try:
        request.urlopen('http://google.com') # dummy url, will be switched with a different one later
        logs.write(f"{datetime.datetime.now().time()}: Connection successful, updating data!\n")
        return True # return success
    except: 
        logs.write(f"{datetime.datetime.now().time()}: Connection unsuccessful, using saved data.\n")
        return False # return failure, write error to logs, try to reconnect in a while

def connectDatabase(cam_status, old_log_exists, logs):
    #get Weather data
    weatherData = weather.getWeatherData()
    print(weatherData)
    
    #Use a service account
    cred = credentials.Certificate("/home/pi/Desktop/V1/monitorrpi-ebdb6-firebase-adminsdk-p6p92-3574ae712a.json")
    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Firebase already Initialized")
    db = firestore.client()
    #Create a Document for the Current Day
    date = str(datetime.date.today())
    print(date)
    print(type(date))
    start_time = str(datetime.datetime.now().time())
    weatherData = weather.getWeatherData()
    
    #update saved weather data file
    weather_log = open(f"weather_data.txt", "w")
    weather_log.write(weatherData)
    weather_log.close()

    #sync values in global scope
    sunrise_time = weatherData[date]["sunrise"]
    sunset_time = weatherData[date]["sunset"]

    log_file = "".join(logs.readlines())
    data_ref = db.collection(u'User').document(u'data')
    data_ref.set({
        (date): {
            u'startup_time': start_time,
            u'shutdown_time': weatherData[date]["sunset"],
            u'pwr': [],
            u'rpi_status': {
                u'csi': cam_status,
                u'motor1': "active",
                u'motor2': "active",
                u'motor_driver': "active",
                u'wifi_module': "active"
            },
            u'weather_data': {
                u'is_humid': weatherData[date]["is_humid"],
                u'is_overcast': weatherData[date]["is_overcast"],
                u'is_rainy': weatherData[date]["is_rainy"],
                u'is_snowy': weatherData[date]["is_snowy"],
                u'is_sunny': weatherData[date]["is_sunny"],
            },
            u'logs and errors': log_file
        }
    })

    if(old_log_exists):
        yesterday = str(datetime.date.today() - datetime.timedelta(days = 1))
        yest = open(f"/home/pi/Sun_Detection/logs/{yesterday}.txt", 'r')
        yest_log_file = "".join(yest.readlines())
        data_ref.set({
            (yesterday): {
                u'logs and errors': yest_log_file
            }
        })
        yest.close()

#Initialize Logs file with current date
current_date = str(datetime.date.today()).split()[0]
logs = open(f"/home/pi/Sun_Detection/logs/{current_date}.txt", 'w')
sunrise_time = 0
sunset_time = 0
#Check if network is connected
connectionStatus = connectionStatus()
if(connectionStatus):
    #connection established check rpi_status, upload cached data
    #check rpi_stats(camera)
    cam_status = rpi_stats()

    old_log_exists = False
    #check if old log file is existing
    try:
        #Upload existing old log file to Database
        yesterday = str(datetime.date.today() - datetime.timedelta(days = 1))
        yest = open(f"/home/pi/Sun_Detection/logs/{yesterday}.txt", 'r')
        logs.write(f"{datetime.datetime.now().time()}: Previous logs Found, syncing with database")
        old_log_exists = True     
        yest.close()     

    except FileNotFoundError:
        logs.write(f"{datetime.datetime.now().time()}: No Previous logs Found!")

    #create document for the day and upload stats
    connectDatabase(cam_status, old_log_exists, logs)

else:
    pass

logs.close()
main.main(sunrise_time, sunset_time, current_date)