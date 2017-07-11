#-*- coding:utf-8 -*-
import re
import codecs
import collections
from prettytable import PrettyTable

#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

f =codecs.open('d_12306.json','r')
#with codecs.open(12306-0703.json,'r','GBK') as f:

f_read = f.read().replace('\xe6\x97\xa0','soldout').replace('\xe6\x9c\x89','available')#.decode('utf-8')
#print f_read
pattern = re.compile(r'\[(.+?)\]')
result = str(re.findall(pattern,f_read))
#print result
print ('the result')
pattern = re.compile(r'"(.+?)"')
#state of every train
s_result = re.findall(pattern,result)
'''
print s_result
pattern = re.compile(r'\|(.+?)\|')
ss_result = re.findall(pattern,str(s_result[0]))
'''

'''
print s_result[0]

print len(ss_result)

for i in range(len(ss_result)):
    print i
    print ss_result[i]
'''
x = PrettyTable(["trainnumber","start_time","arrive_time","last","YW","second_class","RW","DW","YZ"])
x.align["trainnumber"] = '1'
x.padding_width = 1


dict_head = ['number','s_time','a_time','last','YW','s_class','RW','DW','YZ']
refer_num = [3,8,9,10,28,30,23,22,29]
train = collections.OrderedDict()


for i in range(len(s_result)):
    ss_result = str(s_result[i]).split('|')
    for key in range(len(dict_head)):
        if ss_result[refer_num[key]]:
            train[dict_head[key]] = ss_result[refer_num[key]]
        else :
            train[dict_head[key]] = '--'
    #print train
    #x.add_row([train.values()])       
    x.add_row([train['number'],train['s_time'],train['a_time'],train['last'],train['YW'],train['s_class'],train['RW'],train['DW'],train['YZ']])    


print x

