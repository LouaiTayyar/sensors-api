node {
    stage('Checkout SCM Files') {
        checkout scm
    }
    stage('Verify Available Tools') {
        sh '''
            docker version 
            docker info 
            docker compose version
            curl --version
        '''
    }
    stage('Prune Docker Data') {
        sh 'docker system prune -a --volumes -f'
    }
    stage('Build Services') {
        sh 'docker compose up -d'
    }
    stage('SonarQube Analysis') {
        def scannerHome = tool 'SonarScanner';
        withSonarQubeEnv() {
        sh "${scannerHome}/bin/sonar-scanner -X"
        }
    }
    stage('Run Unit Tests') {
        sh 'docker exec -i sensorsapi_api python3 manage.py test'
    }
    stage('Deploy Heroku') {
        sh './deploy-heroku.sh'
    }
}
