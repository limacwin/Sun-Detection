import subprocess
from urllib import request

def cameraStatus():
    cameraDetected = subprocess.check_output(["vcgencmd", "get_camera"])
    int(cameraDetected.strip()[-1])

    if(cameraDetected):
        logs.write("Camera detected, good to go!\n")
        return True # return success
    else:
        logs.write("Camera not detected.\n")
        return False # return failure, write error to logs

def connectionStatus():
    try:
        request.urlopen('http://google.com') # dummy url, will be switched with a different one later
        logs.write("Connection successful, good to go!\n")
        return True # return success
    except: 
        logs.write("Connection unsucessful.\n")
        return False # return failure, write error to logs, try to reconnect in a while

logs = open("/home/pi/Sun_Detection/logs/logs.txt", 'w')

cameraStatus = cameraStatus()
connectionStatus = connectionStatus()

if(cameraStatus and connectionStatus):
    logs.write("Camera Detected and Connection established. Proceeding to application status checking.\n")
else:
    logs.write("Something feels wrong here. Kindly recheck!\n")

logs.close()