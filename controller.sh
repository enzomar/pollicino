#!/bin/bash

source venv/bin/activate
nohup python pollicino.py -m ctrl $1 $2 </dev/null >/dev/null 2>&1 &

