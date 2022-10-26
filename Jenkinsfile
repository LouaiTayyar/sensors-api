node {
    stage "Hello World"

    echo 'Hello world!' 

    stage "checkout"

    checkout scm

    stage "Build Test"

    sh "cd /var/jenkins_home/workspace/SensorsAPI@temp"
    sh "docker-compose up sensorsapi_api"
    echo 'Hello world!' 
          
}