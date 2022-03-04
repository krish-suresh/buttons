from time import sleep
from urllib import response
from datetime import datetime as dt
import requests
import csv

# 3rd floor
query = {'school_desc_key': 2, 'location':296972, 'rdm': 1646322013176}
response = requests.get("https://www.laundryview.com/api/currentRoomData", params=query)

# print(f"Washer 1 {response.json()['objects'][1]['time_left_lite']}")
# print(f"Washer 2 {response.json()['objects'][2]['appliance_desc_key']}")
# print(f"Dryer 1 {response.json()['objects'][3]['time_left_lite']}")
# print(f"Dryer 2 {response.json()['objects'][4]['time_left_lite']}")

# define headers of csv 
headers = ["time", "available"]

# write a new line of data every ~26 minutes telling whether washer 2 is available
with open("data.csv","a",newline = '') as f:
    dictwriter = csv.DictWriter(f, fieldnames = headers)
    for _ in range(96): 
        timestamp = dt.now().strftime("%A, %H:%M:%S")
        api_response = response.json()['objects'][2]['time_left_lite']
        new_data = {"time":timestamp,"available": api_response}
        dictwriter.writerow(new_data)
        sleep(1600)

        
    
        
        
    
        

    
