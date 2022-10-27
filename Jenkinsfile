node {
    stage('SCM') {
        checkout scm
    }
    stage('Verify tools') {
        sh '''
            docker version 
            docker info 
            docker compose version
            curl --version
        '''
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
