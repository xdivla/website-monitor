# Libraries
import os
import json
import asyncio
import requests
from time import sleep
from prometheus_client import start_http_server, Gauge

# Prometheus variables
RESPONSE_CODE = Gauge('response_code', 'Response Status code', ["site"])
RESPONSE_TIME = Gauge('response_time', 'Response time in seconds', ["site"])

# Check if the environment variable 'SITES' is defined correctly as an array of URLs
try:
	sites = json.loads(os.environ['SITES'])
except: 
 	print('Please set the environment variable SITES as an array of URLs: ["https://some_url", "https://some_other_url"]')
 	quit()

# Defining the event
def monitor():
	while True:
		for site in sites:
			try:
				res = requests.get(site)
			except:
				print('The site URL ' + site + ' could not be reached or does not exist')
				continue

			RESPONSE_TIME.labels(site=site).set(res.elapsed.total_seconds())
			RESPONSE_CODE.labels(site=site).set(res.status_code)
		sleep(5)

if __name__ == '__main__':
    start_http_server(8888)
    monitor()