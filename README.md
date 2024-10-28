# Jenkins Docker Pipeline Setup Guide

## Introduction

This guide provides a step-by-step approach to setting up a Jenkins pipeline for building and deploying a Dockerized application. The pipeline automates tasks such as checking for existing Docker images, cleaning up old images and containers, building new images, and deploying the application.

## Prerequisites

Before you begin, ensure you have the following:

- **Jenkins** installed and running on your server.
- **Docker** installed on the Jenkins server.
- A **GitHub** account to access the repository.

## Clone the Repository

1. Open a terminal on your Jenkins server.
2. Clone the repository:
   ```bash
   git clone https://github.com/dost0092/docker_jenkin.git
   cd docker_jenkin

## Configure Jenkins
Set Up Git Repository:

In the job configuration, scroll down to the Pipeline section.
Set the Definition to Pipeline script from SCM.
Choose Git from the SCM dropdown.
Enter your Git repository URL: https://github.com/dost0092/docker_jenkin.git.
Optionally, add credentials if your repository is private.
Specify the Script Path:

Set the Script Path to Jenkinsfile, which is located in the root of your cloned repository.


## Running the Pipeline
Access Jenkins: Open your Jenkins dashboard in a web browser.
Navigate to Your Pipeline Job: Click on the job you created earlier.
Start the Build: Click on Build Now to initiate the pipeline.
Monitor Console Output: Click on the build number in the Build History section to see the console output and monitor the progress.
