#!/usr/bin/python2
import sys
import subprocess

output = subprocess.check_output("batctl tg |sed -e 's/( *//g' |awk '{ print $5 }'| sort | uniq -c | sort | sed -e 's/^ *//g'", shell=True)
orgs = []
top = output.splitlines()[-1].split(' ')[0]
clients = 0
for originator in output.splitlines()[0:-1]:
    clients += int(originator.split(' ')[0])
print("all node but top have "+ str(clients)+ " clients, top node {" +output.splitlines()[-1].split(' ')[1] +"} has "+ str(top) +" clients" )
mac = output.splitlines()[-1].split(' ')[1].split(':')[4] + output.splitlines()[-1].split(' ')[1].split(':')[5]
print("try sudo tcpdump -i br-ffbs  -e  \"ether[4:2] == 0x" + mac +"\"  to find the nodes primary mac")
