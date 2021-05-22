#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap
import yaml
import os 


def get_tags(smb_data, tags):
    
    list_data = smb_data.keys()
    final_services = [] 

    for parameter in tags:
        for technique in list_data:
            total = 0
            for opt in smb_data[technique]['tags']: 
                ecual = False
                if parameter.lower() == opt.lower(): 
                    ecual = True
                    total +=1
                if not ecual:
                    break
            if total == len(tags):
                final_services.append(technique)

    return final_services

def smb(all_info, recon_path, out_path):
    target = all_info['target']
    port = all_info['port']
    tags = all_info['tags'].split(',')
    username = all_info['username']
    password = all_info['password']
    
    if len(username) == 0 or len(password) == 0: 
        username = ''
        password = ''

    # get path information
    smb_data = os.path.join(recon_path, "smb_config.yaml")
    command_info = {} 
     
    with open(smb_data, 'r') as unparsed:
        try:
            smb_data = yaml.safe_load(unparsed)
        except yaml.YAMLError as exc:
            print(exc)
        
        services = get_tags(smb_data, tags)        
        
        for options in services:
            descr = smb_data[options]['description']
            out_file = os.path.join(out_path, '.'.join((options, 'txt')))
            cmd = (smb_data[options]['commands'].replace('${{ out_dir }}', out_file).replace('${{ target }}', target).replace('${{ port }}', port).replace('${{ username }}', username).replace('${{ password }}', password))
            command_info[descr] = cmd 
         
    return command_info

