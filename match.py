#-*- coding:utf-8 -*-
import re
import codecs
#import sys
#reload(sys)
#sys.setdefaultencoding("utf-8")

f =codecs.open('d_12306.txt','r')


f_read = f.read()#.decode('utf-8')
#print f_read
pattern = re.compile(r'\[(.+?)\]')
result = str(re.findall(pattern,f_read))
#print result
print ('the result')
r_result = str(result.replace('"','\n').replace('\\xe6\\x97\\xa0','soldout').replace('\\xe6\\x9c\\x89','available'))
#print r_result
r = r_result.split('\n')
#print r


pat_tnum = re.compile(r'\|(T\d+|Z\d+|K\d+)\|')
tnum1 = re.findall(pat_tnum,r[1])
tnum2 = re.findall(pat_tnum,r[3])
tnum3 = re.findall(pat_tnum,r[5])
tnum4 = re.findall(pat_tnum,r[7])
#print tnum1[0]+'\n'+tnum2[0]+'\n'+tnum3[0]+'\n'+tnum4[0]



#print the date od query
pat_date = re.compile(r'\|(2\d{7})\|')
date = re.findall(pat_date,r[1])
print date[0]


#pat_state = re.compile(r'(?<=\d\|\|)(\d{0,2}|\\.+)(?=\|\d+|\\)')
pat_state = re.compile(r'\|\|\|\|(.+?)\|\|\|\|\|')

state1 = str(re.findall(pat_state,r[1])[0]).split('|')
state2 = str(re.findall(pat_state,r[3])[0]).split('|')
state3 = str(re.findall(pat_state,r[5])[0]).split('|')
state4 = str(re.findall(pat_state,r[7])[0]).split('|')

print 'trainnumber'+' \t'+'YW'+' \t\t'+'RW'+' \t\t'+'YZ'
print tnum1[0]+' \t\t'+state1[5]+' \t'+state1[0]+' \t'+state1[6]
print tnum2[0]+' \t\t'+state2[5]+' \t'+state2[0]+' \t'+state2[6]
print tnum3[0]+' \t\t'+state3[5]+' \t'+state3[0]+' \t'+state3[6]
print tnum4[0]+' \t\t'+state4[5]+' \t'+state4[0]+' \t'+state4[6]

