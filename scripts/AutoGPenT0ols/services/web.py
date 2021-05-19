#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap
import yaml
import os 


def web(all_info, recon_path, out_path):
    target = all_info['target'][0]
    info_data = all_info['scanner']
    
    # get path information
    web_data = os.path.join(recon_path, "web_config.yaml")
    command_info = {} 
    with open(web_data, 'r') as unparsed:
        try:
            web_data = yaml.safe_load(unparsed)
        except yaml.YAMLError as exc:
            print(exc)
        
        list_data = web_data[info_data].keys()

        for options in list_data: 
            descr = web_data[info_data][options]['description']
            out_file = os.path.join(out_path, '.'.join((options, 'txt')))
            cmd = (web_data[info_data][options]['commands'].replace('${{ out_dir }}', out_file).replace('${{ target }}', target))
            command_info[descr] = cmd 
    
    return command_info

