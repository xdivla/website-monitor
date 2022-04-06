# site-monitor

A simple Python3 website response time and response code monitor. 
The monitor exposes both prometheus metrics on port 8888 with the help of the prometheus_client library



## Features

- You can add one or as many websites as you like.

- You can filter through both metrics using the prometheus label "site"



## Instructions

Required: Set the environment variable SITES as a JSON array of websites

Example: SITES='["https://url1", "https://url2", "https://url3"]'


Optional: Set the environment variable REQUEST_FREQUENCY for request frequency in seconds (default: 30)

Example: REQUEST_FREQUENCY = 60