# pytraffic

Dockerized Python Web Traffic Generator For Untangle NGFW and MFW products

# Recommended Setup

Recommend configuring device with 3 NIC's, one for local network (ssh access), one to connect to NGFW, and one to connect to MFW
NOTE: if using Ubuntu 20 you will have to edit /etc/netplan/ configuration, example config shown on netplan-example.yaml file

# Make directory for logs on host

On the host device, make a directory in /home called traffic_logging, this will be used for the logs from the containers:

mkdir ~/traffic_logging

# Pull Docker Image

docker pull container-registry.untangle.com/traffic_gen:latest

# Edit .env file

Edit the .env file in the repo to match the name of the interfaces on your device

# Make logging script executable and copy to /usr/local/bin of host machine

This will allow you to run the trafficlogs command to aggregate log data and get stats from traffic. It will ask you to give a name for a folder to backup the current files in traffic_logging directory. After aggregating it moves all files into the backup directory that was created and makes a .summary file for the data report.

cd (repo dir)
sudo chmod + x trafficlogs
sudo cp trafficlogs /usr/local/bin

# Make ngfw-traffic and mfw-traffic executable and copy to /usr/local/bin oh host machine
This will allow you to run the mfw-traffic and ngfw-traffic commands to start the traffic generators. These commands will ask how many clients you would like to run and then start the clients daemonized.

cd (repo dir)
sudo chmod +x *-traffic
sudo cp *-traffic /usr/local/bin

# To stop containers that are running daemonized

docker-compose -f /path/to/repo/mfw.yml down

docker-compose -f /path/to/repo/ngfw.yml down
