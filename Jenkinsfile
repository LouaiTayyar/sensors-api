pipeline {
    agent none 
    stages {
      stage('Stage 1') {
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
      stage('Build API'){
        agent {
            // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
            dockerfile {
                filename 'Dockerfile'
                dir 'api'
                label 'my-defined-label'
                args '-v /static:/static'
            }
        }
      }
    }
}