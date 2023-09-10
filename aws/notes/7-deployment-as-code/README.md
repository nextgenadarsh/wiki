Deployment as Code (DaC)
=========

# Continuous Delivery with AWS `CodePipeline`

- create a continuous integration/continuous deployment pipeline (CI/CD) that integrates various sources, tests, deployments, or other components
- Implements AWS CodeCommit as a source
- `CodeBuild` allows you to pull code and packages from various sources to create publishable build artifacts
- AWS `CodeDeploy` allows you to deploy compiled artifacts to infrastructure in your environment
- AWS CodePipeline can also be used to provision, configure, and manage infrastructure

## Benefits of Continuous Delivery

- reduced manual effort required to ensure code changes are tested prior to release
- developers are no longer tasked with completing steps other than checking in code changes
- the fact that changes are tested immediately after check-in ensures that more bugs are caught earlier in the development process
- continuous delivery ensures that quality changes are delivered faster

# Using AWS CodePipeline to Automate Deployments

![AWS CodePipeline workflow](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c07f002.jpg)

## CodePipeline (Like `Jenkin`)

- Underpinning of CI/CD processes in AWS
- CodePipeline builds, tests, and deploys your code every time there is a code change, based on the release process models you define.
- You define workflow steps through a visual editor within the AWS Management Console or via a JavaScript Object Notation (JSON) structure for use in the AWS CLI or AWS SDKs
- Access to create and manage release workflows is controlled by AWS Identity and Access Management (IAM)
- provides a dashboard where you can review real-time progress of revisions, attempt to retry failed actions, and review version information about revisions that pass through the pipeline.

## AWS CodePipeline Concepts

### Pipeline

- overall workflow that defines what transformations software changes will undergo
- You cannot change the name of a pipeline. If you would like to change the name, you must create a new pipeline

### Revision

- work item that passes through a pipeline.
- can be a change to your source code or data stored in AWS CodeCommit or GitHub or any other source
- a single stage can process one revision at a time

### Stage

- a group of one or more actions
- Each stage must have a unique name. Should any one action in a stage fail, the entire stage fails for this revision

### Action
- defines the work to perform on the revision
- actions run in series or in parallel

### Source

- source action defines the location where you store and update source files
- Modifications to files in a source repository or archive trigger deployments to a pipeline

### Build

- use a build action to define tasks such as compiling source code, running unit tests, and performing other tasks that produce output artifacts for later use in your pipeline

### Test

- use test actions to run various tests against source and compiled code, such as lint or syntax tests on source code, and unit tests on compiled, running applications

### Deploy

- deploy action is responsible for taking compiled or prepared assets and installing them on instances, on-premises servers, serverless functions, or deploying and updating infrastructure using AWS CloudFormation templates.

### Approval

- approval action is a manual gate that controls whether a revision can proceed to the next stage in a pipeline. Further progress by a revision is halted until a manual approval by an IAM user or IAM role occurs.

### Invoke

- Invoke actions execute AWS Lambda functions, which allows arbitrary code to be run as part of the pipeline execution

### Artifact

- actions that act on a file or set of files. Artifacts can pass between actions and stages in a pipeline to provide a final result or version of the files

### Transition

- Transitions connect stages in a pipeline and define which stages should transition to one another. When all actions in a stage complete successfully, the revision passes to the next stage(s) in the pipeline.

### Managing Approval Actions

- Approval actions halt further progress through a pipeline until an authorized IAM user or IAM rule approves the transition. You can use approvals to review changes manually before final release into production, or as a code review step.

### AWS CodePipeline Service Limits

## AWS CodePipeline Tasks

### Create an AWS CodePipeline

### Start a Pipeline

### Retry a Failed Action

### Create a Cross-Account Pipeline

### Pipeline Account Steps

### Target Account Steps

# Using AWS CodeCommit as a Source Repository

- A fully managed source control service that makes it easy for companies to host secure and highly scalable private Git repositories

## AWS CodeCommit Concepts

### Credentials

### HTTPS

### SSH

### Use the Credential Helper

### Development Tools and Integrated Development Environment

### Repository

### Repository Notifications

### Repository Triggers

### Cross-Account Access to a Different Account

### Repository Account Actions

### User Account Actions

### Files

### Pull Requests

### Commits

### Branches

## Migrate to AWS CodeCommit

### Migrate a Git Repository

### Migrate Unversioned Content

### Migrate Incrementally

## AWS CodeCommit Service Limits

# Using AWS CodeCommit with AWS CodePipeline

# Using AWS CodeBuild to Create Build Artifacts

## CodeBuild

- a fully managed build service that compiles source code, runs tests, and produces software packages that are ready to deploy.
- enables you to define the build environment to perform build tasks and the actual tasks that it will perform. AWS CodeBuild comes with prepackaged build environments for most common workloads and build tools (Apache Maven, Grade, and others), and it allows you to create custom environments for any custom tools or processes.

## AWS CodeBuild Concepts

### Build Projects

### Create a Build Project

### Build Specification (buildspec.yml)

### Version

### Environment Variables (env)

### Phases

### Artifacts

### Cache

### Build Environments

- a Docker image with a pre-configured operating system, programming language runtime, and any other tools that AWS CodeBuild uses to perform build tasks and communicate with the service, along with other metadata for the environment, such as the compute settings

### AWS CodeBuild Environments

### Compute Types

### Environment Variables

### Builds

## AWS CodeBuild Service Limits

# Using AWS CodeBuild with AWS CodePipeline

# Using AWS CodeDeploy to Deploy Applications

## CodeDeploy

- a service that automates software deployments to a variety of compute services, such as Amazon EC2, AWS Lambda, and instances running on-premises
- use to automate software deployments and eliminate the need for error-prone manual operations. 

## AWS CodeDeploy and NGINX

## AWS CodeDeploy Concepts

### Revision

### Deployments

### In-Place Deployments

### Blue/Green Deployments

### Stop Deployments

### Rollbacks

### Test Deployments Locally

### Deployment Group

- designates the Amazon EC2 on-premises instances that a revision deploys.

### On-Premises Instances

### Deploy to Amazon EC2 Auto Scaling Groups

### Deployment Configuration

#### Amazon EC2 On-Premises Deployment Configurations

#### AWS Lambda Deployment Configurations

### Application

### AppSpec File

#### Amazon EC2 On-Premises AppSpec

#### AWS Lambda AppSpec

### AWS CodeDeploy Agent

## AWS CodeDeploy Service Limits

# Using AWS CodeDeploy with AWS CodePipeline

