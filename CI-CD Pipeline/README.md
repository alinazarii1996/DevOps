# CI/CD Pipeline for Microservices with Jenkins, Docker, and Kubernetes

## Overview
This project sets up a CI/CD pipeline using Jenkins, Docker, and Kubernetes. It automates the process of building Docker images, pushing them to Docker Hub, and deploying them to a Kubernetes cluster.

## Files:
- `Jenkinsfile`: The Jenkins pipeline script for automating CI/CD tasks.
- `kubernetes/deployment.yaml`: Kubernetes deployment configuration.
- `kubernetes/service.yaml`: Kubernetes service configuration for exposing the application.

## Prerequisites:
- Jenkins with Docker and Kubernetes plugin installed.
- Docker Hub account for pushing images.
- Kubernetes cluster with `kubectl` configured.

## Usage:
1. Clone the repository and configure Jenkins to use the `Jenkinsfile`.
2. The pipeline will automatically build the Docker image and deploy it to your Kubernetes cluster.

