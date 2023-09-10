Serverless Applications
===

# Introduction to Serverless Applications

- serverless applications have built-in availability and fault tolerance

# Web Server with Amazon S3 (Presentation Tier)

## Amazon S3 Static Website

- S3 bucket names must be globally unique
- SSL wildcard certificate only matches buckets that do not contain periods
- enable and configure bucket to use static website hosting, index document, error document, and redirection rules 
- Your website address looks like `examplebucket.s3-website.region.amazonaws.com`

## Configuring Web Traffic Logs

- Amazon S3 allows you to log and capture information such as the number of visitors who access your website
- To enable logs, create a new Amazon S3 bucket to store your logs

## Creating Custom Domain Name with Amazon Route 53

- Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service
- designed to give developers and businesses an extremely reliable and cost-effective way to route end users to internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1
- Amazon Route 53 Traffic Flow makes it easy for you to manage traffic globally through a variety of routing types, including latency-based routing, geolocation, geoproximity, and weighted round-robin, all of which can be combined with DNS failover to enable a variety of low-latency, fault-tolerant architectures.

## Speeding Up Content Delivery with Amazon CloudFront

![Amazon CloudFront cache](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c13f001.jpg)
- use Amazon CloudFront to move your content closer to your end users
- Amazon CloudFront has two delivery methods to deliver content
  - first is a web distribution, and this is for storing of .html, .css, and graphic files
  - also provides the ability to have an RTMP distribution, which speeds up distribution of your streaming media files using Adoble Flash Media Server’s RTMP protocol. An RTMP distribution allows an end user to begin playing a media file before the file has finished downloading from a CloudFront edge location
- To use Amazon CloudFront with your Amazon S3 static website, perform these tasks:
  - Choose a delivery method
  - Specify the cache behavior
  - Choose the distribution settings and network

# Dynamic Data with Amazon API Gateway (Logic or App Tier)

- a fully managed, serverless AWS service, with no server that runs inside your environment to define, deploy, monitor, maintain, and secure APIs at any scale

## API Gateway integration strategy

### Control service

  - Uses REST to provide access to Amazon services, such as AWS Lambda, Amazon Kinesis, Amazon S3, and Amazon DynamoDB

### Execution service

- Uses standard HTTP protocols or language-specific SDKs to deploy API access to backend functionality

### Endpoints

- `Regional endpoints` Live inside the AWS Region, such as us-west-2
- `Edge optimized endpoints` Use Amazon CloudFront as connection points for clients, and integrate with your API
- `Private endpoints` Can live only inside of a virtual private cloud (VPC)

## Resources

- an object that provides operations you use to interact with HTTP commands such as GET, POST, or DELETE
- use a model to describe the data format for the request or response
- use the model with the AWS SDK for an API to validate data and generate a mapping template

## HTTP Methods

- The Internet Engineering Task Force (IETF) is responsible for developing and documenting the HTTP protocol and how it operates
- Amazon API Gateway uses the HTTP protocol to process these HTTP methods

## Stages

- a named reference to a deployment, which is a snapshot of the API
- Use a stage to manage and optimize a particular deployment. For example, stage settings enable caching, customize request throttling, configure logging, define stage variables, or attach a canary release to test

## Authorizers

- Use Amazon API Gateway to set up authorizers with Amazon Cognito user pools on an AWS Lambda function. This enables you to secure your APIs and only allow users to whom you have granted specific access to your API.

## API Keys

- generate API keys to provide access to your API for external users, use them to sell to your customer base, and use the API call apikey:create to create an API key

## Cross-Origin Resource Sharing

- Remedies the inability of a client-side web application that runs on one server to be retrieved from another service. This remedy is called a same-origin policy, and primarily it prevents malicious actors from calling your APIs from different servers and creates a denial of service for your endpoint.
- Allows you to set certain HTTP headers to enable cross-origin access to call APIs or services to which you need access
- To use Amazon API Gateway, you must enable the CORS resource

## Integrating with AWS Lambda

- Contents of the client’s HTTPS request can be passed to AWS Lambda for execution, where you can write a function to talk to your database tier

## Monitoring Amazon API Gateway with Amazon CloudWatch

- Amazon API Gateway also integrates with Amazon CloudWatch
- Amazon CloudWatch provides pre-configured metrics to help you monitor your APIs and build both dashboards and alarms
- Supported metrics
  - 4XX
  - 5XX
  - CacheHitCount
  - CacheMissCount
  - Count
  - IntegrationLatency
  - Latency

## Other Notable Features

### Security

- API Gateway exposes HTTPS endpoints only

### Definition support

- Swagger Specification, is used to define a RESTful interface

### Free Tier

