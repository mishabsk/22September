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

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = 6194df3c829666a24686dbc492081659408b9cafc18af2f19136e70ecb9cb871
        # jwt is passed in the request header
        if token in request.headers:
            token = request.headers['token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

@app.route("/test")
def test():
    return 'Navtech API running... '