pipeline {
    agent none 
    stages {
      stage('Hello World') {
          steps {
              echo 'Hello world!' 
          }
      }
      stage('Checkout files'){
        agent any
        steps{
          checkout scm
        }
      }
      stage('Build TEST'){
        agent any
        steps {
            sh "ls"
            sh "docker-compose up"
            echo 'Hello world!' 
        }
      }
    }
}