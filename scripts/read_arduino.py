from turtle import update
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import serial

# Use a service account
cred = credentials.Certificate('scripts/olinbuttons-firebase-adminsdk-3uqsp-2cf1964c2c.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'machines').document(u'DUQrTjlWeTT2DAdupQzp')
doc_ref.set({
    u'status': u'waiting',
},merge=True)

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
prev = None
while True:
    try:
        read = int(ser.readline().strip())
    except ValueError:
        continue
    print(f"p: {prev} r:{read}")
    if read != 0 and read != 1:
        print("invalid")
        prev = read
        continue
    if prev == 0 and read == 1:
        print("update")
        doc_ref = db.collection(u'machines').document(u'DUQrTjlWeTT2DAdupQzp')
        if doc_ref.get().to_dict()['status'] == "waiting":
            doc_ref.set({
                u'status': u'open',
            },merge=True)
    prev = read