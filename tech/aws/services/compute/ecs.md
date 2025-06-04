Amazon Elastic Container Service (ECS)
---

- is a `fully managed container orchestration service` that makes it `easy to deploy, run, and scale` containerized applications on AWS running Docker containers running on a `managed cluster across multiple AZs (AZs)` within an AWS region.
- supports both `rolling updates` and `blue/green` deployments using AWS `CodeDeploy`.

# Features

- Container orchestration
  - enables you to easily deploy and manage your containers across a fleet of Amazon EC2 instances.
- Auto Scaling
  - `automatically scales` your containers using Amazon `EC2 Auto Scaling` to automatically scale your EC2 instances and Docker container workloads.
- Task Definition
  - Specify the `desired state` of your containerized applications and AWS ECS or `Fargate automatically schedules tasks` to meet requirements.
- Monitoring and Logging
- Integration
  - AWS IAM
  - Amazon EC2 Auto Scaling
  - ELB Application Load Balancer
  - Amazon RDS
  - Amazon Elastic Container Registry (ECR)

# AWS ECS Task Definition

- is `a blueprint` that `describes the containers` that make up an ECS task.
- `specifies the container image, CPU and memory` requirements, networking settings, and other information needed to run a containerized application.
- The management of the container infrastructure that your tasks and services are hosted on is determined by the launch type selected

## ECS Task Definition Launch Types

### AWS Fargate launch type

- `Specify` the `container image and memory and CPU` requirements by using an ECS task definition.
- Fargate then takes over `scheduling the orchestration, management, and placement of the containers throughout the cluster`, providing a highly available operation environment.
- You can `still launch` your container environment using `manual EC2 launch patterns` using the ECS service.
- AWS Fargate with ECS can also be used to `run containers without having to manage (provision, configure, or scale) your clusters of EC2` instances.
- Applications launched by Fargate are packaged in containers with the defined CPU, memory at the task level, networking, and security policies.
- AWS Fargate `supports Amazon Linux 2 and Microsoft Windows Server 2019 and 2022` Full and Core editions.
- EKS running Kubernetes pods can be also managed by Fargate.
- Fargate `profiles control which pods use Fargate management` when launched.
- Each Fargate profile `defines the pod’s execution role, subnets` where pods will be launched, and namespace.

### EC2 Launch Type

- Run containerized applications that are hosted on a `cluster of EC2 instances that you manage`.
- `Task definitions` are created that `define the container images` that will run across your clusters.
- Direct `fine-grained control` can be run using the EC2 launch type that deploys EC2 instances in your cluster.
- ECS follows a `task placement strategy` and uses a defined task definition when launching your containers.
- For example, your strategy might be to spread the containers across multiple EC2 instances and across multiple AZs.
- Task placement strategies might include running a task per EC2 instance or running your own custom-designed tasks.
- `ECS monitors all running tasks and restarts tasks as a service restart when failure occurs`.

### External Launch Type

- `Self-managed` ECS `on-premises` deployments on an organization’s `own hardware` resources.

## ECS Task Definition must define the following criteria:

- The container image to be pulled from the private registry to create the containerized application.
- Container definitions, each of which includes the container image, the command to run when the container starts, the CPU and memory requirements, and other settings.
- The launch type to use for your task: AWS Fargate, EC2, or ECS Anywhere deployments on premises.
- The task execution role, which is the IAM role the ECS agent uses to perform tasks on your behalf.
- Links that need to be established between containers.
- Volumes, which can be used to store data that is persisted across container restarts or to share data between containers.
- Network and port settings. ECS supports several networking modes, including bridge mode, host mode, and awsvpc mode.