- API Gateway has a free tier, and it allows one million API receive calls per month, for free, for the first 12 months

# User Authentication with Amazon Cognito

- allows for simple and secure user sign-up, sign-in, and access control mechanisms designed to handle web application authentication
- Amazon Cognito includes the following features:
  - Amazon Cognito user pools, which are secure and scalable user directories
  - Amazon Cognito identity pools (federated identities), which offer social and enterprise identity federation
  - Standards-based Web Identity Federation Authentication through Open Authorization (OAuth) 2.0, Security Assertion Markup Language (SAML) 2.0, and OpenID Connect (OIDC) support
  - Multi-factor authentication
  - Encryption for data at rest and data in transit
  - Access control with AWS Identity and Access Management (IAM) integration
  - Easy application integration (prebuilt user interface)
  iOS Object C, Android, iOS Swift, and JavaScript
  - Adherence to compliance requirements such as Payment Card Industry Data Security Standard (PCI DSS)

### Amazon Cognito User Pools

- a user directory in Amazon Cognito
- It provides the features like:
  - Sign-up and sign-in services
  - A built-in, customizable web user interface (UI) to sign in users
  - Social sign-in with Facebook, Google, and Amazon, and sign-in with Security Assertion Markup Language (SAML) identity providers from your user pool
  - User directory management and user profiles
  - Security features, such as multi-factor authentication (MFA), check for compromised credentials, account takeover protection, and phone and email verification
  - Customized workflows and user migration through AWS Lambda triggers
  - After successfully authenticating a user, Amazon Cognito issues JSON Web Tokens (JWT) that you can use to secure and authorize access to your own APIs or exchange them for AWS credentials.

### Password Policies

- you can either allow users to sign up and enroll themselves or allow only administrators to create users

### Multi-factor Authentication

### Device Tracking and Remembering

- you can save that user’s device and remember it so that they do not have to provide a token again, as the application has already seen this specific device

### User Interface Customization

### Amazon Cognito Identity Pools

- allow you to create unique identities and assign permissions for your users
- allows you to obtain temporary AWS credentials with permissions that you define either to access other Amazon services directly or to access resources through Amazon API Gateway

# Standard Three-Tier vs. the Serverless Stack

![Serverless web application architecture](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c13f006.jpg)

- Serverless web application architecture services include the following:
  - Routing: Amazon Route 53
  - Web servers/static data: Amazon S3
  - User authentication: Amazon Cognito user pools
  - App servers: Amazon API Gateway and AWS Lambda
  - Database: Amazon DynamoDB

# Amazon Aurora Serverless

- an on-demand, auto-scaling configuration for the Aurora MySQL-compatible edition, where the database automatically starts, shuts down, and scales up or down as needed by your application. This allows you to run a traditional SQL database in the cloud without needing to manage any infrastructure or instances.
- great for infrequently used applications, new applications, variable workloads, unpredictable workloads, development and test databases, and multi-tenant applications

# AWS Serverless Application Model

- allows you to create and manage resources in your serverless application with AWS CloudFormation to define your serverless application infrastructure as a SAM template
- A SAM template is a JSON or YAML configuration file that describes the AWS Lambda functions, API endpoints, tables, and other resources in your application
- When you update your AWS SAM template, you re-deploy the changes to this stack
- AWS SAM is an extension of AWS CloudFormation

# AWS SAM CLI

- With AWS SAM, you can define templates, in JSON or YAML, which are designed for provisioning serverless applications through AWS CloudFormation.
- AWS SAM CLI is a command line interface tool that creates an environment in which you can develop, test, and analyze your serverless-based application, all locally. This allows you to test your AWS Lambda functions before uploading them to the AWS service. AWS SAM CLI also allows you to develop and test your code quickly, and this gives you the ability to test it locally, which allows you to develop it faster.
- To use AWS SAM CLI, you must meet a few prerequisites. You must install Docker, have Python 2.7 or 3.6 installed, have pip installed, install the AWS CLI, and finally install the AWS SAM CLI

# AWS Serverless Application Repository

- enables you to deploy code samples, components, and complete applications quickly for common use cases, such as web and mobile backends, event and data processing, logging, monitoring, Internet of Things (IoT), and more. Each application is packaged with an AWS SAM template that defines the AWS resources.

# Serverless Application Use Cases

Case studies on running serverless applications are located at the following URLs:

The Coca-Cola Company:
https://aws.amazon.com/blogs/aws/things-go-better-with-step-functions/
FINRA:
https://aws.amazon.com/solutions/case-studies/finra-data-validation/
iRobot:
https://aws.amazon.com/solutions/case-studies/irobot/
Localytics:
https://aws.amazon.com/solutions/case-studies/localytics/