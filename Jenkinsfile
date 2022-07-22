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

                sh '''
                    docker rm -f dogworld || true

                    docker run -p 1234:1234 -d -t dogworld dogworld:latest
                '''
            }
        }
    }
}