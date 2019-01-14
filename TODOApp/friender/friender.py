import os
from flask import Flask
from flask import render_template
from flask import request
import requests


BENDER_PORT=54321
if 'BENDER_PORT' in os.environ:
    print("FOUND BP")
    BENDER_PORT=os.environ['BENDER_PORT']

FRIENDER_PORT=54322
if 'FRIENDER_PORT' in os.environ:
    print("FOUND FP")
    FRIENDER_PORT=os.environ['FRIENDER_PORT']

app = Flask(__name__)

@app.route("/test")
def test1():
    return "Hello World!"


@app.route("/", methods=['POST', 'GET'])
def root(name=None):
    error = None
    if request.method == 'POST':
        mess = request.form['mess']
        # Send POST to bender
        data1={'mess': mess}
        r = requests.post('http://127.0.0.1:'+BENDER_PORT, json = data1)
    else:
        r = requests.get('http://127.0.0.1:'+BENDER_PORT)
    # Both get and post return json list
    try:
        mess = r.json()
    except expression as identifier:
        print "NO JSON :("
        pass

    return render_template('index.html', mess=mess, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(FRIENDER_PORT))
