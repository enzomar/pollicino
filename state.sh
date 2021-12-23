#!/bin/bash

ps -ef | grep pollicino | grep -v grep | awk '{ print "["$2"]: " $9" "$10" "$11" "}'
ps -ef | grep broker | grep -v grep | awk '{ print "["$2"]: " $8" "$9" "$10}'