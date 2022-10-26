pipeline {
    agent any 
    stages {
      stage('Hello World') {
          steps {
              echo 'Hello world!' 
          }
      }
      stage('Checkout files'){
        steps{
          checkout scm
        }
      }
      stage('Build TEST'){
        steps {
            sh "ls"
            sh "docker-compose up --build"
            echo 'Hello world!' 
        }
      }
    }
}