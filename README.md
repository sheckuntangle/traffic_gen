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

Edit the .env file in the repo to match the name of the interfaces on your device. Also add the path to your logging directory.

# Create trafficlogs, ngfw-traffic, and mfw-traffic commands

This will create a symlink for trafficlogs, ngfw-traffic, and mfw-traffic commands to /usr/local/bin and make them executable so they can run as commands on the host. ngfw-traffic and mfw-traffic commands assume that your repo is in /home, i.e ~/traffic_gen, if not you will need to edit these files and change the repo path in the docker-compose commaand.

The following commands need to be run from the repo directory:

sudo chmod +x commands.sh
sudo ./commands.sh

If you need to edit:
sudo nano /usr/local/bin/mfw-traffic
sudo nano /usr/local/bin/ngfw-traffic

# Usage

These command will ask how many clients and create the containers:
ngfw-traffic
mfw-traffic

This command will ask for name to create a folder, aggregate the logs, show stats, create a summary, and backup the logs in that folder:
trafficlogs

# To run containers manually

replace the /path/to/repo with your repo location and X with amount of clients you want to run

docker-compose -f /path/to/repo/mfw.yml up --scale mfw-traffic=X
docker-compose -f /path/to/repo/ngfw.yml up --scale ngfw-traffic=X

# To stop containers that are running daemonized

docker-compose -f /path/to/repo/mfw.yml down
docker-compose -f /path/to/repo/ngfw.yml down
