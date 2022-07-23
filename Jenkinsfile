def sc

pipeline {
    agent any
    parameters {
        string(name: 'IMAGENAME', defaultValue: 'dogworld', description: 'Image Name')
        string(name: 'IMAGETAG', defaultValue: 'latest', description: 'Image Tag')
    }

    stages {
        stage('Init') {
            steps{
                script{
                    sc = load 'script.groovy'
                }
            }
        }
        stage('Unit-Test') {
            steps {
                script {
                    sc.echo_out('Testing....')
                }
                sh '''
                   pytest --verbose ./tests
                '''
            }
        }
        stage('Build') {
            steps {
                script {
                    sc.echo_out('Building....')
                }
                sh "docker build -t ${params.IMAGENAME}:${params.IMAGETAG} ."
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sc.echo_out('Deploying....')
                }
                sh "docker rm -f ${params.IMAGENAME} || true"

                sh "docker run -p 1234:1234 -d --name ${params.IMAGENAME} ${params.IMAGENAME}:${params.IMAGETAG}"
            }
        }
    }
}