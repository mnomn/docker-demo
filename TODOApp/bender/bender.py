import os
from flask import Flask
from flask import jsonify
from flask import request
import logging
import time

logging.basicConfig(filename=__name__+'.log',level=logging.INFO)

BENDER_PORT=54321
if 'BENDER_PORT' in os.environ:
    print("FOUND BP")
    BENDER_PORT=os.environ['BENDER_PORT']

app = Flask(__name__)

# Liat of dicts with "time" and "mess"
test_db=[]

@app.route('/', methods=['POST', 'GET'])
def summary():
    logging.info("BENDER")
    if request.method == 'POST':
        t = time.time()
        jdata = request.get_json()
        mess = jdata['mess']
        test_db.append({'time':t, 'mess':mess})

    # For both get and post, return todo-list.
    return jsonify(test_db)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(BENDER_PORT))
