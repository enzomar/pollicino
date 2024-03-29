#!/bin/bash


source venv/bin/activate
echo "- Launching Servos"
nohup python pollicino.py -m servos $1 $2 </dev/null >/dev/null 2>&1 &
sleep 1
echo "- Launching Controller"
nohup python pollicino.py -m ctrl $1 $2 </dev/null >/dev/null 2>&1 &
sleep 1
echo "- Launching Sensors"
nohup python pollicino.py -m sensors $1 $2 </dev/null >/dev/null 2>&1 &
sleep 1
echo "Status"
./state.sh

