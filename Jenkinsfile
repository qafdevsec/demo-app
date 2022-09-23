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
        stage ("Testing - running in Jenkins Node") {
            steps {
                sh "docker run -d --name ${JOB_NAME} -p 8080:8080 ${img}"
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
