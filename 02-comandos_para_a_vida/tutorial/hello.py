from flask import Flask
import redis

app = Flask(__name__)

@app.route("/")
def hello():
    return "Ola!"

@app.route("/setcache/<key>/<value>", methods=['POST'])
def set_cache(key,value):
    redis_server = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)    
    redis_server.set(key, value)
    return "Yep"

@app.route("/getcache/<key>")
def get_cache(key):
    redis_server = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
    return redis_server.get(key)


def gogo():
    app.run(host='0.0.0.0', port=5000)

gogo()