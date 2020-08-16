FROM python:3.8-slim
ENV PYTHOUNNBUFFERED 1

RUN mkdir /code
ADD . /code/
WORKDIR /code

RUN pip install -r requirements.txt
RUN pip install -r requirements-test.txt

CMD ["python", "manage_web.py"]
