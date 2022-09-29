pipeline {
    environment {
        registry = "leandro2m/demo-app"
        registryCredential = "leandro2m"
    }
    agent  any

    stages {
        // stage('SAST') {
        //     steps {
        //         script {
        //             sh '''env | grep -E "JENKINS_HOME|BUILD_ID|GIT_BRANCH|GIT_COMMIT" > /tmp/env
        //                 docker pull registry.fortidevsec.forticloud.com/fdevsec_sast:latest
        //                 docker run --rm --env-file /tmp/env --mount type=bind,source=$PWD,target=/scan registry.fortidevsec.forticloud.com/fdevsec_sast:latest'''
        //         }
        //     }
        // }
        stage('Build') {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println ("${img}")
                    println ("${registryCredential}")
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
        stage ("List Pods") {
            steps {
                sh 'curl -o kubectl https://s3.us-west-2.amazonaws.com/amazon-eks/1.23.7/2022-06-29/bin/linux/amd64/kubectl'
                sh 'chmod +x ./kubectl'
                sh 'kubectl version --short --client'
                }
        }

    }
}