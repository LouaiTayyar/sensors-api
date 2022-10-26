node {
    stage "Hello World"

    echo 'Hello world!' 

    stage "checkout"

    checkout scm

    stage "Build Test"

    sh "pwd"
    sh "docker-compose up sensorsapi_api"
    echo 'Hello world!' 
          
}