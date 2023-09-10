Deployment
=======

# Phases of the Release Lifecycle

![Major phases of the release lifecycle](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c06f001.jpg)

## Source Phase

- Developers check changes into a source code repository

## Build Phase

- An application’s source code is built, and the quality of the code is tested on the build machine

## Test Phase

- Perform tests that cannot be done during the Build phase and that require the software to be deployed to production-like stages. Often, these tests include testing integration with other live systems, load testing, user interface (UI) testing, and penetration testing

## Deployment Phase

- Code is deployed to production

## Monitor Phase

- You must check the application to detect unusual activities and errors quickly.

# Environment Variables

- Ideal test environment matches the production environment exactly, providing the capability to test an application as if it were running in production and to receive accurate results.

# Software Development Lifecycle with AWS Cloud

# Continuous Integration/Continuous Deployment

- Continuous integration (CI) is the software development practice in which you continuously integrate (or check in) all code changes into a main branch of a central repository.
- Continuous delivery (CD) is the software development practice in which all code changes are automatically prepared and always deployable (ready to go into production) at a single step.
- Continuous deployment extends continuous delivery and is the automated release of software to customers, from check-in through production, without human intervention.
- The CI/CD pipeline helps developers implement continuous builds, tests, and code deployments with multiple AWS resources and a continuous integration server.
- You can integrate AWS Elastic Beanstalk with the CI/CD pipeline as one of the deployment resources.
- Use AWS CodeCommit as a CI/CD resource paired with a Git repository, from which Elastic Beanstalk can extract and deploy code.

# AWS Code Services

![AWS Code services](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c06f003.jpg)

## AWS CodePipeline

- A service for fast and reliable application updates.
- You can model and visualize the software release process. 
- To build, test, and deploy your code every time there is a code change, integrate this service with third-party tools and AWS.

## AWS CodeCommit
- A secure, highly scalable, managed source-control service that hosts private Git repositories
- Enables you to `store and manage assets` (such as documents, source code, and binary files) `privately` in the AWS Cloud.

## AWS CodeBuild

- `Compiles` source code, runs `tests`, and produces ready-to-deploy software `packages`. There is no need to manage build servers.

## AWS CodeDeploy

- Automates code `deployments` to any instance
- Handles the complexity of updating your applications, which avoids downtime during application deployment
- Deploys to Amazon EC2 or on-premises servers, in any language and on any operating system.
- It also integrates with third-party tools and AWS.

# Deploying Highly Available and Scalable Applications

## Elastic Load Balancing (ELB)

- Supports three types of load balancers:

### Application Load Balancers

- Operates at the request level (Layer 7) to route HTTP/HTTPS traffic
- Ideal for advanced load balancing of HTTP and HTTPS traffic

### Network Load Balancers

- Operates at the connection level (Layer 4) to route TCP traffic
- Best option for load balancing of `TCP traffic` because it’s capable of handling `millions of requests per second`
- Optimized to handle sudden and volatile traffic patterns while using a `single static IP` address per `AZ`
- Integrated with Auto Scaling, ECS, CloudFormation

### Classic Load Balancers

- `Basic load balancing` across multiple EC2 instances
- Operates at `both` the `request` level and the `connection` level
- Intended for applications that were built within the `EC2-Classic` network

# Deploying and Maintaining Applications

![Deployment and maintenance services](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c06f005.jpg)

## Elastic Beanstalk

- You do not have to worry about managing the infrastructure for your application
- EB Takes care of scaling and managing your application

## OpsWorks

- A `configuration` and `deployment management` tool for `Chef` or `Puppet` resource stacks
- OpsWorks for Chef Automate enables you to manage the lifecycle of your application in layers with Chef recipes

## CloudFormation

- `Template-based` Infrastructure as code (`IaC`) tool
- Helps you `model and set up AWS resources` so that you can spend less time managing them

# Automatically Adjust Capacity

## Auto Scaling

- Monitor the AWS resources that are part of your application
- Automatically adjusts capacity to maintain steady, predictable performance
- Gives recommendations that allow you to optimize performance, costs, or balance between them

## Auto Scaling Groups

- contains a collection of Amazon EC2 instances that share similar characteristics.
- Use to to scale the number of instances automatically based on criteria that you specify or maintain a fixed number of instances
- use scaling policies to increase or decrease the number of instances in your group dynamically to meet changing conditions

# AWS Elastic Beanstalk

- use to deploy applications, services, and architecture
- It provides provisioned scalability, load balancing, and high availability.
- enables the automated deployments and management of applications on the AWS Cloud
- can launch AWS resources automatically with Route 53, Auto Scaling, Elastic Load Balancing, Amazon EC2, and RDS instances
- it allows you to customize additional AWS resources

