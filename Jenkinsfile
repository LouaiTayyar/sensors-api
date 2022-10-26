pipeline{
  agent any
  node {
    stage('Checkout Files') {
      checkout scm
    }
  }
  stages{
    stage('API') {
      agent {
        dockerfile {
            filename 'Dockerfile'
            dir 'api'
            args '-v static:/static -p 8000:8000'
        }
      }
    }
  }
}