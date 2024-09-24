import pandas as pd
import numpy as np
import json
data_read = open('wuhansubway.json','r',encoding='utf-8')
data=json.load(data_read)

result={'name':[],
        'line':[],
        'line_':[],
        'color':[],
        'longitude':[],
        'latitude':[],
        'poiid':[],
        'is_transfer_station':[]}
for line in range(len(data['l'])):
    for point in range (len(data['l'][line]['st'])):
        result['name'].append(data['l'][line]['st'][point]['n'])
        result['line'].append(data['l'][line]['kn']+data['l'][line]['la'])
        result['line_'].append(data['l'][line]['kn'])
        result['color'].append(data['l'][line]['cl'])
        lon_lat=data['l'][line]['st'][point]['sl'].split(',')
        result['longitude'].append(lon_lat[0])
        result['latitude'].append(lon_lat[1])
        result['poiid'].append(data['l'][line]['st'][point]['poiid'])
        result['is_transfer_station'].append(data['l'][line]['st'][point]['t'])
pd.DataFrame(result).to_csv('wuhansubway.csv',encoding='gbk',index=False)
print(data['s'], '总共有{}条线路；总共有{}个地铁站！'.format(len(data['l']),len(set(result['poiid']))))