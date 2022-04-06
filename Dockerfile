FROM python:3-alpine
ADD monitor.py /
RUN pip install requests prometheus_client
CMD [ "python", "./monitor.py" ]