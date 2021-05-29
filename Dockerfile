FROM kalilinux/kali

RUN mkdir -p /opt/tools/{recon,smb,web}

RUN apt-get update && \
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

RUN git clone https://github.com/Th3FirstAvenger/GPenT0ols.git GPenT0ols

WORKDIR /GPenT0ols/scripts/AutoGPenT0ols

RUN pip install -r ../../requirements.txt 

ENTRYPOINT ["python3", "AutoGPenT0ols.py"]
