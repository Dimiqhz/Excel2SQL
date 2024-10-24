#!/bin/bash

echo "Updating packages..."
sudo apt update -y && sudo apt upgrade -y

echo "Installing dependencies for building Python..."
sudo apt install -y software-properties-common build-essential libssl-dev zlib1g-dev \
libncurses5-dev libnss3-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

echo "Adding repository and installing Python 3.11..."
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update -y
sudo apt install -y python3.11 python3.11-venv python3.11-dev

python3.11 --version
if [ $? -ne 0 ]; then
    echo "Python 3.11 installation failed."
    exit 1
fi

echo "Installing pip for Python 3.11..."
sudo apt install -y python3-pip

python3.11 -m ensurepip --upgrade
if [ $? -ne 0 ]; then
    echo "pip installation failed. Trying manual installation..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3.11 get-pip.py
fi

echo "Creating virtual environment with Python 3.11..."
python3.11 -m venv venv

echo "Activating virtual environment and installing dependencies..."
source venv/bin/activate
pip install --upgrade pip
pip install openpyxl pandas colorama

deactivate

echo "Setup completed!"