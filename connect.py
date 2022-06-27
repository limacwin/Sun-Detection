import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from gpiozero import CPUTemperature
from random import uniform
import datetime

#Use a service account
cred = credentials.Certificate("monitorrpi-ebdb6-firebase-adminsdk-p6p92-3574ae712a.json")
#default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':''})
#cred = credentials.ApplicationDefault()
try:
    firebase_admin.initialize_app(cred)
except:
    print("Firebase already Initialized")

print("OK")

db = firestore.client()

#Read Data
ref = db.collection(u'main_data')
docs = ref.stream()
for doc in docs:
    print(f"{doc.id} => {doc.to_dict()}")
  
#Get CPU Temperature
cpu = CPUTemperature()
temp = cpu.temperature
  
#Write Data
doc_ref = db.collection(u'main_data').document(u'status')
"""
doc_ref.set({
    u'name': u'Raspberry Pi',
    u'temperature': temp,
    u'pwr': [12]
})
"""
power = round(60 * 1 * (uniform(0.5, 0.75)), 2)
power_gen = doc_ref.get().to_dict()

dat = power_gen['pwr']
dat.append(power)
print(power_gen)
print(dat)

doc_ref.update({u'pwr': dat})
