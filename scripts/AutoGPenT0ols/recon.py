#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap

from pwn import *
import json
import time
import subprocess


# Vars 
## PATH=dsdas
nmap_p = '{"name":"nmap", "command":["nmap -p- --min-rate 5000 -n -oG ./allports 127.0.0.1", "nmap -p-"]}'

p1 = log.progress("Recon")
data = json.loads(nmap_p)


def main():
    p1.status("{}".format(data['name']))
    time.sleep(2)
    with open('out.txt','w+') as fout:
        with open('err.txt','w+') as ferr:
            for command in data['command']:
            out=subprocess.call([command],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            output=fout.read())

            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()

main()
