import os
from flask import Flask
from flask import render_template
from flask import request
import requests

BENDER_PORT=os.environ['BENDER_PORT']
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello(name=None):
    print("GET ROOT!!")
    error = None
    if request.method == 'POST':
        mess = request.form['mess']
        # Send POST to bender
        data1={'mess': mess}
        r = requests.post('http://127.0.0.1:'+BENDER_PORT, json = data1)
        print ("POST RESP: " + str(r.status_code))
    else:
        r = requests.get('http://127.0.0.1:'+BENDER_PORT)
    # Both get and post return json list
    mess = r.json()

    return render_template('index.html', mess=mess, error=error)
