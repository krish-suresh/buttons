from time import sleep
from urllib import response
from datetime import datetime as dt
import csv
import pandas as pd
from matplotlib.style import available
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
# 3rd floor


    
cred = credentials.Certificate('scripts/olinbuttons-firebase-adminsdk-3uqsp-2cf1964c2c.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
doc_ref = db.collection(u'machines').document(u'DUQrTjlWeTT2DAdupQzp')
data_database = db.collection(u'logs').stream()

#data_database[0].to_dict()

all_data_dict={}
headers = ["source","data","timestamp","current_machine_status","prev_machine_status"]

with open("laundry_data.csv","a",newline='') as f:
    dictwriter = csv.DictWriter(f, fieldnames = headers)
    for data in data_database:
        next_line = data.to_dict()             
        if "prev_machine_status" not in next_line.keys():
            next_line["prev_machine_status"] = None
        
        # print(next_line["source"])
        new_data = {"source":next_line["source"],"data": next_line["data"], 
                    "timestamp":next_line["timestamp"],
                    "current_machine_status":next_line["current_machine_status"],
                    "prev_machine_status":next_line["prev_machine_status"]}
        # print(new_data)
        dictwriter.writerow(new_data)
        

df = pd.read_csv("laundry_data.csv")
sorted_file = df.sort_values(by=["timestamp"],ascending = False)
sorted_file.to_csv("laundry_data_sorted.csv", index = False)


# with open("laundry_data_sorted","w") as f:
