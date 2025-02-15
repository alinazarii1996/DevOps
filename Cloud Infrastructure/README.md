# Automated Cloud Infrastructure Setup with Terraform and Ansible

## Overview
This project automates the deployment of cloud infrastructure using Terraform and Ansible. It provisions EC2 instances, configures them with Docker and NGINX, and ensures that the infrastructure is easily scalable.

## Files:
- `setup_infrastructure.sh`: A shell script that automates the Terraform setup and deployment process.
- `setup_ec2.yml`: An Ansible playbook for provisioning and configuring EC2 instances.

## Prerequisites:
- Terraform
- Ansible
- AWS CLI with configured credentials

## Usage:
1. Run the `setup_infrastructure.sh` script to initialize and apply the Terraform configuration.
2. The script will also configure EC2 instances using the `setup_ec2.yml` Ansible playbook.

