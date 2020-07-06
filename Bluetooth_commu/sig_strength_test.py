import os
import subprocess
import time
import re
import numpy as np

dist = '1m'
sample_num = 20
RPI_addr = 'DC:A6:32:2A:13:51'
all_RI = []

f = open('test_rssi_'+dist+'.txt','w')
f.write('RSSI test at ' + dist +'\n')

for n in range(sample_num):
    time.sleep(0.1)
    b_rssi = subprocess.check_output('sudo hcitool rssi ' + RPI_addr ,shell = True)
    str_rssi = b_rssi.decode('ascii')
    #if require the sign of the value, add \W
    #rssi = re.findall(r'\d+\.?\d*',str_rssi)
    rssi = re.findall(r'?\W\d+\.?\d*',str_rssi)    
    tp = type(rssi)
    #print(rssi)
    #print(tp)
    all_RI += rssi
    f.writelines(rssi)
    f.writelines('\n')

all_RI = list(map(int,all_RI))
avg_RI = np.mean(all_RI)
lt = str(sample_num)
#print(type(lt))
avg_reminding = 'The average RSSI at '+ dist + ' calculated from ' + lt  + ' samples is :'
f.write(avg_reminding)
f.writelines('\n')
f.write(str(avg_RI))
#f.writelines(avg_RI)
#f.writelines('\n')
f.close()
#print(all_RI)
#print(avg_RI)
#print(type(all_RI))
