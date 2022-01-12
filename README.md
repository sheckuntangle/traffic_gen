# pytraffic

Dockerized Python Web Traffic Generator For Untangle NGFW and MFW products

# Recommended Setup

Recommend configuring device with 3 NIC's, one for local network (ssh access), one to connect to NGFW, and one to connect to MFW

NOTE: if using Ubuntu 20 you will have to edit /etc/netplan/ configuration, example config shown on netplan-example.yaml file

# Pull Docker Image

docker pull container-registry.untangle.com/traffic_gen:latest

# Edit .env file

Edit the .env file in the repo to match the name of the interfaces on your device

# Copy ngfw-traffic and mfw-traffic to /usr/local/bin and make executable

cd (repo dir)

sudo chmod +x *-traffic

sudo cp *-traffic /usr/local/bin

This will allow you to run the mfw-traffic and ngfw-traffic commands to start the traffic generators.

# To stop containers that are running daemonized

docker-compose -f /path/to/repo/mfw.yml down

docker-compose -f /path/to/repo/ngfw.yml down