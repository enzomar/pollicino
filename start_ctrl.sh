#!/bin/bash

source venv/activate/bin
nohup python pollicino.py -m ctrl </dev/null >/dev/null 2>&1 &
