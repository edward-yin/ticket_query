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
		#replace the Chinese characters to English
		page = response.read().replace('\xe6\x97\xa0','soldout').replace('\xe6\x9c\x89','available')


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


		pattern = re.compile(r'\[(.+?)\]')
		result = str(re.findall(pattern,page))

		
		pattern = re.compile(r'"(.+?)"')
		#state of every train
		s_result = re.findall(pattern,result)

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
		print (x)


    print ('input the new date to continue \nor press the "ctrl+z" to exit\n\n')
