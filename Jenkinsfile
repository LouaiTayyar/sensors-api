pipeline{
  agent none
  stages{
    stage('Checkout Files'){
      node {
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