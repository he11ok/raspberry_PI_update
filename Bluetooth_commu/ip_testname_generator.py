
make_list = []
'''
f = open('adv_testname1.txt','a')
for i in range(10000+1):
    i = 'RPI_' + str(i).zfill(5)
    make_list.append(i)
    f.write(i)
    f.write('\n')
    
f.close
#print(make_list)
'''

f = open('adv_testname_ip.txt','w')
for i in range (int(10 + 1)):
    i = str(i).zfill(12)
    i_list = list(i)
    i_list.insert(3,'.')
    i_list.insert(6+1,'.')
    i_list.insert(9+2,'.')
    i_str = ''.join(i_list)
    f.write(i_str)
    f.write('\n')
    
f.close()