pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask-city-api"          // Define Docker image name
        DOCKER_CONTAINER_NAME = "cityapi"         // Define Docker container name
        REPO_URL = "https://github.com/dost0092/docker_jenkin.git"  // GitHub repository URL
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Check for Old Docker Image') {
            steps {
                script {
                    // Check if the old Docker image exists
                    def imageExists = sh(script: "docker images -q ${DOCKER_IMAGE}", returnStatus: true) == 0

                    if (imageExists) {
                        echo "Old Docker image '${DOCKER_IMAGE}' exists. Cleaning up..."
                    } else {
                        echo "No old Docker image '${DOCKER_IMAGE}' found. Proceeding to build new image..."
                    }
                }
            }
        }

        stage('Clean Up Old Docker Image & Container') {
            when {
                expression { 
                    // Proceed only if the old image exists
                    sh(script: "docker images -q ${DOCKER_IMAGE}", returnStatus: true) == 0 
                }
            }
            steps {
                script {
                    // Stop and remove old container if it exists
                    bat "docker stop ${DOCKER_CONTAINER_NAME} || exit 0"
                    bat "docker rm ${DOCKER_CONTAINER_NAME} || exit 0"

                    // Remove old Docker image
                    bat "docker rmi ${DOCKER_IMAGE} || exit 0"
                }
            }
        }

        stage('Build New Docker Image') {
            steps {
                script {
                    // Build new Docker image
                    bat "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('Deploy New Container') {
            steps {
                script {
                    // Run the new Docker container
                    bat "docker run -d --name ${DOCKER_CONTAINER_NAME} -p 3000:5000 ${DOCKER_IMAGE}"
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
