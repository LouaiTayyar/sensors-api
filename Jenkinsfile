node {
    stage('Checkout SCM Files') {
        checkout scm
    }
    stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv('SonarCloud') { // If you have configured more than one global server connection, you can specify its name
      sh "${scannerHome}/bin/sonar-scanner"
    }
    }
    stage('Verify Available Tools') {
        sh '''
            docker version 
            docker info 
            docker compose version
            curl --version
        '''
    }
    stage('Build Database') {
        sh 'docker compose up -d db --no-color --wait'
    }
    stage('Deploy API') {
        sh 'docker compose up -d api --no-color --wait'
    }
    stage('Run Unit Tests') {
        sh 'docker exec -i sensorsapi_api python3 manage.py test'
    }
}
