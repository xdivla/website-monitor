# site-monitor

A simple Python3 website response time and response code monitor. 
The monitor exposes both prometheus metrics on port 8888 with the help of the prometheus_client library

You can add one or as many websites as you like.

Enjoy :)


## Instructions

Set the environment variable SITES as a JSON array:

SITES='["https://url1", "https://url2", "https://url3"]'