#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap

from pwn import *
import json
import time
import subprocess


# Vars 
## PATH= dsad
nmap_p = '{ "name":"nmap allports", "command":"nmap -p- --min-rate 5000 -n -oG ./allports 127.0.0.1"}'

p1 = log.progress("Recon")
data = json.loads(nmap_p)


