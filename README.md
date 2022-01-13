# pytraffic

Dockerized Python Web Traffic Generator For Untangle NGFW and MFW products

# Recommended Setup

Recommend configuring device with 3 NIC's, one for local network (ssh access), one to connect to NGFW, and one to connect to MFW
NOTE: if using Ubuntu 20 you will have to edit /etc/netplan/ configuration, example config shown on netplan-example.yaml file

# Make directory for logs on host

On the host device, make a directory called traffic_logging, this will be used for the logs from the containers:

ex:
mkdir ~/traffic_logging

# Pull Docker Image

docker pull container-registry.untangle.com/traffic_gen:latest

# Edit .env file

Edit the .env file in the repo to match the name of the interfaces on your device.

# Create trafficlogs, ngfw-traffic, and mfw-traffic commands

This will create a symlink for trafficlogs, ngfw-traffic, and mfw-traffic commands to /usr/local/bin and make them executable so they can run as commands on the host. 

The following commands need to be run from the repo directory:

sudo chmod +x commands.sh
./commands.sh

# Usage

This command will ask how many clients and create the containers
ngfw-traffic 

# To stop containers that are running daemonized

docker-compose -f /path/to/repo/mfw.yml down

docker-compose -f /path/to/repo/ngfw.yml down
