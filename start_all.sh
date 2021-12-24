#!/bin/sh

echo "- Broker"
nohup sh broker.sh </dev/null >/dev/null 2>&1  &
sleep 1
source venv/bin/activate
echo "- Servos"
nohup python pollicino.py -m servo </dev/null >/dev/null 2>&1 &
sleep 1
echo "- Controller"
nohup python pollicino.py -m ctrl </dev/null >/dev/null 2>&1 &
<<<<<<< HEAD
sleep 1
echo "- Sensors"
nohup python pollicino.py -m sensors </dev/null >/dev/null 2>&1 &
sleep 1
echo "Satus"
sh state.sh
=======
nohup python pollicino.py -m sensors </dev/null >/dev/null 2>&1 &
>>>>>>> 7aa02d6d6224aa8269c94fd4eb97fdbdd2ae6d17
