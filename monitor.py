# Libraries
import os
import json
import requests
from time import sleep
from prometheus_client import start_http_server, Gauge

# Prometheus variables
RESPONSE_CODE = Gauge('endpoint_monitor_response_code', 'Response Status code', ["site"])
RESPONSE_TIME = Gauge('endpoint_monitor_response_time', 'Response time in seconds', ["site"])
RESPONSE_STATUS = Gauge('endpoint_monitor_response_status', 'Offline/Online status as 0/1', ["site"])

# Check if the environment variable 'SITES' is defined correctly as an array of URLs
try:
	sites = json.loads(os.environ['SITES'])
except Exception as e:
	print(e)
	print('Please set the required environment variable SITES as an array of URLs: ["https://some_url", "https://some_other_url"]')
	quit()

# 'REQUEST_FREQUENCY' environment variable with default value: 30 and illegal value ''
request_freq = os.environ.get('REQUEST_FREQUENCY', 30)

if (request_freq == ''):
	print('The environment variable REQUEST_FREQUENCY cannot be an empty string.')
	quit()

# Defining the event
def monitor():
	while True:
		for site in sites:
			try:
				res = requests.get(site, timeout=10)
				RESPONSE_TIME.labels(site=site).set(res.elapsed.total_seconds())
				RESPONSE_CODE.labels(site=site).set(res.status_code)
				RESPONSE_STATUS.labels(site=site).set(1)
			except Exception as e:
				print(e)
				print('The site URL ' + site + ' could not be reached or does not exist')
				RESPONSE_STATUS.labels(site=site).set(0)
				continue
		sleep(int(request_freq))

# Starting the server
if __name__ == '__main__':
    start_http_server(8888)
    print('Endpoint monitoring starting... OK')
    monitor()
