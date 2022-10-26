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
        steps {
            sh "docker-compose up"
            echo 'Hello world!' 
        }
      }
      stage('Build API'){
        agent {
            // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
            dockerfile {
                filename 'Dockerfile'
                dir 'api'
                additionalBuildArgs  '--build-arg version=1.0.2'
                args '-v /static:/static -t api'
            }
        }
        steps {
          echo 'Hello world!' 
        }
      }
    }
}