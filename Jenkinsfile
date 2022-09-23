def img
pipeline {
    environment {
        registry = "leandro2m/demo-app"
        registryCredential = "docker-credentials"
    }
    agent  { dockerfile true }

    stages {
        stage('build checkout') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println ("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }
        stage ("Push to DockerHub") {
            steps {
                script {
                    docker.withRegistry("https://registry.hub.docker.com", registryCredential) {
                        dockerImage.push()
                    }
                }
            }
        }
    }
 
}
