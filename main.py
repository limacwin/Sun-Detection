# main code to run sequentially
import camera_run as cr
import dual_motors_rotation as dmr
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from random import uniform
import cv2

def checkOffset():
    offsetX, offsetY = cr.CaptureImages(preview=True)
    dmr.unitsConversion(offsetX, offsetY)
    cv2.destroyAllWindows()

def checkRPIStatus():
    pass

def syncPower(current_time, current_date):
    power = round(60 * 1 * (uniform(0.5, 0.75)), 2)
    #Use a service account
    cred = credentials.Certificate("/home/pi/Desktop/V1/monitorrpi-ebdb6-firebase-adminsdk-p6p92-3574ae712a.json")
    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Firebase already Initialized")
    db = firestore.client()
    data_ref = db.collection(u'User').document(u'data')
    old_data = data_ref.get().to_dict()
    power_gen = old_data[current_date]["pwr"]
    power_gen.append(power)
    data_ref.update({
        (current_date): {
                u'pwr': power_gen
            }
    })
    logs = open(f"/home/pi/Sun_Detection/logs/{current_date}.txt", 'a')
    logs.write(f"\n{current_time}: {power}W Power Generated for the last hour")
    log_data = logs.readlines()
    logs.close()

def sayBye(current_date, current_time):
    #Use a service account
    cred = credentials.Certificate("/home/pi/Desktop/V1/monitorrpi-ebdb6-firebase-adminsdk-p6p92-3574ae712a.json")
    try:
        firebase_admin.initialize_app(cred)
    except:
        print("Firebase already Initialized")
    db = firestore.client()
    data_ref = db.collection(u'User').document(u'data')
    
    logs = open(f"/home/pi/Sun_Detection/logs/{current_date}.txt", 'a')
    logs.write(f"\n{current_time}: Successfully Shutting Down")
    log_data = logs.readlines()
    logs.close()
    data_ref.set({
        (current_date): {
                u'logs and errors': log_data
            }
    })

def main(sunrise_time, sunset_time, current_date):
    current_time = datetime.datetime.now().time()
    lastCorrected = sunrise_time

    while(current_time < sunset_time):
        #continuosly check RPI Stats
        checkRPIStatus()
    
        #if its been 15 mins since last offset correction, call checkoffset()
        if(current_time >= lastCorrected):
            #check if offset exists and correct it
            checkOffset()
            current_time = datetime.datetime.now().time()
            lastCorrected = current_time + datetime.timedelta(minutes = 15)
            syncPower(current_date)

        #update current_time    
        current_time = datetime.datetime.now().time()

    sayBye(current_date, current_time)
