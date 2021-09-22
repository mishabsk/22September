from app import app
from flask import Flask, render_template

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/trigger")
def trigger():
    print('Akshi Bhasker developed this code/ Girl Engineers')
    return 'Navtech Secured Script Flask - Test Version 1 '