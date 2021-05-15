## 

##

import json
import os
import time
import subprocess
from pwn import *
from gptools_cli import gen_cli_args
from recon import *


# Vars 

PATH="/tmp/autorecon/" # demo path
ip='127.0.0.1'
nmap_p = '{"name":"nmap", "commands":["nmap -p- --min-rate 5000 -n -oG allports", "nmap -p 21"]}' # demo check 


infra = log.progress("Build")

def mdir(dir_name):

    try:
        os.makedirs(dir_name)
    except OSError:
        infra.failure("Creation of the directory {} failed".format(dir_name))
    except: 
        infra.status("Succes")
    else: 
        infra.status("Succesfully created the directory {}".format(dir_name))
    

def run(dir_file, command):
    out = dir_file + "out.txt"
    err = dir_file + "err.txt"

    with open(out,'w+') as fout:
        with open(err,'w+') as ferr:
            
            com = command.split()
            com.append(ip)            
            
            out=subprocess.call(com,stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            output=fout.read()

            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            errors = ferr.read()

def main():
    
    args = gen_cli_args()
    
    print(args)
    
    infra.status("Building structure on {}".format(PATH))
    
#    data = json.loads(nmap_p)
#    
#    recon = log.progress("Recon")
#    recon.status("Enum with {}".format(data['name']))
#    
#    dir_name = PATH + data['name'] + "/"
#    dir_tmp = "tmp/" + data['name']
#    
#    if not os.path.exists(dir_name):
#        mdir(dir_name) 
#    
#    if not os.path.exists(dir_name):
#        mdir(dir_tmp) 
#       
#
#    for command in data['commands']: 
#
#       run(dir_name,command)
#       time.sleep(2)


if __name__ == '__main__':
    main()
