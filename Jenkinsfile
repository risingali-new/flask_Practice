pipeline {
    agent any

    environment {
        APP_NAME = "FlaskApp"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'

                sh '''
                python3 -m pip install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running Tests...'

                sh '''
                pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying to Staging...'

                sh '''
                chmod +x start_flask.sh
                nohup ./start_flask.sh &
                '''
            }
        }
    }

    post {

        success {
            mail to: 'your-email@gmail.com',
                 subject: 'SUCCESS : Jenkins Pipeline',
                 body: 'Build Successful'
        }

        failure {
            mail to: 'risingali@gmail.com',
                 subject: 'FAILED : Jenkins Pipeline',
                 body: 'Build Failed'
        }
    }
}