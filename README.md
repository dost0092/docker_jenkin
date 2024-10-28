# Jenkins Docker Pipeline

This repository contains a Jenkins pipeline for automating the building and deployment of Dockerized applications. The pipeline includes stages for checking for existing Docker images, cleaning up old images and containers, building new Docker images, and deploying them.

## Pipeline Diagram

![Pipeline Diagram](./pipeline.png)

## Introduction

This Jenkins pipeline is designed to streamline the process of building and deploying Docker containers. By using this pipeline, developers can ensure that their applications are always up to date and running in a consistent environment.

## Prerequisites

Before you get started, make sure you have the following installed:

- **Jenkins**: You can follow the [official installation guide](https://www.jenkins.io/doc/book/installing/) to set up Jenkins.
- **Docker**: Install Docker on your Jenkins server. Follow the [Docker installation instructions](https://docs.docker.com/get-docker/).
- **Git**: Ensure that Git is installed on the Jenkins server.


## Setup Instructions

1. **Clone the Repository**:
   Open a terminal and clone the repository using the following command:
   ```bash
   git clone https://github.com/dost0092/docker_jenkin.git
   cd docker_jenkin
Configure Jenkins:

### 1.Install Required Plugins:

Navigate to Manage Jenkins > Manage Plugins.
Install the Docker Pipeline and Git plugins.
Create a New Pipeline Job:

### 2.Click on New Item in the Jenkins dashboard.
Enter a name for your pipeline job.
Select Pipeline and click OK.
Set Up Git Repository in Jenkins:

In the pipeline job configuration, scroll down to the Pipeline section.
Set the Definition to Pipeline script from SCM.
Choose Git from the SCM dropdown.
Enter your Git repository URL: https://github.com/username/repo.git.
Specify the Script Path:

### 3.Set the Script Path to Jenkinsfile, which is located in the root of your cloned repository.
Add Jenkins User to Docker Group (if required): Run the following command to allow Jenkins to execute Docker commands:

bash
Copy code
sudo usermod -aG docker jenkins
Restart Jenkins to apply the changes.

## Pipeline Overview

The Jenkins pipeline defined in the `Jenkinsfile` includes the following stages:

- **Clone Repository**: Clones the Git repository.
- **Check for Old Docker Image**: Checks if an existing Docker image is present.
- **Clean Up Old Docker Image & Container**: Deletes old images and containers if they exist.
- **Build New Docker Image**: Builds a new Docker image from the Dockerfile.
- **Deploy New Container**: Deploys the new Docker container using the newly built image.
- **Post Actions**: Performs any necessary cleanup or notifications after the pipeline runs.

## Using the Pipeline

1. **Access Jenkins**: Open your Jenkins dashboard in a web browser.
2. **Navigate to Your Pipeline Job**: Click on the job you created earlier.
3. **Start the Build**: Click on **Build Now** to initiate the pipeline.
4. **Monitor Console Output**: Click on the build number in the **Build History** section to see the console output and monitor the progress of your build. Thanks you
5. Triggerd again
