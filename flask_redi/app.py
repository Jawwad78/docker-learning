from flask import Flask
from redis import Redis
r = Redis(host='redis', port=6379, decode_responses=True)



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/count")
def num():
    num = r.incr("visits")
    return (f"you are the {num} visitor")

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5002)
