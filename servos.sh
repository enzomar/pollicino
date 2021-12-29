#!/bin/bash

source venv/bin/activate
nohup python pollicino.py -m servos </dev/null >/dev/null 2>&1 &
