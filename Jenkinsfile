pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker build -t dogworld:latest .'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}