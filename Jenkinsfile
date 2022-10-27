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
        stage('Build Containers') {
            steps {
                sh 'docker compose up -d --no-color --wait'
            }
        }
    }
}
