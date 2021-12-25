#!/bin/bash

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	/usr/sbin/mosquitto -c broker/mosquitto.conf -v
elif [[ "$OSTYPE" == "darwin"* ]]; then
	/usr/local/sbin/mosquitto -c broker/mosquitto.conf -v
fi


