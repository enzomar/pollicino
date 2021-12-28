#!/bin/bash

echo "# MOSQUITTO"
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
	sudo apt-get install mosquitto
elif [[ "$OSTYPE" == "darwin"* ]]; then
	brew install mosquitto
fi

echo "# VIRTUALENV"
pip3 install virtualenv 
python -m virtualenv -p python3 venv
source venv/bin/activate

echo "# REQUIREMENTS"
pip3 install -r requirements.txt