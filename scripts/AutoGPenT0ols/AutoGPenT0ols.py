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

import json
import os
import time
import subprocess
from pwn import *
from gptools_cli import gen_cli_args
from recon import *


# Vars 

# Make directories

def mdir(progress, dir_name):
    
    directory_created = True

    try:
        os.makedirs(dir_name)
    
    except OSError:
        directory_created = False
    
    return directory_created

# Managment function, we can build directories for save outputs

def build_infraestucture(out_path, services):

    infra = log.progress("Managment")
    
    infra.status("Building structure on {}".format(out_path))

    dir_name = os.path.join(out_path,services)
    
    if not os.path.exists(dir_name):
        directory_created = mdir(infra, dir_name) 
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
    out_path = args['path']

    build_infraestucture(out_path, service)

    print(args) # debug

    # Build infraestucture for save output

    
    # Start progress
    service_progress = log.progress(service)

    if 'recon' == service: 
        service_progress.status("Enum with service {}".format(service))
        



#    data = json.loads(nmap_p)
#    
#    
#       
#
#    for command in data['commands']: 
#
#       run(dir_name,command)
#       time.sleep(2)


if __name__ == '__main__':
    main()
