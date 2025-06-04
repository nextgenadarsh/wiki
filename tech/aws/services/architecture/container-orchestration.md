Container Orchestration
---

# Container Orchestration Options

## Amazon EKS

- Kubernetes control and data plane instances are located `across three AZs`, ensuring high availability.
- Amazon EKS `can detect and replace unhealthy` control plane instances.

## Amazon ECS

- Docker containers are deployed `across multiple AZs` within an AWS region.

## AWS Fargate

- Provision and manage containerized applications that are hosted on `either Docker or Kubernetes` deployments.

## AWS Copilot

## AWS App Runner

## AWS Lightsail

## AWS App2Container (A2C)

## AWS Elastic Beanstalk

. | AWS Service | Use Case  | Details
  --  | --  | --  | --
Container Orchestration | Amazon ECS  | Docker applications or micro-services | Hybrid deployments and scale
. | Amazon EKS  | Manage Kubernetes container deployments (applications or micro-services) | Hybrid deployments and scale
Compute Options | Fargate | Manage ECS or EKS deployments | Manage containerized applications, not infrastructure, at AWS
. | Amazon EC2 instances  | Containers with full control | Bare-metal deployments at AWS, AWS Outposts
Container Tools | AWS Copilot | Manage containerized applications | CLI controlled deployments on ECS and Fargate
. | Amazon Elastic Container Registry (ECR) | Storage and deploy containers | AWS hosted repository
. | AWS App Mesh | Hybrid application-level networking service mesh | Use with Fargate, EC2, ECS, EKS, Kubernetes, AWS Outposts
. | AWS Cloud Map | AWS cloud resource discovery service | Register AWS application resource services (databases, queues, microservices) with custom names; resource health is checked to ensure the location is up to date
. | AWS Lambda | Integrate with many AWS services with custom functions | Package Lambda functions as container applications
. | AWS App Runner | Run containerized web apps at AWS | Infrastructure and container orchestration is fully hidden
. | Amazon ECS Anywhere | Run containers on customer-managed hardware | AWS supported hybrid deployments
. | Amazon EKS Anywhere | Operate Kubernetes clusters on customer hardware | AWS supported hybrid deployments
. | AWS Proton | Self-service portal for platform team infrastructure deployment tool templates | Deploy existing infrastructure-as-code tools using CloudFormation or Terraform
. | Amazon Elastic Beanstalk | Deploy the app and AWS infrastructure | EC2 instances or Docker containers

