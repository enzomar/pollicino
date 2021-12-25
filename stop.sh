#!/bin/bash


if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	ps -aux | grep pollicino | grep -v grep | awk '{print "sudo kill -9 " $2}' | sh
	ps -aux | grep broker | grep -v grep | awk '{print "sudo kill -9 " $2}' | sh
	ps -aux | grep mosquitto | grep -v grep | awk '{print "sudo kill -9 " $2}' | sh

elif [[ "$OSTYPE" == "darwin"* ]]; then
	ps -ef | grep pollicino | grep -v grep | awk '{print "kill -9 " $2}' | sh
	ps -ef | grep broker | grep -v grep | awk '{print "kill -9 " $2}' | sh
	ps -ef | grep mosquitto | grep -v grep | awk '{print "kill -9 " $2}' | sh
fi




./state.sh