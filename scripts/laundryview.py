from urllib import response
import requests
query = {'school_desc_key': 2, 'location':296977, 'rdm': 1646060067065}
response = requests.get("https://www.laundryview.com/api/currentRoomData", params=query)

print(f"Washer 1 {response.json()['objects'][2]['time_left_lite']}")
print(f"Washer 2 {response.json()['objects'][3]['time_left_lite']}")
print(f"Dryer 1 {response.json()['objects'][4]['time_left_lite']}")
print(f"Dryer 2 {response.json()['objects'][5]['time_left_lite']}")
