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
values['leftTicketDTO.train_date'] = '2017-07-02'
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
    print 'OK'
page = response.read()
#save to file
f = open('12306-0703.json','w')
f.write(page)
print page


result =str(re.findall(r'\[(.+?)\]',page))
print('the result is')
print result.replace('"','\n')

f =codecs.open('12306-0703.json','r')
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
