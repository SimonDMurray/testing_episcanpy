ARG ubuntu_version=18.04

FROM ubuntu:$ubuntu_version

ENV DEBIAN_FRONTEND=noninteractive 

RUN apt-get update && apt-get install -y cmake 

RUN set -xe \
    && apt-get -y update \
    && apt-get -y install python3 \
    && apt-get -y install python3-dev \
    && apt-get -y install python3-pip 

RUN pip3 install --upgrade pip

RUN pip3 install --upgrade --no-cache \
	epiScanpy \
	MulticoreTSNE \
	python-igraph \
	louvain leidenalg 
