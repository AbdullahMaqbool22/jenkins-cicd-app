pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "abdullahmaqbool22/jenkins-cicd-app:latest"
    }
    stages {
        stage('Code Fetch Stage') {
            steps {
                git branch: 'main', url: 'https://github.com/AbdullahMaqbool22/jenkins-cicd-app.git'
            }
        }
        stage('Docker Image Creation Stage') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds', url: '']) {
                    script {
                        docker.image("${DOCKER_IMAGE}").push()
                    }
                }
            }
        }
        stage('Kubernetes Deployment Stage') {
            steps {
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/service.yaml'
                sh 'kubectl apply -f k8s/pvc.yaml'
            }
        }
        stage('Prometheus/Grafana Stage') {
            steps {
                echo 'Monitoring setup (Prometheus/Grafana) can be triggered here'
            }
        }
    }
}
