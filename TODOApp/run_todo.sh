#!/bin/sh

MYDIR=$(dirname $0)

python $MYDIR/bender/bender.py &
sleep 1

python $MYDIR/friender/friender.py  #blocking

killall python # Needed to kill bg proc
