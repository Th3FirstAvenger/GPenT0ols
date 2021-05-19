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
    info_data = all_info['scanner']

    # get path information
    recon_data = os.path.join(recon_path, "recon_config.yaml")
    command_info = {} 
    with open(recon_data, 'r') as unparsed:
        try:
            recon_data = yaml.safe_load(unparsed)
        except yaml.YAMLError as exc:
            print(exc)
        print(recon_data) 
        
        list_data = recon_data[info_data].keys()
        print(list_data) 
        
        for options in list_data: 
            descr = recon_data[info_data][options]['description']
            cmd = (recon_data[info_data][options]['commands'].replace('${{ out_dir }}', out_path).replace('${{ target }}', target))
            command_info[descr] = cmd 
    
    return command_info

