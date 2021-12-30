
# Pollicino

*"Done is better than perfect!"* and *"Premature optimization is the root of all evil"* are two of the guidelines I am following for my new Christmas project. As almost every year I commit myself to start and hopeful to complete a project and this time I focused on domotic and gardening.

The goal of the project is indeed to provide a way to ***automatize plants  and garden caring***.

It is full of projects on internet about this and I do took a lot of inspiration from them but I added some some personalization to enable scalability, customization and plug and play approach.

Here some of the component and tools used to give you an idea of what you will find here:

- Raspberry PI Zero W
- Sensors (Moisture, Brightness,...)
- Solenoid valve, servo motor
- MQTT (Mosquitto, MQTT Explorer)
- Ansible
- Docker
- Python
- ...

<hr/>

### Table of Contents

1. [If you have just some minutes...](#some_minutes)
2. [Software and flow](#software) (Almost finished)
3. [Hardware](#hardware) (Just started)
4. [Up and running](#all) (To do)
6. [Contributing and next step](#contributing)
7. [References](#references)

<hr/>

# If you have just some minutes... <a name="some_minutes"></a>

## Prerequisites
Ensure you have installed

- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- [MQTT Explorer](http://mqtt-explorer.com/)
- [Docker](https://docs.docker.com/get-docker/)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Run simulation

1) Start machines on docker

On **Terminal 1**

```bash
git clone git@github/enzomar/pollicino
cd pollicino/emu
docker-compose up
```

2) Configure manchines and start

On **Terminal 2**

```bash
cd pollicino/ansible
ansible-playbook setup.yaml -i hosts_emu
ansible-playbook start.yaml -i hosts_emu
```

3) Open MQTT Explorer and create a new connection ( host = localhost, port = 1883)

On **MQQT Explorer**

![MQTT_Explorer](docs/MQTT_Explorer.png)

4)  Connect to the broker and explore

![MQTT_Explorer2](docs/MQTT_Explorer2.png)

5) Close 

On **Terminal 1**

```shell
CTRL+c
```

# If you have more time... 
# Software <a name="software"></a>

## Flow

![archi](docs/flow.png)

- The **sensor** it is in charge to observe regularly the phisical environment and publish state and measurement
- The **controller** goal is to read the input from the sensors and, after applying a certain logic, it will eventually send commands to the servo to change the state of the environment. It is also possible to *schedule* commands.
- The objective of the **servo** is to execute the command sent by the controller by activating an engine, solenoid valve or any other phisical device. It has triggers:
    - *Switch*: it is basic binary on / off cmmands (ie. shiwtgin on/off a light)
    - *Square*: Is will maitain a certain state for a given time (ie. open water for a given amout of time)
    - *Pulse*: it will change state multiple times over time 

- The **broker** role is to provide a scalable and realilable message bus used by the oher component to communicate.

## Message Bus  
The protocol choosed to make the components exchanging messages is [MQTT](https://mqtt.org/). It can be considered the standard in the IoT communication.   
MQTT is a pub/sub protocol and its main elementis the topic to be published by a producer and subscribed by consumer. I strongly suggest you to have a look to this [link](https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/) , it explains quite well how to perform the first step into the deisgn part of MQTT Topic.
### Topic
Defining the topic grammar is crucial in order to be able to govern the message exchange in a clear way. Here below the topic's pattern designed:
    
    PATTERN_STATUS = '{sector}/{category}/{type}/{dev_id}'
    PATTERN_CMD_PUB = '{sector}/{category}/{type}/{dev_id}/set'
    PATTERN_CMD_SUB = '{sector}/{category}/+/+/set'

- The *sensor* will **publish** PATTERN_STATUS
- The *controller* will **suscribe** to PATTERN_STATUS
- The *controller* will **publish** to PATTERN\_CMD_PUB
- The *servo* will **suscribe** to PATTERN\_CMD_SUB

Note that all sensors and servos (*category*) operate in a certain *sector* and they are identifed by a *type* and an *id*


## Components

![archi](docs/pollicino.png)


## Sensor
The sensors needs to transmit at regular time status of a given device. It is possible to set **polling_in\_second** 

## Controller

## Servos

## Project Organization

```bash
├── ansible           <- ansible roles to automatize tasks across multiple machienes
├── broker            
├── controller
├── docs
├── emu
├── helpers
├── sensors
├── servos
├── venv
├── LICENSE.md
├── MANIFEST.in
├── README.md
├── __init__.py
├── _config.yml
├── broker.sh
├── controller.sh
├── daemon_broker.sh
├── pollicino.py
├── pollicino.yaml
├── requirements.txt
├── sensors.sh
├── servos.sh
├── setup.sh
├── start_all.sh
├── state.sh
└── stop.sh
```

# Simulation
I decide to test all the entire application before finalizing the hardware connestion and soldering. The idea is to use 
- docker to instance


# Hardware <a name="hardware"></a>


This is the hardware used:
- 3 Raspberry PI Zero W
- Raspberry Pi Relay Hat 5V
- Soil Moisture sensors (resistive) + ADC
- 2 FPD-270A solenoid valve 12V
- Router TP link TL-MR3020
- NP7-12 FR 1v Volte BAttery

## Raspberry PI Zero W

## Moisture Sensors

## GPIO Soldier

# Network

# Putting all together <a name="all"></a>



# Next steps and on going tasks <a name="next"></a>

# Contributing <a name="contributing"></a>

# References <a name="reference"></a>




------------------------------------------
Python 3 MUST!


"Premature Optmization is the roots of all the evil"
"Done is better than perfect"


Flow
-------

title Flow 
participant Hardware\ndevice as d
participant App\nsensors as i
participant App\nctrl as c
participant App\nservos as o
participant Hardware\nmotor as m


note over i,o
Common configuration
- MQTT broker
- topic pattern
end note

note over c
subscribe to "<sector>/sensors/+/+"
link sensor and servo topics with <threshold>
end note

loop each X sec
i->d: query
d-->i: M
i->c: mqtt://<sector>/sensors/<type>/<id>: <value>
end
note over c
Apply logic 
if <value> > <threshold> 
then <state>
end note
note over o
subscribe to "<sector>/servos/<type>/<id>/set"
end note
c->o: mqtt://<sector>/servos/<type>/<id>/set: <state>
alt switch
o->m: query
alt 0
m-->o: 0
o->m: set 1
else 1
m-->o: 1
end
end
alt square
o->m: query
m-->o: <initial_state>
o->m: <state>
note over o
sleep
end note
o->m: <initial_state>
end

alt pulse
o->m: query
m-->o: <initial_state>
loop whished num of pulse
o->m: <state_a>
note over o
sleep
end note
o->m: <state_b>
note over o
sleep
end note
end
o->m: <initial_state>
end








Software
-------
sensor and servo -> pollicino.py
broker 


Hardware
-------


Next Step Going Big
-------
Ansible
Cockpit

https://grafana.com/blog/2021/08/12/streaming-real-time-sensor-data-to-grafana-using-mqtt-and-grafana-live/


References
-------
https://www.ev3dev.org/docs/tutorials/sending-and-receiving-messages-with-mqtt/
http://www.steves-internet-guide.com/client-connections-python-mqtt/
https://nodered.org/about/
http://mqtt-explorer.com/
https://www.hivemq.com/blog/mqtt-essentials-part-5-mqtt-topics-best-practices/

https://www.raspberryitaly.com/pigarden-e-pigardenweb-realizza-il-tuo-impianto-di-irrigazione-con-raspberry-pi/

https://www.youtube.com/watch?v=51dg2MsYHns

https://mtlynch.io/greenpithumb/

https://projects.raspberrypi.org/en/projects/build-your-own-weather-station/3

https://schedule.readthedocs.io/en/stable/examples.html#pass-arguments-to-a-job

https://crontab.guru/#0_7_*_2_*

https://nazrul.me/2019/07/17/ssh-agent-forward-into-docker-container-on-macos/

https://pinout.xyz/pinout/pin11_gpio17


ansible-playbook setup.yaml -i hosts_emu -v

Ansible
--------
ssh-copy-id -i .ssh/id_rsa.pub pi@raspberrypi
ansible -i hosts -m setup -a 'filter=ansible_memtotal_mb' all
ssh-keygen -t rsa
install samba
git clone git@github.com:enzomar/pollicino.git
sudo apt install python3 idle3
sudo update-alternatives --install $(which python) python $(readlink -f $(which python3)) 3
venv
pip install -r requirements.txt
install samba -> https://pimylifeup.com/raspberry-pi-samba/



- enable ssh over internet
- assign static ip
- create ssh key pair
- git clone