## Components

- Environments
- Application versions
- Environment configurations

## Permission Model

- Service role
- Instance profile

![AWS Elastic Beanstalk underlying technologies](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c06f006.jpg)

## Implementation Responsibilities

![ AWS Elastic Beanstalk responsibilities](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c06f007.jpg)

### Developer Teams

- build full-stack environments for web and worker tiers

### Elastic Beanstalk Responsibilities

- provisions the necessary infrastructure resources, such as the load balancer, Auto Scaling group, security groups, and database (optional)
- Provides a unique domain name for your application

## Working with Your Source Repository

- You can use AWS CodeCommit as a source control system to retrieve source code
- use the IAM role to grant Elastic Beanstalk access to all services

## Concepts

### Application

- a logical collection of environment variables and components, application versions, and environment configurations.

### Application Versions

- iterations of the application’s deployable code.
- point to an Amazon S3 object with the code source package

### Environment

- a separate version of the application, and that version’s AWS Cloud components deploy onto AWS resources to support that version.
- Each environment runs one application version at a time, but you can run multiple environments, with the same application on each, along with its own customizations and resources.

### Environment Tier

- To launch an environment, you must first choose an environment tier

### Environment Configuration

- saves to a configuration template exclusive to each environment 

### Docker Containers

- You can also use Docker containers with Elastic Beanstalk to run your applications from a container

### AWS Elastic Beanstalk Command Line Interface

- Elastic Beanstalk has its own command line interface separate from the AWS CLI tool

## Integrating with Other AWS Services

- Elastic Beanstalk automatically integrates or manages other AWS services with application code to provision efficient working environments.

### S3

- Use S3 to store static content you want to integrate with your application and point directly to objects you store in Amazon S3

### CloudFront

- provides content delivery and distribution through the use of edge locations
- To identify the source of your content in Amazon CloudFront, you can use URL path patterns to cache your content and then retrieve it from the cache

### AWS Config

- visualize configuration history and how configurations evolve over time
- customize AWS Config to record changes per resource, per region, or globally

### Amazon RDS

### Amazon ElastiCache

## AWS Identity and Access Management Roles

- enable access to the services you require to run your architecture
- a default service role and instance profile are created for you through the service API

## Deployment Strategies

- A deployment is the process of copying content and executing scripts on instances in your deployment group

### All-at-Once and In-Place Deployments

- applies updates to all your instances at once
- CodeDeploy stops currently running applications on the target instance, deploys the latest revision, restarts applications, and validates successful deployment

### Rolling Deployments

- applies changes to all of your instances by rolling the updates from one instance to another
- reduces possible downtime during implementation of the change and allows available instances to run while you deploy.
- If the rolling update fails, the service begins another rolling update for a rollback to the previous configuration.
- By using Rolling with additional batch, you can launch a new batch of instances before you begin to take instances out of service for your rolling updates

### Blue/Green Deployment

- your newer environment will be separate from your existing environment
- `running production` environment is considered the `blue` environment, and the `newer environment` with your update is considered the `green` environment
- swap the CNAMEs of the environments to redirect traffic to the newer green environment after testing

### Immutable Deployment

- best when an environment requires a total replacement of instances, rather than updates to an existing part of an infrastructure
- implements a safety feature for updates and rollbacks

## Deployment Strategies Comparison

Method	  | Impact of Failed Deployment | Deploy Time | Zero Downtime | No DNS Change	| Rollback Process | Code Deployed To
--        | -- | -- | -- | -- | --| -- 
All-at-once	| Downtime | 🕜	|	 | ✓	| Redeploy | Existing instances
In-place	| Downtime | 🕜 |	|	✓	| Redeploy | Existing instances
Rolling	| Single batch out of service; any successful batches before failure running new application version | 🕜 🕜 | ✓ | ✓ | Redeploy	Existing instances
Rolling with additional batch | Minimal if first batch fails; otherwise, similar to Rolling | 🕜 🕜 🕜 | ✓ | ✓ | Redeploy	| New and existing instances
Blue/Green | Minimal | 🕜 🕜 🕜 🕜 | ✓ | Swap URL | New instances
Immutable | Minimal | 🕜 🕜 🕜 🕜 | ✓ | ✓ | Redeploy | New instances

## Container Deployments

- Elastic Beanstalk enables you to launch your applications with Docker containers. 

## Monitoring and Troubleshooting

- Elastic Beanstalk also creates alerts that trigger at established thresholds to monitor your environment’s health

## Basic Health Monitoring

## Enhanced Health Monitoring

- gather additional resource data and display graphs and statistics of environment health in greater detail. 

