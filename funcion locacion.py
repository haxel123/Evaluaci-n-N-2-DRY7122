import requests
import urllib.parse

route_url = "https://graphhopper.com/api/1/route?"
loc1 = "Washington, D.C."
loc2 = "Baltimore, Maryland"
key = "8bc67068-d89a-4e21-ab2c-3abc59f3050b"

def geocoding (location, key):
    geocode_url = "https://graphhopper.com/api/1/geocode?"
    url = geocode_url + urllib.parse.urlencode({"q":location, "limit":"1", "key":key})
    
    replydata = requests.get(url)
    json_data = replydata.json()
    json_status = replydata.status_code
    print("Geocoding API URL for " + location + ":\n" + url)
    if json_status == 200:
        json_data = requests.get(url).json()
        lat=(json_data["hits"][0]["point"]["lat"])
        lng=(json_data["hits"][0]["point"]["lng"])
    else:
        lat="null"
        lng="null"
    return json_status, lat, lng

replydata = requests.get(url)
json_data = replydata.json()
json_status = replydata.status_code

json_status = replydata.status_code

if json_status == 200:
    print("Geocoding API URL  for " + loc1 + ":\n" + url)
    
orig = geocoding(loc1,
key) print(orig)
dest = geocoding(loc2,
key) print(dest)














'''
name = json_data["hits"][0]["name"]
value = json_data["hits"][0]["osm_value"]
if "country" in json_data["hits"][0]:
country = json_data["hits"][0]
["country"]
else:
country=""
if "state" in json_data["hits"][0]:
state = json_data["hits"][0]
["state"]
else:
state=""
if len(state) !=0 and len(country) !=0:
new_loc = name + ", " + state + ", " + country
elif len(state) !=0:
new_loc = name + ", " + country
else:
new_loc = name
print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n"
+ url)
else:
lat="null"
lng="null"
new_loc=location
return json_status,lat,lng,new_loc
'''








'''
while True:
loc1 = input("Starting Location:
") orig = geocoding(loc1, key)
print(orig)
loc2 = input("Destination:
") dest = geocoding(loc2,
key) print(dest)
'''

'''
while True:
loc1 = input("Starting Location:
") if loc1 == "quit" or loc1 ==
"q":
break
orig = geocoding(loc1,
key) print(orig)
loc2 = input("Destination: ")
if loc2 == "quit" or loc2 == "q":
break
dest = geocoding(loc2,
key) print(dest)
'''



'''
def geocoding (location,
key): while location ==
"":
location = input("Enter the location again: ")
geocode_url =
"https://graphhopper.com/api/1/geocode?"
url = geocode_url + urllib.parse.urlencode({"q":location, "limit":
"1", "key":key})
''''

'''
print("Geocoding API URL for " + new_loc + " (Location Type: " + value + ")\n"
+ url)
else:
lat="null"
lng="null"
new_loc=location
print("Geocode API status: " + str(json_status) + "\nError message: "
+ json_data["message"])
return json_status,lat,lng,new_loc
while True:
loc1 = input("Starting Location: ")

'''
