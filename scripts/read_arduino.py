import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import serial

# Use a service account
cred = credentials.Certificate('scripts/buttons-9f1e7-firebase-adminsdk-acyce-f5cedc1ac4.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
prev = None
while True:
    if ser.readline().strip() != "0" or ser.readline().strip() != "1":
        continue
    if prev == "0" and ser.readline().strip() == "1":
        doc_ref = db.collection(u'machines').document(u'mJJ2Rw4XrQzDDwYHKaYZ')
        doc_ref.set({
            u'status': u'open',
        },merge=True)
    prev = ser.readline().strip()