Python 3 MUST!


"Premature Optmization is the roots of all the evil"
"Done is better than perfect"


Flow
-------

title Generic commumnication MQTT 
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

Ansible
--------
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
