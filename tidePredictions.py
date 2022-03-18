import json
from matplotlib import pyplot as plt
from urllib.request import urlopen

# Get data from NOAA
with urlopen("https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?product=predictions&application=NOS.COOPS.TAC.WL&begin_date=20220301&end_date=20220331&datum=MLLW&station=8633532&time_zone=lst_ldt&units=english&interval=hilo&format=json") as response:
    source = response.read()
data = json.loads(source)

for item in data['predictions']:
    tideTime = item['t']
    tideValue = item['v']
    tideType = item['type']
    if tideType == 'H':
        highTide = {tideTime,tideValue}
        print(highTide)

#    for tideType in tideTypes:
#        if tideType == 'H':
#            highTide = {tideTime,tideValue}
#            print(highTide)
