#!/bin/bash

source venv/bin/activate
nohup python pollicino.py -m servos $1 $2 $3 </dev/null >/dev/null 2>&1 &
