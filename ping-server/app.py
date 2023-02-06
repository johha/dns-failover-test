#!/usr/bin/python3
import time

from flask import Flask, make_response, Response
from werkzeug.serving import WSGIRequestHandler
from flask import jsonify


app = Flask(__name__)

@app.route("/v1/ping", methods=["GET", "POST"])
def ping():
    # time.sleep(5)
    return jsonify({"message": "pong"})

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "hi"})

if __name__ == "__main__":
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(debug=True)