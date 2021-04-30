#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap

from pwn import *
import json
import time
import subprocess


# Vars 
## PATH=dsdas
nmap_p = '{ "name":"nmap allports", "command":"nmap -p- --min-rate 5000 -n -oG ./allports 127.0.0.1"}'

p1 = log.progress("Recon")
data = json.loads(nmap_p)

def main():
    global single_target
    global only_scans_dir
    global port_scan_profile
    global heartbeat_interval
    global nmap
    global srvname
    global verbose

    _init()
    parser = argparse.ArgumentParser(description='Network reconnaissance tool to port scan and automatically enumerate services found on multiple targets.')
    parser.add_argument('-o', '--output', action='store', default='results', dest='output_dir', help='The output directory for results. Default: %(default)s')
    parser.add_argument('-t','--target', action='store_true', default=False, help='Only scan a single target. A directory named after the target will not be created. Instead, the directory structure will be created within the output directory. Default: false')
    parser.error = lambda s: fail(s[0].upper() + s[1:])
    args = parser.parse_args()

    target = args.target
    only_scans_dir = args.only_scans_dir

    errors = False

