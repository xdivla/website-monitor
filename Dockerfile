FROM python:3-alpine
ADD site-monitor.py /
RUN pip install requests prometheus_client
CMD [ "python", "./site-monitor.py" ]