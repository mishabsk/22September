from app import app
from flask import Flask, render_template,redirect,request, jsonify, make_response
import glob
import json
from functools import wraps
import sys
sys.path.insert(1, '/root/jFiles')
import ver
import os

#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1,'/root/jFiles')
#import ver

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/upload")
def upload():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        password = request.form.get('psw')
        if password != '782701794ad0eae0957c0d35fb32cf5d675d38566b76838b6dbcb9ecdf8fe957':
            return "Unauthorised"
        if 'files[]' not in request.files:
            return redirect(request.url)
        files = request.files.getlist('files[]')
        for file in files:
            filename = file.filename
            file.save(os.path.join("/root/jFiles", filename))
    return "happy upload!"

@app.route("/trigger")
def trigger():
    print('Akshi Bhasker developed this code/ Girl Engineers')
    return 'Navtech Secured Script Flask - Test Version 1 '

@app.route('/query-example')
def query_example():
    # if key doesn't exist, returns None
    language = request.args.get('language')
    return '''<h1>The language value is: {}</h1>'''.format(language)

@app.route("/API")
def API():
    headers = request.headers
    auth = headers.get("X-Api-Key")
    if auth == '782701794ad0eae0957c0d35fb32cf5d675d38566b76838b6dbcb9ecdf8fe957':
        json_dump= ver.get_loc()
        return jsonify({"Output":json_dump}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401

@app.route("/test")
def test():
    return 'Navtech API running... '
