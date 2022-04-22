import firebase_admin as fba
from firebase_admin import credentials
from firebase_admin import db
import config

cred = credentials.Certificate("service_account_key.json")

fba.initialize_app(cred, {
    'databaseURL': config.database_url
})

# save data
ref = db.reference('data/')
ref.set ({
    'power_generated': {
        'from': '10:00',
        'power': '52W',
        'to': '12:00'
    },
    'rpi_status': {
        'csi': 'active',
        'motor1': 'active',
        'motor2': 'active',
        'motor_driver': 'active',
        'wifi_module': 'active'
    },
    'weather_status': {
        'is_overcast': 'false',
        'is_rainy': 'false',
        'is_snowy': 'false',
        'is_sunny': 'true',
        'is_windy': 'false',
        'is_humid': 'false'
    }
})

rpi_status = ref.child('rpi_status')
rpi_status.update({
    'csi': 'inactive'
})





