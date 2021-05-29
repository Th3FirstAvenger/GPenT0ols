#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap
import yaml
import os 


def get_tags(ftp_data, tags):
    
    list_data = ftp_data.keys()
    final_services = [] 

    for parameter in tags:
        for technique in list_data:
            total = 0
            for opt in ftp_data[technique]['tags']: 
                ecual = False
                if parameter.lower() == opt.lower(): 
                    ecual = True
                    total +=1
                if not ecual:
                    break
            if total == len(tags):
                final_services.append(technique)

    return final_services

def ftp(all_info, recon_path, out_path):
    target = all_info['target']
    port = all_info['port']
    tags = all_info['tags'].split(',')
    username = all_info['username']
    password = all_info['password']
    
    if len(username) == 0 or len(password) == 0: 
        username = 'anonymous'
        password = ''

    # Check https or http scheme 
    scheme = 'ftp'
    if all_info['ssl']:
       scheme = 'ftps' 
    
    # get path information
    ftp_data = os.path.join(recon_path, "ftp_config.yaml")
    command_info = {} 
     
    with open(ftp_data, 'r') as unparsed:
        try:
            ftp_data = yaml.safe_load(unparsed)
        except yaml.YAMLError as exc:
            print(exc)
        
        services = get_tags(ftp_data, tags)        
        
        for options in services:
            descr = ftp_data[options]['description']
            out_file = os.path.join(out_path, '.'.join((options, 'txt')))
            cmd = (ftp_data[options]['commands'].replace('${{ out_dir }}', out_file).replace('${{ target }}', target).replace('${{ port }}', port).replace('${{ username }}', username).replace('${{ password }}', password).replace('${{ scheme }}', scheme))
            command_info[descr] = cmd 
         
    return command_info

