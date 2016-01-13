#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import json
import sys
import subprocess

def fnd(fw):
    print "---"
    print "Nodes with firmware " + fw + ":"
    for n in data:
        if data[n]['software']['firmware']['release'] == fw:
	    if 'owner' not in data[n]:
                print data[n]['hostname'] + " <kein Kontakt>" 
	    else:
                print data[n]['hostname'] + " von " + data[n]['owner']['contact']
		

output = subprocess.check_output("alfred-json -r 158", shell=True)

data = json.loads(output)

firmwares = set()

for n in data:
    firmwares.add(data[n]['software']['firmware']['release'])

print "Current Firmware Versions:"
for f in firmwares:
    print f

if len(sys.argv) >= 2:
    fw = sys.argv[1]
    fnd(fw)
else:
    for f in firmwares:
        fnd(f)
        
