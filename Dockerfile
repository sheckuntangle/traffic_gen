# use ubuntu:latest base image
FROM ubuntu:latest

# install needed packages 
RUN apt update && apt install python3 pip python-is-python3 wget unzip nano

# install selenium with pip
RUN pip3 install selenium

# download and install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb

# download chrome driver
RUN wget https://chromedriver.storage.googleapis.com/97.0.4692.71/chromedriver_linux64.zip

# unzip and move chrome driver

# make traffic dir
RUN mkdir traffic
