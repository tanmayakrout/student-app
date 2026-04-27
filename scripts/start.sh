#!/bin/bash

echo "===== APPLICATION START PHASE ====="

cd /home/ec2-user/student-app || exit 1

# Kill any existing running app (avoid port conflict)
echo "Stopping existing app if running..."
pkill -f "python3 app.py" || true

# Start the Flask app in background
echo "Starting application..."
nohup python3 app.py > app.log 2>&1 &

# Give app few seconds to start
sleep 5

echo "===== APPLICATION STARTED ====="