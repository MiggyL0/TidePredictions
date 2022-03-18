# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 13:09:44 2022

@author: e4wromal
"""

import requests



payload = {
'product': 'predictions',
'application': 'NOS.COOPS.TAC.WL',
'begin_date': '20220301',
'end_date': '20220331',
'datum': 'MLLW',
'station': '8633532',
'time_zone': 'lst_ldt',
'units': 'english',
'interval': 'hilo',
'format': 'json'
}

r = requests.get('https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?', params=payload)

print(r.text)