node {
    stages {
        stage('Verify tools') {
            sh '''
                docker version 
                docker info 
                docker compose version
                curl --version
            '''
        }
        stage('Prune Docker data') {
            sh 'docker system prune -a --volumes -f'
        }
        stage('Build Containers') {
            sh 'docker compose up -d --no-color --wait'
        }
        stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarScanner';
            withSonarQubeEnv() {
            sh "${scannerHome}/bin/sonar-scanner"
            }
        }
    }
}
