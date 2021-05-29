# GPenT0ols


The origin of this project is due to the end-of-degree project. My goal is to share my methodology to perform a pentesting attack and others can use it to improve theirs and add content.

When you start a project you look for precision, but I think the most important thing for me is how you do it.
It's how you do it. My main goal is to enjoy learning about this subject as much as possible.

Searching I found a very powerful, open source framework for Red and Blue Team.CALDERA, It is built on the MITRE ATT&CK™ framework and is an active research project at MITRE.

Finally I decided to create my own tool that would allow me to automate the entire first phase of enumeration in a Pentest. My tool was inspired by two tools: [Crackmapexec](https://github.com/byt3bl33d3r/CrackMapExec) and [autorecon](https://github.com/Tib3rius/AutoRecon). I may later convert it into a tool that uses MITRE ATT&CK techniques. 

Currently being a project of a few hours I have only managed to create a beta phase, being my first project as a developer there are many improvements to make so I keep it as a beta phase.

## Quick install (Docker) - Recommended
### Requeriments
- [x] [docker](https://docs.docker.com/get-docker/)

### Build

```bash
docker build -t capitanj4ck/gpent0ols .
```

### Run 
I recomend add alias in your zshrc or bashrc

```bash 
alias gpt="docker run --rm -it -v /tmp/gpt_report:/tmp/gpt_report capitanj4ck/gpent0ols"
```

## Install 
With that install you must exec command in abolute path you can't add symbolik link yet. 

### Requeriments
- [x] python3
- [x] pip3

#### install requeriments
```bash
apt-get update && \
        apt-get install -y \
    python3 \
    python3-pip \
    git \
    nmap \
    masscan \
    smbmap \
    whatweb \
    snmp \
    wget \
    nbtscan \
    wpscan \
    enum4linux \ 
    nikto \
    ffuf \
    golang \
    python3-venv \
    crackmapexec \
    seclists 
```


### Download 

```bash
git clone https://github.com/Th3FirstAvenger/GPenT0ols.git 
```

### Install requeriments

```bash
pip3 install -r requeriments.txt
```

## Usage
```
usage: AutoGPenT0ols.py [-h] [-t THREADS] [--verbose] [--show-commands] [--path PATH] {recon,web,smtp,smb,ftp,ldap,snmp} ...

                           #                                                 
                           ##                                ###             
  ###### #######  ######## ###  ## ######## ####### #######  ###         ####
 ###           ##          #### ##    ###   ##   ##       ## ###        ###  
 ###  ##  ######   ####### #######    ###   ##   ##  ##   ## ###        ###  
 ###  ##  ###      ###     ### ###    ###   ##   ##  ##   ## ###        ###  
  ######  ###      ####### ###  ##    ###   #######   #####  ####### #####   
                                 #                                           

                                 Version: 0.1
                                 Codename: CapitanJ4ck

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS            set how many concurrent threads to use (default: 100)
  --verbose             enable verbose output
  --show-commands       Just check commands 
  --path PATH           Destination path (default: /tmp/gpt_report)

services:
  available options

  {recon,web,smtp,smb,ftp,ldap,snmp}
    recon               Initial recon
    web                 Web server scanner
    smtp                smtp enumeration
    smb                 Enum smb
    ftp                 FTP enum
    ldap                LDAP enum
    snmp                Enum SNMP

We are in... Let the hacking begin!
```








