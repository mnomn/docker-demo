#import sys
from flask import Flask
from flask import jsonify
from flask import request
import logging
import time

logging.basicConfig(filename=__name__+'.log',level=logging.INFO)

app = Flask(__name__)

# Liat of dicts with "time" and "mess"
test_db=[]

@app.route('/', methods=['POST', 'GET'])
def summary():
    logging.info("BENDER")
    if request.method == 'POST':
        jdata = request.get_json()
        logging.info("jdata---" + str(jdata))
        #jdata = r.json()
        mess = jdata['mess']
        logging.info("mess:::" + mess)
        t = time.time()
        logging.info("BENDER POST" + str(t))
        test_db.append({'time':t, 'mess':mess})

    return jsonify(test_db)
