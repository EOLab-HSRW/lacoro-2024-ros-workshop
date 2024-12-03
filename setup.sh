#!/bin/bash

# install apptainer.
# reference docs: https://apptainer.org/docs/admin/main/installation.html#install-ubuntu-packages
sudo apt-get update
sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:apptainer/ppa
sudo apt update
sudo apt install -y apptainer apptainer-suid
