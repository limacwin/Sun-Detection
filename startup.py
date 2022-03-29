import subprocess
from urllib import request
import main as main
import time

def cameraStatus():
    cameraDetected = subprocess.check_output(["vcgencmd", "get_camera"])
    int(cameraDetected.strip()[-1])

    if(cameraDetected):
        logs.write(f"At time: {time.time()}: Camera detected, good to go!\n")
        return True # return success
    else:
        logs.write(f"At time: {time.time()}: Camera not detected.\n")
        return False # return failure, write error to logs

def connectionStatus():
    try:
        request.urlopen('http://google.com') # dummy url, will be switched with a different one later
        logs.write(f"At time: {time.time()}: Connection successful, good to go!\n")
        return True # return success
    except: 
        logs.write(f"At time: {time.time()}: Connection unsucessful.\n")
        return False # return failure, write error to logs, try to reconnect in a while

logs = open("/home/pi/Sun_Detection/logs/logs.txt", 'a')

cameraStatus = cameraStatus()
connectionStatus = connectionStatus()

if(cameraStatus or connectionStatus):
    logs.write(f"At time: {time.time()}: Camera Detected or Connection established. Proceeding to application status checking.\n")
    # call to firebase database connection checker 
    main.main()
else:
    logs.write(f"At time: {time.time()}: Something feels wrong here. Kindly recheck!\n")
    # abort and/or wait for connection to get established

logs.close()