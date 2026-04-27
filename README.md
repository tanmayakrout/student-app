# Student Management System (SRE-Style Project)

## Overview

This is a lightweight full-stack application built using Flask and SQLite, designed with **Production Engineering / SRE principles** such as logging, monitoring, and failure handling.

## Features

* Add and view student records
* Backend built using Flask
* SQLite database integration
* HTML-based UI

## SRE / Production Engineering Features

* **Logging**: Application logs captured in `app.log`
* **Health Monitoring Endpoint**: `/health` endpoint to check application and DB status
* **Failure Simulation**: `/fail` endpoint to simulate application crash scenarios
* **Error Handling**: Graceful handling of runtime failures

## Tech Stack

* Python (Flask)
* SQLite
* HTML / CSS
* Git / GitHub

## Project Structure

student-app/
├── app.py
├── requirements.txt
├── templates/
├── static/
├── scripts/
├── .gitignore

## How to Run Locally

1. Install dependencies:
   pip install -r requirements.txt

2. Run application:
   python app.py

3. Open browser:
   http://127.0.0.1:5000

## Monitoring Endpoints

* Health Check:
  http://127.0.0.1:5000/health

* Failure Simulation:
  http://127.0.0.1:5000/fail

## Future Enhancements

* Prometheus + Grafana integration
* AWS deployment (EC2 + RDS)
* CI/CD pipeline integration

## Deployment Setup (EC2 + CodeDeploy)

### EC2 Setup

1. Launch EC2 (Amazon Linux 2)
2. Allow ports: 22 (SSH), 5000 (App)
3. Attach IAM role: `AmazonEC2RoleforAWSCodeDeploy`

### Install CodeDeploy Agent

```bash
sudo yum update -y
sudo yum install ruby -y
sudo yum install wget -y

cd /home/ec2-user
wget https://aws-codedeploy-ap-south-1.s3.ap-south-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent start
```

### Verify Agent

```bash
sudo service codedeploy-agent status
```

Expected: running

```
```

## Author

Tanmaya Kumar Rout
