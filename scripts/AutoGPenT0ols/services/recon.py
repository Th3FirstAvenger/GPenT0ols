#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap
import yaml
import os 

#{'threads': 100, 'verbose': False, 'path': '/tmp/autorecon/', 'services': 'recon', 'target': ['127.0.0.1'], 'all_ports': True, 'ports': None}

#Gen command for get all ports
#def reg_ports(ports):

def recon(all_info, recon_path, out_path):
    target = all_info['target'][0]
    out_path = all_info['path']
    
    recon_commands = []

    # get path information
    recon_data = os.path.join(recon_path, "recon_config.yaml")
    cmd = 1
    
    with open(recon_data, 'r') as unparsed:
        try:
            print(yaml.safe_load(unparsed))
        except yaml.YAMLError as exc:
            print(exc)
    
        #cmd = (data['commands'].replace('${{ out_dir }}', target)
         #                 .replace('${{ target }}', target))
    
    return cmd

