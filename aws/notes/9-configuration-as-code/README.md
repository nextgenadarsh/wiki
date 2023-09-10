Configuration as Code
===

# Using AWS OpsWorks Stacks to Deploy Applications

## What Is AWS OpsWorks Stacks?

- lets you manage applications and servers on AWS and on-premises. With AWS OpsWorks Stacks, you can model your application as a stack that contains different layers, such as load balancing, database, and application server
- only service that performs configuration management tasks

## AWS OpsWorks Stack Concepts

### Cookbooks and Recipes

### Managing Cookbooks

### Package Cookbook Dependencies

### Stack

### Stack Name

### API Endpoint Region

### Amazon Virtual Private Cloud

### Default Operating System

### Layer

### Elastic Load Balancing

### Elastic IP Addresses

### Amazon EBS Volumes

### Amazon RDS Layer

### Amazon ECS Cluster Layer

### Chef 11.10 Built-in Layers

### Instances

#### Instance Type

##### 24/7 instances

##### Time-based instances

##### Load-based instances

### Root Device Type

### Instance Updates

### Register Instances

### AWS OpsWorks Agent

### Auto-Healing Instances

### Apps

### Users and Permissions Management

### Managing Permissions

### Managing Users

### Lifecycle Events

### Setup

### Configure

### Deploy

### Undeploy

### Shutdown

### Resource Management

### Amazon EBS Volumes

### Elastic IP Addresses

### Amazon RDS Instances

### Chef 11 and Chef 12

### Separate Chef Runs

### Community Support

### Built-in Layers

### Berkshelf

### Data Bags

### Data Bags and Custom JSON

### Monitor Instance Metrics

## AWS OpsWorks Stacks Service Limits

# Using AWS OpsWorks Stacks with AWS CodePipeline

## Deployment Best Practices

### Rolling Deployments

### Blue/Green Deployments (Separate Stacks)

### Manage Databases Between Deployments

# Using Amazon Elastic Container Service to Deploy Containers

## What Is Amazon ECS?

- a highly scalable, high-performance container orchestration service that supports Docker containers and allows you to easily run and scale containerized applications on AWS
- streamlines the process for managing and scheduling containers across fleets of Amazon EC2 instances, without the need to include separate management tools for container orchestration or cluster scaling

## AWS Fargate

- reduces management further as it deploys containers to serverless architecture and removes cluster management requirements entirely. To create a cluster and deploy services, you need only configure the resource requirements of containers and availability requirements. Amazon ECS manages the rest with the use of an agent that runs on cluster instances. AWS Fargate requires no agent management.

## Amazon ECS Concepts

### Amazon ECS Cluster

### AWS Fargate

### Containers and Images

### Task Definition

### Services

### Balance Loads

### Schedule Tasks

### Target Tracking Policies

### Step Scaling Policies

### Task Placement Strategies

### Task Placement Constraints

### Amazon ECS Service Discovery

### Private Image Repositories

### Amazon Elastic Container Repository

### Amazon ECS Container Agent

## Amazon ECS Service Limits

# Using Amazon ECS with AWS CodePipeline

