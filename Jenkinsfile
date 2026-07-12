pipeline {

    agent any

    environment {
        VENV = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {

                sh '''

                python3 -m venv $VENV

                . $VENV/bin/activate

                pip install -r requirements.txt

                '''

            }
        }

        stage('Test') {
            steps {

                sh '''

                . $VENV/bin/activate

                pytest test_app.py

                '''

            }
        }

        stage('Deploy') {
            steps {

                sh '''

                chmod +x start_flask.sh

                ./start_flask.sh

                '''

            }
        }
    }

    post {

        success {
            echo "Pipeline completed successfully."
        }

        failure {
            echo "Pipeline failed."
        }

        always {
            cleanWs()
        }

    }

}