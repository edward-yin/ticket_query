#-*- coding:utf-8 -*-
import re
import codecs
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

f =codecs.open('12306-0703.json','r')
#with codecs.open(12306-0703.json,'r','GBK') as f:
    
f_read = f.read()#.decode('utf-8')
#print f_read
pattern = re.compile(r'\[(.+?)\]')
result = str(re.findall(pattern,f_read))
#print result
print ('the result')
r_result = str(result.replace('"','\n'))
#print str(r_result)
r = r_result.split('\n')
pat_tnum = re.compile(r'\|(T\d+|Z\d+|K\d+)\|')
tnum1 = str(re.findall(pat_tnum,r[1]))
tnum2 = str(re.findall(pat_tnum,r[3]))
tnum3 = str(re.findall(pat_tnum,r[5]))
tnum4 = str(re.findall(pat_tnum,r[7]))
pat_date = re.compile(r'\|(2\d{7})\|')
date = str(re.findall(pat_date,r[1]))
print date
print tnum1+'\n'+tnum2+'\n'+tnum3+'\n'+tnum4
#pat_state = re.compile(r'(?<=\d\|\|)(\d{0,2}|\\.+)(?=\|\d+|\\)')
pat_state = re.compile(r'\|\|\|\|(.+?)\|\|\|\|\|')
state1 = str(re.findall(pat_state,r[1])).split('|')
state2 = str(re.findall(pat_state,r[3])).split('|')
state3 = str(re.findall(pat_state,r[5])).split('|')
state4 = str(re.findall(pat_state,r[7])).split('|')
print state1[5]
print state2[5]
print state3[5]
print state4[5]
