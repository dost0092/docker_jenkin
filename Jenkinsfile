pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-city-api"     // Define Docker image name
        DOCKER_CONTAINER_NAME = "cityapi"         // Define Docker container name
        REPO_URL = "https://github.com/dost0092/docker_jenkin.git"  // GitHub repository URL
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Clean Up Old Docker Image & Container') {
            steps {
                script {
                    // Stop and remove old container if it exists
                    sh "docker stop ${DOCKER_CONTAINER_NAME} || true"
                    sh "docker rm ${DOCKER_CONTAINER_NAME} || true"

                    // Remove old Docker image
                    sh "docker rmi ${DOCKER_IMAGE} || true"
                }
            }
        }

        stage('Build New Docker Image') {
            steps {
                script {
                    // Build new Docker image
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Deploy New Container') {
            steps {
                script {
                    // Run the new Docker container
                    sh "docker run -d --name ${DOCKER_CONTAINER_NAME} -p 80:80 ${DOCKER_IMAGE}"
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment succeeded!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
