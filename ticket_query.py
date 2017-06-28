# -*- coding=utf-8 -*-
#python 2.7.6
#date 2017-06-28
import urllib
import urllib2
import json
import collections
import re
import codecs

url = 'https://kyfw.12306.cn/otn/leftTicket/query?'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = collections.OrderedDict()
#query date
values['leftTicketDTO.train_date'] = raw_input('input the date of query\neg. 2017-06-28\n')
#start station
values['leftTicketDTO.from_station'] = 'BJP'
#final station
values['leftTicketDTO.to_station'] = 'XNO'
#ticket type
values['purpose_codes'] = 'ADULT'
data = urllib.urlencode(values)
geturl = url+data
request = urllib2.Request(geturl)


try :
    response = urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code
    print e.reason
except urllib2.URLError,e:
    print e.code
    print e.reason
else :
    print 'OK\n'
page = response.read()


#save to file
#this feature is just for testing
#f = open('12306-0703.json','w')
#f.write(page)
#print page



print('Here is the result\n')
print values['leftTicketDTO.train_date']


'''
f =codecs.open('d_12306.txt','r')
f_read = f.read()#.decode('utf-8')
#print f_read
pattern = re.compile(r'\[(.+?)\]')
result = str(re.findall(pattern,f_read))
#print result
print ('the result')
'''


result =str(re.findall(r'\[(.+?)\]',page))

#replace the Chinese characters to English
r_result = str(result.replace('"','\n').replace('\\xe6\\x97\\xa0','soldout').replace('\\xe6\\x9c\\x89','available'))
r = r_result.split('\n')

#get the number of the train
pat_tnum = re.compile(r'\|(T\d+|Z\d+|K\d+)\|')
tnum1 = re.findall(pat_tnum,r[1])
tnum2 = re.findall(pat_tnum,r[3])
tnum3 = re.findall(pat_tnum,r[5])
tnum4 = re.findall(pat_tnum,r[7])
#print tnum1[0]+'\n'+tnum2[0]+'\n'+tnum3[0]+'\n'+tnum4[0]


'''
#print the date od query
pat_date = re.compile(r'\|(2\d{7})\|')
date = re.findall(pat_date,r[1])
print date[0]
'''

#get the state of the trains
pat_state = re.compile(r'\|\|\|\|(.+?)\|\|\|\|\|')
state1 = str(re.findall(pat_state,r[1])[0]).split('|')
state2 = str(re.findall(pat_state,r[3])[0]).split('|')
state3 = str(re.findall(pat_state,r[5])[0]).split('|')
state4 = str(re.findall(pat_state,r[7])[0]).split('|')

#the final result
print 'trainnumber'+' \t'+'YW'+' \t\t'+'RW'+' \t\t'+'YZ'
print tnum1[0]+' \t\t'+state1[5]+' \t'+state1[0]+' \t'+state1[6]
print tnum2[0]+' \t\t'+state2[5]+' \t'+state2[0]+' \t'+state2[6]
print tnum3[0]+' \t\t'+state3[5]+' \t'+state3[0]+' \t'+state3[6]
print tnum4[0]+' \t\t'+state4[5]+' \t'+state4[0]+' \t'+state4[6]
