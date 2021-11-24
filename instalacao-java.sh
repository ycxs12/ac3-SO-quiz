#!/bin/bash

java -version
if [ $? -eq 0 ]
then
echo \"java já instalado\"
else
echo \"java não instalado\"
echo \"gostaria de instalar o java? S/n \"
read inst
if [ \"$inst\" == \"s\" ]
then
echo \"voce escolheu instalar o java\"
apt-get update -y
clear
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt install openjdk-11-jre-headless
else echo \"voce escolheu não instalar\"
fi
fi