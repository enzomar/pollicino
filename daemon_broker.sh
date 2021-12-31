#!/bin/bash


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	nohup /usr/sbin/mosquitto -c pollicino/broker/mosquitto.conf -d </dev/null >/dev/null 2>&1 &
elif [[ "$OSTYPE" == "darwin"* ]]; then
	nohup /usr/local/sbin/mosquitto -c pollicino/broker/mosquitto.conf -d </dev/null >/dev/null 2>&1 &
fi
