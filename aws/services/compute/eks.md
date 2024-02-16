Amazon Elastic Kubernetes Service (EKS)
---

- can be used to `run Kubernetes at AWS` without having to install and maintain your own Kubernetes control plane.

# EKS Cluster Components

## Kubernetes Control Plane

- The EKS control plane has a `minimum of two highly available API server instances`
- EKS `automatically scales the control plane` instances based on load, detects and replaces unhealthy instances, and automatically patches and updates control plane instances.

## Cluster of EKS EC2 Instances

- EKS clusters `contain pods` that `contain one or more containers`.
- Pods can be deployed as self-managed nodes, EKS-managed node groups, or using AWS Fargate.

## API Server

- is the `primary point of interaction for users and other components` of the Kubernetes system.
- is `responsible for handling requests to create, update, and delete resources` within the cluster.

## etcd instances

- `3 etcd instances` are hosted across `3 availability zones` within each AWS region.
- `communicate with each other` to form a `distributed system` that can be used to `store and retrieve configuration data`.
- Amazon EKS is integrated with AWS services such as Amazon CloudWatch, EC2 Auto Scaling groups, IAM, and ELB Application Load Balancers.

# Amazon EKS Deployment Methods

## Amazon EKS

- Deploy `managed EKS control plane` and nodes managed by AWS.

## EKS on AWS Outposts

- AWS Outposts allows running of EKS and other AWS infrastructure services in `on-premises` locations.

## Amazon EKS Anywhere

- Deploy and manage Kubernetes clusters on premises supported by AWS using `customer hardware and VMware vSphere`.

## EKS Distro

- Deploy `open-source deployment of Kubernetes` clusters on premises using `customer hardware and customer support`.
