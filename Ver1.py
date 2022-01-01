import os
import sys
import time
import datetime
import requests
import numpy as np
import csv
np.set_printoptions(threshold=sys.maxsize)
channel='@WazirXNotifier'



def server_time():
    try:
    	url='https://api.wazirx.com/sapi/v1/time'
    	r=requests.get(url)
    	r=r.json()
    	t=(r['serverTime'])
    	t=t/1000
    	return t
    except KeyError:
    	return server_time()
    	
cryptomat=np.array(['S.No.', 'baseAsset', 'quoteAsset', server_time()])

def epoch(t):
	datetime_time = datetime.datetime.fromtimestamp(t)
	return datetime_time
	
def totimestamp(t):
	datetime_time=datetime.datetime.timestamp(t)
	return datetime_time


def send(text):
	url='https://api.telegram.org/bot5043060299:AAF4lNBzk_7N01gNDslg1YjOPBYq9ht0WlE/sendMessage?chat_id='+channel+'&text='+str(text)
	r=requests.get(url)


def market():
	try:
		url='https://api.wazirx.com/sapi/v1/tickers/24hr'
		r= requests.get(url)
		r=r.json()
		global cryptomat
		i=0
		while(i!=len(r)):
			temp= np.array([i+1,r[i]['baseAsset'],r[i]['quoteAsset'],r[i]['lastPrice']])
			cryptomat=np.vstack((cryptomat, temp))
			i=i+1
	except KeyError:
		market()
		
def pricefetch():
	try:
		url='https://api.wazirx.com/sapi/v1/tickers/24hr'
		r= requests.get(url)
		r=r.json()
		global cryptomat
		temp2= np.array([server_time()])
		i=0
		while(i!=len(r)):
			temp=np.array([r[i]['lastPrice']])
			temp2=np.vstack([temp2, temp])
			i=i+1
		cryptomat=np.hstack([cryptomat,temp2])
	except KeyError:
		pricefetch()
		


def csvw():
	array_2D = cryptomat
	with open("work.csv","w+") as my_csv:
	  	 newarray = csv.writer(my_csv,delimiter=',')
	  	 newarray.writerows(array_2D)



market()
#print(cryptomat)
#i=0
#while(i!=50):
#	pricefetch()
#	print(i)
#	i=i+1
#pricefetch()
#print(cryptomat)

#datalog()

csvw()
