FROM python:3.8-slim
ENV PYTHOUNNBUFFERED 1

RUN mkdir /code
ADD . /code/
WORKDIR /code

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt

COPY wait-for-it.sh /usr/wait-for-it.sh
RUN chmod +x /usr/wait-for-it.sh
