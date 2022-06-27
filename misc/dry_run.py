import connect
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import strftime

#Create a User with Input name(Email) and Password


#Create a Collection with the User's Email
#Use a service account
cred = credentials.Certificate("/home/pi/Desktop/monitorrpi-ebdb6-firebase-adminsdk-p6p92-3574ae712a.json")

db = firestore.client()
"""
email = input("Enter Name(Email) of User: ")
password = input("Enter Password: ")
auth_ref = db.collection(u'User').document(u'auth')

auth_ref.set({
    u'email': email,
    u'pass': password
})
"""
#Creating (if not exits) documents info and dayX
info_ref = db.collection(u'User').document(u'info')

info_ref.set({
    u'location': "Panaji",
    u'Remarks': "Set up successfully"
})

#Create a Document for the Current Day
day = strftime("%d")
month = strftime("%m")
year = strftime("%y")

print(f"day/month/year: {day}/{month}/{year}")

stamp = str(day + "/" + month + "/" + year)
print(stamp)


data_ref = db.collection(u'User').document(u'data')

data_ref.set({
    (stamp): {
        u'startup_time': 8,
        u'shutdown_time': 6,
        u'pwr': [12.3],
        u'rpi_status': {},
        u'weather_data': {}
    }
})
