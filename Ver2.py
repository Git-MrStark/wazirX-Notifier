import os
import sys
import time
from datetime import datetime as dt
import requests
import numpy as np
import csv
np.set_printoptions(threshold=sys.maxsize)
channel='@WazirXNotifier'

def servertime(var):
	now= dt.now()
	if(var==1):
		return(now)
	if(var==2):
		return(now.strftime("%H:%M:%S"))

inr=np.array(['S.No.', 'Market','Base', '%Change', 'last'])
usdt=np.array(['S.No.', 'Market','Base','%Change', 'last'])

def telegram(text):
	url='https://api.telegram.org/bot5043060299:AAF4lNBzk_7N01gNDslg1YjOPBYq9ht0WlE/sendMessage?chat_id='+channel+'&text='+str(text)
	r=requests.get(url)

def market():
	try:
		url='https://api.coindcx.com/exchange/ticker'
		r= requests.get(url)
		r=r.json()
		global inr
		global usdt
		i=0
		c1=0
		c2=0
		while(i!=len(r)):
			n=r[i]['market']
			if(n[-3:]=='INR'):
				temp=np.array((c1+1,n[:-3],n[-3:],r[i]['change_24_hour'],r[i]['last_price']))
				inr=np.vstack((inr,temp))
				c1=c1+1
			if(n[-4:]=='USDT'):
				temp=np.array((c2+1,n[:-4],n[-4:],r[i]['change_24_hour'],r[i]['last_price']))
				usdt=np.vstack((usdt,temp))
				c2=c2+1
			i=i+1
	except KeyError:
		None
		
def newmarket():
	

def inrmarket():
	tempinr=np.array(['S.No.', 'Market','Base', '%Change', 'last'])
	l=len(inr)
	for()
	
def main():
	market()
	
main()
