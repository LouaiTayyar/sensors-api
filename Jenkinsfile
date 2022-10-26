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
              additionalBuildArgs  '--entrypoint='''
              args '-v static:/static'
          }
      }
      steps{
        sh "echo hello"
      }
    }
  }
}