import os
host = os.environ["REDIS_HOST"]
port = int(os.environ["REDIS_PORT"])
from flask import Flask
from redis import Redis
r = Redis(host=host, port=port, decode_responses=True)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/count")
def num():
    num = r.incr("visits")
    return (f"You are visitor number: {num}.")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5002)
