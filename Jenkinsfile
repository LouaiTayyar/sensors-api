node {
  stage('Checkoutuu Files') {
    checkout scm
  }
  stage('API') {
    agent {
        // Equivalent to "docker build -f Dockerfile.build --build-arg version=1.0.2 ./build/
        dockerfile {
            filename 'Dockerfile'
            dir 'api'
            args '-v static:/static -p 8000:8000'
        }
    }
    steps{
        sh "docker ps -a"
    }
}
}
