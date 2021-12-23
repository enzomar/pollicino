#!/bin/bash

ps -ef | grep pollicino | grep -v grep | awk '{print "kill -9 " $2}' | sh
ps -ef | grep broker | grep -v grep | awk '{print "kill -9 " $2}' | sh
