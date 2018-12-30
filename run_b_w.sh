#/bin/bash

export FLASK_APP=bender/bender.py
export FLASK_RUN_PORT=54321
export BENDER_PORT=54321
#Local dev path. Not so god :) 
#~/Library/Python/2.7/bin/flask run &
flask run &
b_proc=$! #Get proc, so ew can kill it 
echo "PROC "$b_proc

sleep 2

export FLASK_APP=wendy/wendy.py
export FLASK_RUN_PORT=54320
#~/Library/Python/2.7/bin/flask run #This call is blocking
flask run
echo "Closed wendy"
echo "Closing bender $b_proc"
kill $b_proc
