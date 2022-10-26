pipeline {
    agent none 
    stages {
      agent {
        stage('Checkout files'){
          steps{
            checkout scm
          }
      }
      }
      stage('Stage 1') {
          steps {
              echo 'Hello world!' 
          }
      }
    }
}