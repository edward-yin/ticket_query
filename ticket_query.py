# -*- coding=utf-8 -*-
#python 2.7.6
#date 2017-06-28

import urllib
import urllib2
import collections
import re
from datetime import datetime, timedelta
from prettytable import PrettyTable
#import codecs
#import json


url = 'https://kyfw.12306.cn/otn/leftTicket/query?'
#user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'

while True:
    date = raw_input('input the date of query\neg. 20170628\n')
    date2 = datetime.strptime(date,'%Y%m%d')
    date = date2.strftime('%Y-%m-%d')
    print ('querying,please sit an relax......')
    for days in range(7):
		datet = date2+timedelta(days)
		values = collections.OrderedDict()
		#query date
		values['leftTicketDTO.train_date'] = datet.strftime('%Y-%m-%d')
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
		x = PrettyTable(["trainnumber","YW","RW","YZ"])
		x.align["trainnumber"] = '1'
		x.padding_width = 1
		x.add_row([tnum1[0],state1[5],state1[0],state1[6]])
		x.add_row([tnum2[0],state2[5],state2[0],state2[6]])
		x.add_row([tnum3[0],state3[5],state3[0],state3[6]])
		x.add_row([tnum4[0],state4[5],state4[0],state4[6]])
		print (x)


    print ('input the new date to continue \nor press the "ctrl+z" to exit\n\n')
