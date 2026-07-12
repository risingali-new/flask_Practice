# Flask CI/CD Pipeline Assignment

## Project Overview

This project demonstrates the implementation of a complete CI/CD pipeline for a Flask application using both Jenkins and GitHub Actions.

The project satisfies the Hero Vired CI/CD assignment requirements by automating:

- Build
- Testing
- Deployment
- Branch based deployment
- Release based deployment

---

# Technology Stack

- Python 3.11
- Flask
- Jenkins
- GitHub Actions
- Docker
- Terraform
- AWS EC2
- Git
- Pytest

---

# Project Structure

```
flask_Practice/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── templates/
├── app.py
├── test_app.py
├── requirements.txt
├── Jenkinsfile
├── README.md
└── start_flask.sh
```

---

# Jenkins CI/CD Pipeline

The Jenkins pipeline performs the following stages:

## Checkout

Clones the repository from GitHub.

## Build

- Creates Python virtual environment
- Installs dependencies

```
pip install -r requirements.txt
```

## Test

Runs unit tests using Pytest.

```
pytest
```

## Deploy

Starts the Flask application.

```
bash start_flask.sh
```

---

# Jenkins Server

Hosted on:

AWS EC2 Ubuntu 24.04

Installed using Terraform UserData.

Installed software:

- Jenkins (Docker)
- Docker
- Git
- Python
- Terraform
- AWS CLI
- kubectl
- Helm
- eksctl

---

# GitHub Actions Workflow

The workflow performs the following jobs.

## Build & Test

Runs for:

- main branch
- staging branch

Steps

- Checkout Repository
- Install Python
- Install Dependencies
- Execute Unit Tests

---

## Deploy to Staging

Automatically executes when code is pushed to:

```
staging
```

---

## Deploy to Production

Automatically executes whenever a GitHub Release is published.

Example:

```
Production Release v1.0
```

---

# Repository

GitHub Repository

```
https://github.com/risingali-new/flask_Practice
```

---

# Screenshots

## Jenkins Dashboard

<img width="1852" height="717" alt="image" src="https://github.com/user-attachments/assets/bda40e03-6494-4a07-972f-c5f890b4863b" />

## GitHub Actions Build & Test

<img width="1855" height="826" alt="image" src="https://github.com/user-attachments/assets/2b929e05-02d3-42ee-9c7d-bd030538d931" />


---

## GitHub Actions Staging Deployment

<img width="1364" height="836" alt="image" src="https://github.com/user-attachments/assets/f292d7e8-df05-4525-9f26-5c41c7af5b56" />


---

## GitHub Actions Production Deployment

<img width="1350" height="738" alt="image" src="https://github.com/user-attachments/assets/052a68c7-9318-4514-9a2d-c35936c88289" />


---

# Assignment Deliverables

✔ Jenkins Pipeline

✔ GitHub Actions Workflow

✔ Build Automation

✔ Automated Testing

✔ Staging Deployment

✔ Production Deployment

✔ README Documentation

✔ Screenshots

---

# Author

Ali Hussain

Hero Vired DevOps & Multi Cloud Architect Program
Webhook Test
