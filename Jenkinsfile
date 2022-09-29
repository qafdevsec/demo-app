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
                withKubeConfig(caCertificate: '''-----BEGIN CERTIFICATE-----
                MIIC5zCCAc+gAwIBAgIBADANBgkqhkiG9w0BAQsFADAVMRMwEQYDVQQDEwprdWJl
                cm5ldGVzMB4XDTIyMDUxOTIzMDcyMVoXDTMyMDUxNjIzMDcyMVowFTETMBEGA1UE
                AxMKa3ViZXJuZXRlczCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAORt
                dhw7ypOWsJhKs6c8ItrfmB+zS4TSeGKpfiBOJZEMvNPu/U8xD0WPoD07Qo/Ho4QN
                RvWQd+/rhDBKn8X/ZijmSLG101361yLJrQPKmg1q/skPmFSZgzRS9SAMMXpWKJTm
                1wVYTIMQ2oPzr9u7ENorULUSb1YwS5bKcjC5XD9ggefUcmpXF52Zxi0I1yhRtygd
                G6gjyWAkZv4OnNsJrv7nnxbfFjPu/4I5BCQhkptfMfIYeFxuyeSIn4I5AeD4apo6
                Y9KxHsJSaJMA6LsAkiX3vP+P8kXYXjLXWNGaWuyrl7I+uLCw2CB8nxhCYbJYBiPM
                weNn6VUkeoQSYLaPzWUCAwEAAaNCMEAwDgYDVR0PAQH/BAQDAgKkMA8GA1UdEwEB
                /wQFMAMBAf8wHQYDVR0OBBYEFNlV+m73gL+aq1FjJA6qBTQyIJP/MA0GCSqGSIb3
                DQEBCwUAA4IBAQC3JGBK2xfSY+zjgZ0WxJQrFDTmJjGc0OZ1dPW0M6cvausrYdhM
                SSXdI2nnIcKMa3bEu3zzPBCJ/y6pEwElD9P0CD/rdjvFAcaZFKvKCdJthZgqFcui
                U5dATLeGIRIGVWDUrh2WfOrlu5l77cUphH7Ry85gk4MCQ0PpbnbGEa+q6zu9JpI+
                3i4qFkNYf+XXzdTS1ef9T4bQ86iZfevitjrKj8cXTGYWkr+8kfEyURGBnVCvahrw
                QEdUpEp9yQCgzfmVkK6c6udshL3Abmsbs3pdAjO2EPq9kOvpE3qkzxcYhNeRPRDx
                0ToxmD8/hyVnXo6S4o8TRWcVyCP75P0HxIGm
                -----END CERTIFICATE-----''', clusterName: '', contextName: '', credentialsId: 'TOKEN', namespace: '', serverUrl: 'https://66D62BCF34D97646559FCF504C2CF223.gr7.us-east-1.eks.amazonaws.com') {
                kubeclt get pods
                }
        }

    }
}