#!/bin/bash


function create_virtualenv {
	echo "# VIRTUALENV"
	if [ -d venv ]; then
		echo "Skipping beacause it is already created"
	else
		pip3 install virtualenv 
		python -m virtualenv -p python3 venv
	fi
	source venv/bin/activate
}

function install_mosquitto {
	echo "# MOSQUITTO"

	if [[ "$OSTYPE" == "linux-gnu"* ]]; then
		if apt list mosquitto --installed | grep -q mosquitto; then
			echo "Skipping beacause it is already installed"
		else
			sudo apt-get install mosquitto
		fi
	elif [[ "$OSTYPE" == "darwin"* ]]; then
		if brew list --formula -1 | grep -q mosquitto; then
			echo "Skipping beacause it is already installed"
		else
			brew install mosquitto
		fi
	fi
}

function install_requirements {
	echo "# REQUIREMENTS"
	if [[ -z "$VIRTUAL_ENV" ]]
	then
		echo "Skipping beacause virtualenv is not active"
	else
		pip3 install -r requirements.txt
	fi

}



install_mosquitto
create_virtualenv
install_requirements

