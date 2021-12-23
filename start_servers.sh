#!/bin/bash

source venv/activate/bin
nohup python pollicino.py -m sensors </dev/null >/dev/null 2>&1 &
