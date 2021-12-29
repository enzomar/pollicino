#!/bin/bash

source venv/bin/activate
nohup python pollicino.py -m sensors </dev/null >/dev/null 2>&1 &