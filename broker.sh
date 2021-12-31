#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	/usr/sbin/mosquitto -c pollicino/broker/mosquitto.conf -v
elif [[ "$OSTYPE" == "darwin"* ]]; then
	/usr/local/sbin/mosquitto -c pollicino/broker/mosquitto.conf -v
fi
