import requests as r
import time as t
from datetime import datetime as dt
import json 

url = 'https://api.tfl.gov.uk/BikePoint'

response = r.get(url,timeout=10)

data = response.json()

extract_timestamp = dt.now() 

for bp in data:
    bp['extract_timestamp'] = str(extract_timestamp)

filepath = 'data/' + extract_timestamp.strftime('%Y-%m-%dT%H-%M-%S') + '.json'


with open(filepath,'w') as file:
    json.dump(data,file)