#!/bin/bash

echo "- Broker"
./daemon_broker.sh
sleep 1
source venv/bin/activate
echo "- Servos"
nohup python pollicino.py -m servos </dev/null >/dev/null 2>&1 &
sleep 1
echo "- Controller"
nohup python pollicino.py -m ctrl </dev/null >/dev/null 2>&1 &
sleep 1
echo "- Sensors"
nohup python pollicino.py -m sensors </dev/null >/dev/null 2>&1 &
sleep 1
echo "Status"
./state.sh

