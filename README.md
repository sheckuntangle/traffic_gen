# pytraffic

Dockerized Python Web Traffic Generator For Untangle NGFW and MFW products

# Recommended Setup

Recommend configuring with 3 NIC's, one for local network (ssh access), one to connect to NGFW, and one to connect to MFW

# Pull Docker Image

docker pull container-registry.untangle.com/traffic_gen:latest

# Edit .env file

Edit the .env file in the repo to match the name of the interfaces on your device

# Copy ngfw-traffic and mfw-traffic to /usr/local/bin and make executable

cd (repo dir)
sudo chmod +x *-traffic
sudo cp *-traffic /usr/local/bin

This will allow you to run the mfw-traffic and ngfw-traffic commands to start the traffic generators.
