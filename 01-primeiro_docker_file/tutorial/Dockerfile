FROM python:alpine3.6

RUN pip install flask
COPY . .
ENV FLASK_APP=hello.py
EXPOSE 5000
CMD [ "flask", "run" ]