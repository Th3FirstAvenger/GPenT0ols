#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap
import yaml
import os 
## need port, user, passwd, type scanner, CMS, fuzzing, layer (http/https), wordlist, url 

def web(all_info, recon_path, out_path):
    target = all_info['target']
    info_data = all_info['scanner']
    port = all_info['port']
    url_path = all_info['file_path']

    # Check https or http scheme 
    scheme = 'http'
    if all_info['ssl']:
       scheme = 'https' 

    url = '{0}://{1}:{2}{3}'.format(scheme,target, port, url_path) 
    
    ## Set wordlist
    wordlist = all_info['wordlist']
    
    if wordlist == None:
        wordlist = '/usr/share/seclists/Discovery/Web-Content/big.txt'
    

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
            cmd = (web_data[info_data][options]['commands'].replace('${{ out_dir }}', out_file).replace('${{ target }}', target).replace('${{ port }}', port).replace('${{ url }}', url).replace('${{ wordlist }}',wordlist))
            command_info[descr] = cmd 
    
    return command_info

