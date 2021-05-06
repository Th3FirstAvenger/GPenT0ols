FROM python


RUN apt-get update && \
	apt-get install -y git nmap snmp wget nbtscan

RUN git clone https://github.com/Th3FirstAvenger/GPenT0ols.git GPenT0ols

WORKDIR /GPenT0ols

RUN pip install -r requirements.txt 

ENTRYPOINT ["GPenT0ols"]
