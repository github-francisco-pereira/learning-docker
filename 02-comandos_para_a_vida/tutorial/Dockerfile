FROM python:alpine3.6

RUN pip install flask
RUN pip install redis
COPY . .
ENV FLASK_APP=hello.py
EXPOSE 5000
CMD [ "python", "hello.py" ]