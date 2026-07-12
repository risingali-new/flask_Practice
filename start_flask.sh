#!/bin/bash

set -e

cd "$WORKSPACE"

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

export MONGO_URI="mongodb://localhost:27017/testdb"

export SECRET_KEY="jenkins-secret"

pkill -f "python3 app.py" || true

nohup python3 app.py > flask.log 2>&1 &

echo "Flask application deployed successfully."