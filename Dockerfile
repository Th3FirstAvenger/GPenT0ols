FROM python


RUN apt-get update && \
	apt-get install -y git nmap snmp wget nbtscan

RUN git clone https://github.com/Th3FirstAvenger/GPenT0ols.git GPenT0ols

WORKDIR /GPenT0ols

RUN pip install -r requirements.txt && python setup.py install

ENTRYPOINT ["GPenT0ols"]
