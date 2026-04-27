#!/bin/bash

echo "Checking if app is running..."

curl -f http://localhost:5000 || exit 1