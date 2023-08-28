FROM python:3.7

WORKDIR /opt/restapi_testdna
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/restapi_testdna
