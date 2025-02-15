#!/bin/bash

# 1. Initialize Terraform workspace
echo "Initializing Terraform workspace..."
terraform init

# 2. Validate Terraform configuration
echo "Validating Terraform configuration..."
terraform validate

# 3. Plan infrastructure changes
echo "Planning infrastructure deployment..."
terraform plan -out=tfplan

# 4. Apply infrastructure changes to AWS
echo "Applying infrastructure changes to AWS..."
terraform apply "tfplan"

# 5. Provision EC2 instances using Ansible
echo "Provisioning EC2 instances with Ansible..."

# Step 5.1: Define the Ansible inventory file
cat <<EOF > inventory
[aws_instances]
ec2-instance ansible_host=<EC2_PUBLIC_IP> ansible_ssh_private_key_file=~/.ssh/my-key.pem
EOF

# Step 5.2: Run the Ansible playbook to install Docker and NGINX
ansible-playbook -i inventory setup_ec2.yml

echo "Cloud infrastructure successfully deployed!"

