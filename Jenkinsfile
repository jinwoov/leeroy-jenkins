def sc

pipeline {
    agent any
    parameters {
        string(name: 'IMAGENAME', defaultValue: 'dogworld', description: 'Image Name')
        string(name: 'IMAGETAG', defaultValue: 'latest', description: 'Image Tag')
        string(name: 'IMAGEPORT', defaultValue: '1234', description: 'Port')
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
                sh pytest --verbose ./tests
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

                sh "docker run -p ${params.IMAGEPORT}:${params.IMAGEPORT} -d --name ${params.IMAGENAME} ${params.IMAGENAME}:${params.IMAGETAG}"
            }
        }

        stage('Smoke Test') {
            agent { docker 'newman' }
            steps {
                script {
                    sc.echo_out('Smoke Testing....')
                }
                sh """
                    cd smoke-tests
                    newman run dogworld.postman_collection.json --environment dogworld_env.postman_environment.json
                """
            }
        }
    }
}