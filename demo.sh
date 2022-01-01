#!/bin/bash


echo "- Broker"
./daemon_broker.sh
sleep 1
./run.sh -c config/pollicino.yaml
./state.sh

