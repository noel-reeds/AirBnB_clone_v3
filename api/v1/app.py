#!/usr/bin/python3
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/status')
def api_status():
    return jsonify({ "status" : "OK" })


if __name__ == '__main__':
    app.run()
