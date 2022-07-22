def sc

pipeline {
    agent any

    stages {
        stage('init') {
            steps{
                script{
                    sc = load 'script.groovy'
                }
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t dogworld:latest .'
            }
        }
        stage('Test') {
            steps {
                script {
                    sc.echo_out('Testing..')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sc.echo_out('Deploying....')
                }
                sh '''
                    docker rm -f dogworld || true

                    docker run -p 1234:1234 -d --name dogworld dogworld:latest
                
                '''
            }
        }
    }
}