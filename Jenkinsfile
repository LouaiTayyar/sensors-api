node {
    stage "Hello World"

    echo 'Hello world!' 

    stage "checkout"

    checkout scm

    stage "Build Test"

    sh "docker-compose up"
          
}