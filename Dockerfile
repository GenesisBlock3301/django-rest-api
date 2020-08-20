FROM python:3.7-slim

RUN apt-get update && apt-get install build-essential python-dev -y

#COPY requirements.txt  /var/www/html/requirements.txt
#pip3 install -r /var/www/html/requirements.txt &&
RUN  pip3 install uwsgi

RUN pip3 install django

RUN pip3 install djangorestframework

RUN pip3 install requests
RUN pip3 install drf-nested-routers

COPY . /var/www/html

EXPOSE 9090

WORKDIR /var/www/html

CMD ["uwsgi", "--http", ":9090", "--wsgi-file", "khabarKoy/wsgi.py", "--master", "--processes", "4", "--threads", "2"]


