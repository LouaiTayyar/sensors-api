pipeline {
    agent any
    stages {
        stage('Verify tools') {
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
                sh 'docker system prune -a --volumes -f'
            }
        }
        stage('Build Required Images') {
            steps {
                sh 'docker compose pull'
            }
        }
        stage('Build Required Services') {
            steps {
                sh 'docker compose build'
            }
        }
        stage('Setup SonarQube') {
            steps {
                sh 'docker compose run sonarqube'
            }
        }
    }
}