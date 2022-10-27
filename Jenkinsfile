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
        stage('Setup SonarQube') {
            steps {
                sh 'docker compose up -d sonarqube '
            }
        }
    }
}