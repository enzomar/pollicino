#!/bin/bash

nohup /usr/local/sbin/mosquitto -c broker/mosquitto.conf -d </dev/null >/dev/null 2>&1 &
