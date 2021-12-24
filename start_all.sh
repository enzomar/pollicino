#!/bin/sh

nohup sh broker.sh </dev/null >/dev/null 2>&1  &
source venv/bin/activate

nohup python pollicino.py -m servo </dev/null >/dev/null 2>&1 &
nohup python pollicino.py -m ctrl </dev/null >/dev/null 2>&1 &
nohup python pollicino.py -m sensors </dev/null >/dev/null 2>&1 &
