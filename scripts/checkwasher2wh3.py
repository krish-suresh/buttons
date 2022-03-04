from time import sleep
from urllib import response
from datetime import datetime as dt
from matplotlib.style import available
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# 3rd floor
query = {'school_desc_key': 2, 'location':296972, 'rdm': 1646322013176}
res_data = requests.get("https://www.laundryview.com/api/currentRoomData", params=query)
cred = credentials.Certificate('scripts/olinbuttons-firebase-adminsdk-3uqsp-2cf1964c2c.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'machines').document(u'DUQrTjlWeTT2DAdupQzp')

# print(f"Washer 1 {res_data.json()['objects'][1]['time_left_lite']}")
# print(f"Washer 2 {res_data.json()['objects'][2]['appliance_desc_key']}")
# print(f"Dryer 1 {res_data.json()['objects'][3]['time_left_lite']}")
# print(f"Dryer 2 {res_data.json()['objects'][4]['time_left_lite']}")

# define headers of csv 
headers = ["time", "available"]
prev = {"time":None,"available": res_data.json()['objects'][2]['time_left_lite']}
while True: 
    res_data = requests.get("https://www.laundryview.com/api/currentRoomData", params=query)
    timestamp = dt.now().strftime("%A, %H:%M:%S")
    api_response = res_data.json()['objects'][2]['time_left_lite']
    new_data = {"time":timestamp,"available": api_response}
    if prev["available"] == 'Available' and new_data["available"] != 'Available':
        print(new_data)
        doc_ref.set({
            u'status': u'busy',
        },merge=True)
    elif prev["available"] != 'Available' and new_data["available"] == 'Available':
        print(new_data)
        doc_ref.set({
            u'status': u'waiting',
        },merge=True)
    prev = new_data
    sleep(30)