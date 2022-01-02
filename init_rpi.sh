#!/bin/bash

ansible-playbook -i $1, ansible/init_rpi.yaml --extra-vars "new_hostname=$2"