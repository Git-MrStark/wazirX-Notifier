import os
import sys
import time
import datetime
import requests
channel='@WazirXNotifier'



PATH_TO_ADD = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if PATH_TO_ADD not in sys.path:
    sys.path.append(PATH_TO_ADD)

from wazirx_sapi_client.rest import Client

# Keys for private events
api_key = "test_api_key"
secret_key = "test_secret_key"

# public
c = Client()


#print(type(c.send("ping")))
#print(type(c.send("time")))
#print(c.send("system_status"))
#print(c.send("exchange_info"))

def server_time():
	time=c.send("time")
	t=time[1]
	t=str(t['serverTime'])
	t=t[:-3]
	epoch_time=int(t)
	datetime_time = datetime.datetime.fromtimestamp(epoch_time)
	print(datetime_time)
	return datetime_time



def send(text):
	url='https://api.telegram.org/bot5043060299:AAF4lNBzk_7N01gNDslg1YjOPBYq9ht0WlE/sendMessage?chat_id='+channel+'&text='+str(text)
	r=requests.get(url)

		
def marketstatus():
	url="https://api.wazirx.com/api/v2/market-status"
	r=requests.get(url)
	r=r.json()
	list=r['markets']
	#print(len(list))
	#print((list[0]).keys())
	total=len(list)
	i=0
	while(i!=total):
		if(list[i]['type']=='SPOT'):
			print(i,(list[i])['baseMarket'], (list[i])['quoteMarket'],(list[i])['last'])
		i=i+1
		
		
marketstatus()
