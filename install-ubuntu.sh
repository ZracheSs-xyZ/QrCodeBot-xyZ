#!/bin/bash
homedir=/home/ubuntu
apppath="QrCodeBot-xyZ"
echo "Installing the requirements ... "


#appending source list required for the application 
sudo echo "deb http://archive.ubuntu.com/ubuntu bionic main universe" >> /etc/apt/sources.list
sudo echo "deb http://archive.ubuntu.com/ubuntu bionic-security main universe" >> /etc/apt/sources.list
sudo echo "deb http://archive.ubuntu.com/ubuntu bionic-updates main universe" >> /etc/apt/sources.list

echo "Updating source lists"
sudo apt update 

echo "Installing python "
sudo apt install -y python3-pip
sudo apt-get install -y libcairo2-dev libgirepository1.0-dev

echo "Updating requirements file"
cd $homedir/$apppath
pip freeze > requirements.txt

echo "Installing application requirements"
pip3 install -r requirements.txt
pip3 install discord
pip3 install qrcode
pip3 install web3
pip3 install Image
pip install pillow


sudo chown -R ubuntu:ubuntu $homedir/$apppath
