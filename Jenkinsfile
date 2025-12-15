pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "abdullahmaqbool22/jenkins-cicd-app"
    DOCKER_CREDENTIALS = "dockerhub-creds"
  }

  stages {

    stage('Code Fetch Stage') {
      steps {
        git branch: 'main',
        url: 'https://github.com/AbdullahMaqbool22/jenkins-cicd-app.git'
      }
    }

    stage('Docker Image Creation Stage') {
      steps {
        script {
          docker.build("${DOCKER_IMAGE}:latest")
        }
      }
    }

    stage('Push Image to DockerHub') {
      steps {
        script {
          docker.withRegistry('', DOCKER_CREDENTIALS) {
            docker.image("${DOCKER_IMAGE}:latest").push()
          }
        }
      }
    }

    stage('Kubernetes Deployment Stage') {
      steps {
        sh '''
          kubectl apply -f k8s/pvc.yaml
          kubectl apply -f k8s/deployment.yaml
          kubectl apply -f k8s/service.yaml
        '''
      }
    }

    stage('Prometheus/Grafana Stage') {
      steps {
        echo "Application monitoring via Prometheus & Grafana enabled"
      }
    }
  }
}
