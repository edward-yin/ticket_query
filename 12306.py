# -*- coding=utf-8 -*-
import urllib
import urllib2
import json
import collections
import re

url = 'https://kyfw.12306.cn/otn/leftTicket/query?'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = collections.OrderedDict()
values['leftTicketDTO.train_date'] = '2017-07-02'
values['leftTicketDTO.from_station'] = 'BJP'
values['leftTicketDTO.to_station'] = 'XNO'
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
f = open('d_12306.txt','w')
f.write(page)
print page


result =str(re.findall(r'\[(.+?)\]',page))
print('the result is')
print result.replace('"','\n')
