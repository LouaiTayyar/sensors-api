pipeline {
    agent any
    stages {
        stage('verify tooling') {
            steps {
                sh '''
                    docker version 
                    docker info 
                    docker compose version
                    curl --version
                '''
            }
        }
        stage('Prune Docker data') {
            steps {
                sh './clean.sh'
            }
        }
        stage('Starting containers') {
            steps {
                sh 'docker compose up -d '
                sh 'docker compose ps'
            }
        }
    }
}