pipeline{
    agent any 
    stages{
        stage('Get files'){
            steps{
                git branch: 'master', url: 'https://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@github.com/LouaiTayyar/SensorsAPI.git'
            }
        }
    }
}
node {
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      sh "${scannerHome}/bin/sonar-scanner"
    }
  }
