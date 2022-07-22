def sc

pipeline {
    agent any

    stages {
        stage('init') {
            steps{
                sc = load 'script.groovy'
            }
        }
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
                script {
                    sc.echo_out('Deploying....')
                    sc.docker_deploy()
                }
            }
        }
    }
}