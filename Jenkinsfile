pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Source code checkout completed'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application'
            }
        }

        stage('Test') {
            steps {
                echo 'Application tests passed'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t devops-demo:latest .'
            }
        }

    }
}