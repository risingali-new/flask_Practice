# Flask Practice - CI/CD Pipeline Project

## Project Overview by Ali HUssain

This project demonstrates the implementation of Continuous Integration and Continuous Deployment (CI/CD) for a Flask web application using:

- Jenkins Pipeline
- GitHub Actions
- Pytest for automated testing

---

## Repository Structure

```
flask_Practice
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── templates/
├── app.py
├── test_app.py
├── requirements.txt
├── Jenkinsfile
├── start_flask.sh
└── README.md
```

---

# Prerequisites

- Python 3.x
- pip
- Git
- GitHub Account
- Jenkins
- Pytest

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Jenkins CI/CD Pipeline

The Jenkins pipeline is defined in the `Jenkinsfile`.

## Pipeline Stages

### 1. Checkout
Downloads the latest source code from the GitHub repository.

### 2. Build
Installs all required Python dependencies using pip.

### 3. Test
Runs automated unit tests using Pytest.

### 4. Deploy
Starts the Flask application using the `start_flask.sh` script.

### Notifications

The pipeline sends email notifications on:

- Build Success
- Build Failure

---

# GitHub Actions Workflow

The GitHub Actions workflow is located at:

```
.github/workflows/ci-cd.yml
```

## Workflow Jobs

### Build

- Checkout repository
- Setup Python
- Install dependencies

### Test

- Execute all unit tests using Pytest

### Deploy to Staging

Triggered when code is pushed to the **staging** branch.

### Deploy to Production

Triggered when a release tag is created.

---

# GitHub Secrets

The workflow uses the following repository secret:

| Secret Name | Purpose |
|-------------|---------|
| DEPLOY_KEY | Deployment authentication (dummy value for assignment) |

Configure the secret from:

```
Repository
→ Settings
→ Secrets and Variables
→ Actions
→ New Repository Secret
```

---

# Branch Strategy

- **main** → Primary development branch
- **staging** → Staging deployment branch

---

# Workflow Triggers

| Event | Action |
|--------|--------|
| Push to main | Build & Test |
| Push to staging | Build, Test & Deploy to Staging |
| Release Tag | Deploy to Production |

---

# Technologies Used

- Python
- Flask
- Jenkins
- GitHub Actions
- Git
- Pytest

---

# Submission Deliverables

- Jenkins Pipeline (Jenkinsfile)
- GitHub Actions Workflow
- Updated README
- Jenkins Pipeline Screenshots
- GitHub Actions Screenshots
- GitHub Repository URL

---

# Author

Ali Hussain
