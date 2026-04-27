#!/bin/bash

echo "===== INSTALL PHASE STARTED ====="

# Navigate to app directory
cd /home/ec2-user/student-app || exit 1

# Ensure Python3 and pip are available
echo "Checking Python..."
python3 --version || exit 1

echo "Checking pip..."
pip3 --version || exit 1

# Upgrade pip
echo "Upgrading pip..."
pip3 install --upgrade pip

# Install dependencies
echo "Installing requirements..."
pip3 install -r requirements.txt || exit 1

echo "===== INSTALL PHASE COMPLETED ====="