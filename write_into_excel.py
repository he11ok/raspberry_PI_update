'''
Author: Limu Han
Function: write all the test data into an Excel
All the data in the folder should be have a name like test_rssi_1.5m
'''

import os
import openpyxl
import numpy as np
import pandas as pd
import re
import linecache
import subprocess

# The address of the data folder
# filePath = "/Users/limu/Desktop/ClientDatas_0.1nocase/"
# filePath = "/Users/limu/OneDrive/RPI_blt_RSSI_data/MasterDatas_0.1/"
filePath = "/Users/limu/OneDrive/RPI_blt_RSSI_data/ClientDatas_0.1nocase/"
DS_storefilePath = filePath + ".DS_store"
filenames_in_folder = os.listdir(filePath)
# print(filenames_in_folder)
filenum_in_folder = len(filenames_in_folder)
# print(filenum_in_folder)

content = []
# added the following line for MacOS to delete the hiden .DS_store file
subprocess.call('sudo -S find '+ filePath +  ' -name ".DS_Store" -depth -exec rm {} \;',shell=True)
f = open(filePath + filenames_in_folder[1])
for line in f:
    content.append(line)

col = len(content)

table_content = np.zeros((filenum_in_folder,col),dtype=np.str)
table_content_list = [[0 for i in range(col)] for i in range(filenum_in_folder)]
# print(table_content)
# print(table_content_list)

index_in_form = []
for order,i in enumerate(filenames_in_folder):
    index_lt = re.findall(r'\d+\.\d|\d+',i)
    index_str = index_lt.pop()

    # index = list(filter(str.isdigit,index_str))
    # string = ''
    # index = string.join(index)
    # index_in_form.append(index)

    index_in_form.append(index_str)
    index_in_form = list(map(float,index_in_form))
    # index_in_form is [4.0, 8.0, 1.5, 9.0, 3.5, 5.0, 7.5, 1.0, 2.0, 3.0, 0.0, 5.5, 9.5, 0.5, 0.0, 1.0, 2.5, 6.0, 0.5, 6.5, 4.5, 8.5, 7.0]


# creat a dir about the order and the distance after sorting
# sort the distance
index_in_form.sort(key=None, reverse=False)

# creat index_dir
index_dir = {}
for order,i in enumerate(index_in_form):
    index_dir[i] = order


for order, i in enumerate(filenames_in_folder):
    f = open(filePath + i,'r')
    # f_new = linecache.getline(filePath + i, (1,)).strip()
    # RE to get the distance in the name string
    dist = re.findall(r'\d+\.\d|\d+', i)
    dist = list(map(float,dist)).pop()

    for line_order,line in enumerate(f):
        # value = re.findall(r'\W?\d+\.?\d*',line)
        # find the sorted order about the distance to make sure the data be written in right row
        # table_content[index_dir[dist]][line_order] = str(line)
        line = re.findall(r'\d+\.?\d|\d+', line) # fatch the number from the string
        table_content_list[index_dir[dist]][line_order] = line[0]
        # why here the table can only save one number ?? Because if the type of the array in numpy is str it only able to
        # store one characters, maybe creat a list to solve this !!

# table_content = table_content[:,:(col-2)] # delete the last two colomns
# table_content = table_content[:,1:] # delete the first colomns
# print(table_content)
for _list in table_content_list:
    #print(list)
    _list.pop() # delete the last one col
    _list.pop() # delete the last one col
    _list.pop(0) # delect the first col

print(table_content_list)

table_content_ar = np.array(table_content_list)
print(table_content_ar)
# data = pd.DataFrame(table_content)
data = pd.DataFrame(table_content_ar).T

writer = pd.ExcelWriter('Data.xlsx')
data.to_excel(writer, 'page_1')
writer.save()
writer.close()

