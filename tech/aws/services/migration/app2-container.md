AWS App2 Container (A2C)
---

- `transforms` existing applications running `on-premises VMs or EC2 instances into containers`. 
- Applications supported include: 
  - `ASP.NET web apps` running on Windows
  - `Java applications` running on Linux JBoss and Apache Tomcat

- A2C can create the containers using the following AWS services:
  - ECS task definitions and Kubernetes deployment YAML files for integration with Amazon Elastic Container Registry, Elastic Container Service, and Elastic Kubernetes Service.
  - CloudFormation templates to configure the required compute, network, and security infrastructure for the deployed containerized applications.
  - Continuous integration/continuous delivery (CI/CD) pipelines for Amazon CodeBuild and CodeDeploy for building and deploying container builds.
