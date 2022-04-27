# Python3 Website Monitor

A simple website response time and response code monitor in python.
The monitor exposes both prometheus metrics on port 8888 with the help of the prometheus_client library

### Name of the prometheus metrics:

website_monitor_response_time

website_monitor_response_code


### Docker image: 

divla/website-monitor



## Features

- Add one or as many websites as you like.

- Adjustable frequency of sent requests

- If the response takes more than 10 seconds, the connection will timout.

- You can filter through metrics using labels:
    - 'site': Website URL (example: 'https://divla.eu')
    - 'status': 'online' or 'offline'
    - 'code': HTTP response status code (example: '200')



## Instructions


### Required

Set the environment variable SITES as a JSON array of website URLs, for example:

SITES = '["https://url1", "https://url2", "https://url3"]'


### Optional

Set the environment variable REQUEST_FREQUENCY for adjusting the frequency of sent requests in seconds (default: 30), for example:

REQUEST_FREQUENCY = 60
