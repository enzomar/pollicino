#!/bin/bash


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	ps -aux | grep pollicino | grep -v grep | awk '{ print "["$2"]: " $9" "$10" "$11" "}'
	ps -aux | grep broker | grep -v grep | awk '{ print "["$2"]: " $8" "$9" "$10}'
	ps -aux | grep mosquitto | grep -v grep | awk '{ print "["$2"]: " $8" "$9" "$10}'

elif [[ "$OSTYPE" == "darwin"* ]]; then
	ps -ef | grep pollicino | grep -v grep | awk '{ print "["$2"]: " $9" "$10" "$11" "}'
	ps -ef | grep broker | grep -v grep | awk '{ print "["$2"]: " $8" "$9" "$10}'
	ps -ef | grep mosquitto | grep -v grep | awk '{ print "["$2"]: " $8" "$9" "$10}'
fi



