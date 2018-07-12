FROM python:alpine3.6

COPY . .
RUN pip install -r requirements.txt
ENV FLASK_APP=app.py
EXPOSE 5000
CMD [ "flask", "run" ]