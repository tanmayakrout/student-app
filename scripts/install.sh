#!/bin/bash
set -e

sudo chown -R ec2-user:ec2-user /home/ec2-user/student-app

echo "===== INSTALL PHASE STARTED ====="

# Navigate to app directory
cd /home/ec2-user/student-app

# Install Python3 if not present
echo "Installing Python3..."
sudo dnf install -y python3

# Install pip3 (THIS was missing)
echo "Installing pip3..."
sudo dnf install -y python3-pip

# Verify installations
echo "Checking Python..."
python3 --version

echo "Checking pip..."
pip3 --version

# Upgrade pip
echo "Upgrading pip..."
python3 -m pip install --upgrade pip

# Install dependencies
echo "Installing requirements..."
pip3 install --user -r requirements.txt

echo "===== INSTALL PHASE COMPLETED ====="