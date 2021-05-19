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
from services.recon import *
from services.web import *

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

def build_infraestucture(dir_name):

    infra = log.progress("Managment")
    
    infra.status("Building structure on {}".format(dir_name))

    
    if not os.path.exists(dir_name):
        directory_created = mdir(dir_name) 
        if directory_created: 
            infra.success("Succesfully created the directory {}".format(dir_name))
        else: 
            infra.failure("Creation of the directory {} failed".format(dir_name))
    else: 
        infra.success("Directory {} already exist".format(dir_name))

def run(dir_file, command):
    out = dir_file + "out.txt"
    err = dir_file + "err.txt"

    with open(out,'w+') as fout:
        with open(err,'w+') as ferr:
            
            out=subprocess.call(command,stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            output=fout.read()

            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()

def main():
    
    # Get args from Namespace type 
    args = vars(gen_cli_args())
    
    # Get service
    service = args['services']
    target = args['target'] 
    
    out_path = os.path.join(args['path'],service)
    config_path = os.path.join(os.getcwd(), os.path.join("data",service))

    # Build infraestucture for save output
    build_infraestucture(out_path)
    build_infraestucture(config_path)

    print(args) # debug
    # Start progress
    service_progress = log.progress(service)
    
    ## Recon scanner
    if 'recon' == service: 
        scanner = recon(args,config_path,out_path)
        for description, command in scanner.items():
            service_progress.status("{}".format(description))
#            run(web_path,command.split()) # WEB PATH 
            time.sleep(2) # Check without exec 
            print(command.split())

if __name__ == '__main__':
    main()
