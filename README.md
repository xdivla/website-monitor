# Python3 Endpoint/Website Monitor

A simple endpoint response time, response code and SSL certificate expiry monitor in Python.
The monitor exposes prometheus metrics on port 8888 with the help of the prometheus_client library


### Name of the prometheus metrics with 'site' label:

endpoint_monitor_response_time

endpoint_monitor_response_code

endpoint_monitor_response_status

endpoint_monitor_ssl_cert_expiry


## Features

- Add one or as many websites as you like.

- Adjustable frequency of sent requests

- If the response takes more than 10 seconds, the connection will timout.

- Checks SSL certificate expiry date


## Instructions

### Required

Set the environment variable SITES as a JSON array of website URLs, for example:

SITES = '["https://url1", "https://url2", "https://url3"]'


### Optional

Set the environment variable REQUEST_FREQUENCY for adjusting the frequency of sent requests in seconds (default: 30), for example:

REQUEST_FREQUENCY = 60
