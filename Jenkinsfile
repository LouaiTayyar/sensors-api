pipeline{
  agent any
  stages{
    stage('Checkout Files'){
      steps{
          checkout scm
      }
    }
    stage('API') {
      agent {
        dockerfile {
            filename 'Dockerfile'
            dir 'api'
            args '-v static:/static -p 8000:8000'
        }
      }
      steps{
        sh "echo hello"
      }
    }
  }
}