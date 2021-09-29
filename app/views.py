from app import app
from flask import Flask, render_template, request, jsonify, make_response
import jwt
from functools import wraps

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/trigger")
def trigger():
    print('Akshi Bhasker developed this code/ Girl Engineers')
    return 'Navtech Secured Script Flask - Test Version 1 '

@app.route("/API")
def API()
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == '6194df3c829666a24686dbc492081659408b9cafc18af2f19136e70ecb9cb871':
        return jsonify({"message": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

@app.route("/test")
def test():
    return 'Navtech API running... '