#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import urllib
import json
import sys

def fnd(fw):
    print "---"
    print "Nodes with firmware " + fw + ":"
    for n in data['nodes']:
        if data['nodes'][n]['nodeinfo']['software']['firmware']['release'] == fw:
            if data['nodes'][n]['flags']['online'] == True:
                print data['nodes'][n]['nodeinfo']['hostname']


url = "https://freifunk-bs.de/nodes.json"

r = urllib.urlopen(url)

data = json.loads(r.read())

firmwares = set()

for n in data['nodes']:
    if data['nodes'][n]['flags']['online'] == True:
        firmwares.add(data['nodes'][n]['nodeinfo']['software']['firmware']['release'])

print "Current Firmware Versions:"
for f in firmwares:
    print f


if len(sys.argv) >= 2:
    fw = sys.argv[1]
    fnd(fw)
else:
    for f in firmwares:
        fnd(f)
        
