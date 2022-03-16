import json


import json
from urllib.request import urlopen

with urlopen("https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=20220301&end_date=20220331&datum=MLLW&station=8633532&time_zone=lst_ldt&units=english&interval=hilo&format=json") as response:
    source = response.read()

data = json.loads(source)

# print(json.dumps(data, indent=2))

high_tides = dict()

for item in data['predictions']:
    tideTime = item['t']
    tideValue = item['v']
    tideType = item['type']
    # while (tideType == 'H'):
    #     print(tideTime, tideValue)
