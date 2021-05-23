#!/usr/bin/python3 
## 
                           #                                                                                                                                                                                         
                           ##                                ###                                                                                                                                                     
  ###### #######  ######## ###  ## ######## ####### #######  ###         ####                                                                                                                                        
 ###           ##          #### ##    ###   ##   ##       ## ###        ###                                                                                                                                          
 ###  ##  ######   ####### #######    ###   ##   ##  ##   ## ###        ###                                                                                                                                          
 ###  ##  ###      ###     ### ###    ###   ##   ##  ##   ## ###        ###                                                                                                                                          
  ######  ###      ####### ###  ##    ###   #######   #####  ####### #####                                                                                                                                           
                                 #                                                                                                                                                                                   
# Author : CapitanJ4ck
##

import signal
from sys import exit
import json
import os
import time
import subprocess
from pwn import *
from gptools_cli import gen_cli_args
from services.recon import recon
from services.web import web
from services.smb import smb
from services.ldap import ldap

## Detect Contrl + C 
def signal_handler(key, frame):
    # Handle any cleanup here
    exit = log.progress("SIGINT or CTRL-C detected.")
    exit.status("Exiting...")
    time.sleep(1)
    exit.failure("Exiting gracefully")
    sys.exit(1)

signal = signal.signal(signal.SIGINT, signal_handler)


# Vars 

# Make directories

def mdir(dir_name):
    
    directory_created = True

    try:
        os.makedirs(dir_name)
    
    except OSError:
        directory_created = False
    
    return directory_created

# Managment function, we can build directories for save outputs

def build_infraestucture(dir_name,output):

    infra = log.progress("Managment")
    
    infra.status("Building structure on ")

    
    if not os.path.exists(dir_name):
        directory_created = mdir(dir_name)
        if directory_created: 
            infra.success("Succesfully created the directory {}".format(dir_name))
        else: 
            infra.failure("Creation of the directory {} failed".format(dir_name))
    else: 
        infra.success("Directory {} already exist".format(dir_name))

def run(dir_file, command,service):
    out = dir_file + "out.txt"
    err = dir_file + "err.txt"
#    parsed_command = command ## Util working other commands 
    parsed_command = []
    
    for c in command:
        parsed_command.append(c.replace('·',' '))
    
    print(parsed_command)

    p = log.progress(service)
    
    with open(out,'w+') as fout:
        with open(err,'w+') as ferr:
            
            p.status("Running")           
            try: 
                out=subprocess.call(parsed_command,stdout=fout,stderr=ferr)
                # reset file to read from it
                fout.seek(0)
                # save output (if any) in variable
                output=fout.read()
                
                # reset file to read from it
                ferr.seek(0) 
                # save errors (if any) in variable
                errors = ferr.read()
                if out != 0: 
                    p.failure("Something wrong")
                else: 
                    p.success("Succesfully!")
            except: 
                p.failure("Command timeout")
            
def main():
    
    # Get args from Namespace type 
    args = vars(gen_cli_args())
    
    # Get service
    service = args['services']
    target = args['target'] 
    
    out_path = os.path.join(args['path'],(os.path.join(args['target'],service)))
    config_path = os.path.join(os.getcwd(), os.path.join("data",service))
    
    web_path = out_path # CHANGE WHEN WEB WORKS

    # Build infraestucture for save output
    build_infraestucture(out_path,config_path)

    #print(args) # debug
    # Start progress
    service_progress = log.progress(service)
    
    ## Recon scanner
    if 'recon' == service: 
        scanner = recon(args,config_path,out_path)
    ## Web scanner
    elif 'web' == service: 
        scanner = web(args,config_path,out_path)
    ## smb scanner
    elif 'smb' == service: 
        scanner = smb(args,config_path,out_path) 
    ## ldap scanner
    elif 'ldap' == service: 
        scanner = ldap(args,config_path,out_path) 
    
    print("-- 𝒞𝒽𝑒𝒸𝓀 𝒢𝒫𝑒𝓃𝒯𝒪𝑜𝓁𝓈 --")

    for description, command in scanner.items():
        service_progress.status("{}".format(command))
        run(web_path,command.split(),description) # WEB PATH 
#        time.sleep(2) # Check without exec 

if __name__ == '__main__':
    main()
