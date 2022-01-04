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
    	t=int(t/1000)
    	return t
    except KeyError:
    	return server_time()

currenttime=0
    	

def epoch(t):
	datetime_time = datetime.datetime.fromtimestamp(t)
	return datetime_time
	
def totimestamp(t):
	datetime_time=datetime.datetime.timestamp(t)
	return datetime_time
	
def settime():
	global currenttime
	currenttime=server_time()

cryptomat=np.array(['S.No.', 'baseAsset', 'quoteAsset',server_time()])

percentdata=np.array([currenttime])

def send(text):
	url='https://api.telegram.org/bot5043060299:AAF4lNBzk_7N01gNDslg1YjOPBYq9ht0WlE/sendMessage?chat_id='+channel+'&text='+str(text)
	r=requests.get(url)


def market():
	try:
		url='https://api.wazirx.com/sapi/v1/tickers/24hr'
		r= requests.get(url)
		r=r.json()
		global cryptomat
		global percentdata
		i=0
		while(i!=len(r)):
			temp= np.array([i+1,r[i]['baseAsset'],r[i]['quoteAsset'],r[i]['lastPrice']])
			cryptomat=np.vstack((cryptomat, temp))
			i=i+1
		percentdata=np.delete(cryptomat,3,1)
	except KeyError:
		market()
		
def pricefetch():
	try:
		url='https://api.wazirx.com/sapi/v1/tickers/24hr'
		r= requests.get(url)
		r=r.json()
		global cryptomat
		global percentdata
		temp2= np.array([currenttime])
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



#market()
#print(cryptomat)
#i=0
#while(i!=50):
#pricefetch()
#	print(i)
#	i=i+1
#pricefetch()
#print(cryptomat)

#datalog()

#csvw()

def percentcalc():
	global percentdata
	rows=len(cryptomat)
	columns=len(cryptomat[0])
	i=1
	temp2= np.array([currenttime])
	while(i!=rows):
		a=float(cryptomat[i][columns-1])
		b=float(cryptomat[i][3])
		per=((a-b)/b)*100
		temp=np.array((per))
		temp2=np.vstack([temp2, temp])
		i=i+1
	percentdata=np.hstack([percentdata,temp2])

def percentcheck():
	i=0
	l1= percentdata[0,3:]
	while(i!=len(l1)):
		if((currenttime)-float(l1[i])<=30):
			break
	print(percentdata[:,i+3])
		


def deleter():
	global cryptomat
	global percentdata
	cryptomat=np.delete(cryptomat,3,1)
	percentdata= np.delete(percentdata,3,1)
	
				
def main():
	market()
	i=1
	while(i!=1000):
		settime()
		pricefetch()
		percentcalc()
		t=epoch(currenttime)
		if(int(t.strftime('%M'))%1==0):
			percentcheck()
		i=i+1
	
main()
