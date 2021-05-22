#!/usr/bin/env python3
### This script enum all ports, services and vulnerabilities with nmap
import yaml
import os 

def smb(all_info, recon_path, out_path):
#    target = all_info['target']
#    info_data = all_info['scanner']
#    port = all_info['port']
    tags = all_info['tags']
    
    ## Set wordlist
#    wordlist = all_info['wordlist']
#    
#    if wordlist == None:
#        wordlist = '/usr/share/seclist/Discovery/Web-Content/big.txt'
    

    # get path information
    smb_data = os.path.join(recon_path, "smb_config.yaml")
    command_info = {} 
     
    with open(smb_data, 'r') as unparsed:
        try:
            smb_data = yaml.safe_load(unparsed)
        except yaml.YAMLError as exc:
            print(exc)
        
        list_data = smb_data.keys()
        
        final_services = {}  
        
        tag = 'no'
        for service in  
            
        

        print(list_data)
#        for options in list_data:
#            descr = web_data[info_data][options]['description']
#            out_file = os.path.join(out_path, '.'.join((options, 'txt')))
#            cmd = (web_data[info_data][options]['commands'].replace('${{ out_dir }}', out_file).replace('${{ target }}', target).replace('${{ port }}', port).replace('${{ url }}', url).replace('${{ wordlist }}',wordlist))
#            command_info[descr] = cmd 
    
 #   return command_info

