Serverless Compute
===

# Introduction to Serverless Compute

- a cloud computing execution model in which the AWS Cloud acts as the server and dynamically manages the allocation of machine resources. AWS bases the price on the amount of resources the application consumes rather than on prepurchased units of capacity.

# AWS Lambda

- serverless compute platform that enables you to run code without provisioning or managing servers. With AWS Lambda, you can run code for nearly any type of application or backend service—with zero administration
- uses containerization to run your code
  ![AWS Lambda execution flow](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c12f001.jpg)
- you can also run AWS Lambda inside your VPC

# AWS Lambda Functions

## Creating an AWS Lambda Function

- methods to access AWS services and create an AWS Lambda function
  - AWS Management Console—graphical user interface (GUI)
  - AWS command line interface (AWS CLI)—Linux Shell and Windows PowerShell
  - AWS Software Development Kit (AWS SDK)—Java, .NET, Node.js, PHP, Python, Ruby, Go, Browser, and C++
  - AWS application programming interface (API)—send HTTP/HTTPS requests manually using API endpoints

## Execution Methods/Invocation Models

- invocation models for AWS Lambda
  - `Non-streaming Event Source` (`Push` Model)
    — Amazon Echo, Amazon S3, Amazon Amazon SNS, and Amazon Cognito
  - `Streaming Event Source` (`Pull` Model)
    — Amazon Kinesis or Amazon DynamoDB stream
- you can execute an AWS Lambda function synchronously or asynchronously

## Securing AWS Lambda Functions

### Execution permissions

- enable the AWS Lambda function to access other AWS resources in your account

### Invocation Permissions

- permissions that an event source needs to communicate with your AWS Lambda function. Depending on the invocation model (push or pull), you can either update the access policy you associate with your AWS Lambda function (push) or update the execution role (pull).

# Inside the AWS Lambda Function

## Function Package

- Two parts of the AWS Lambda function are considered critical:
- function package
  - contains everything you need to be available locally when your function is executed
  - maximum size of a function code package is 50 MB compressed and 250 MB extracted/decompressed
- function handler
  - a method inside the AWS Lambda function that you create and include in your package
  - can interact with other AWS services and make third-party API requests to web services that it might need to interact with.

## Event Object

- You can pass event objects that you pass into the handler function
- includes all the data and metadata that your AWS Lambda function needs to implement the logic

## Context Object

- second object that you pass to the handler 
- contains data about the AWS Lambda function invocation itself. The context and structure of the object vary based on the AWS Lambda function language
- three primary data points that the context object contains
  - AWS Requestid
    - Tracks specific invocations of an AWS Lambda function, and it is important for error reports or when you need to contact AWS Support.
  - Remaining time
    - Amount of time in milliseconds that remain before your function timeout occurs. AWS Lambda functions can run a maximum of 300 seconds (5 minutes) as of this writing, but you can configure a shorter timeout.
  - Logging
    - Each language runtime provides the ability to stream log statements to Amazon CloudWatch Logs. The context object contains information about which Amazon CloudWatch Log stream your log statements are sent to.

# Configuring the AWS Lambda Function

## Descriptions and Tags

- best practice is to tag and give descriptions of your resources

## Memory

- You can allocate 128 MB of RAM up to 3008 MB of RAM in 64-MB increments. This dictates the amount of memory available to your function when it executes and influences the central processing unit (CPU) and network resources available to your function.

## Timeout

- configure how long your function executes for before a timeout is returned
- default timeout value is 3 seconds
- you can specify a maximum of 300 seconds (5 minutes)

## Network Configuration

- two ways to integrate your AWS Lambda functions with external dependencies
  - default network configuration
    - your AWS Lambda function communicates from inside an Amazon VPC that AWS Lambda manages. The AWS Lambda function can connect to the internet, but not to any privately deployed resources that run within your own VPCs, such as Amazon EC2 servers.
  - Amazon VPC
    - Lambda function uses an Amazon VPC network configuration to communicate through an elastic network interface (NIC). This interface is provisioned within the Amazon VPC and subnets, which you choose within your own account
- AWS Lambda easily integrates with AWS CloudTrail, which records and delivers log files to your Amazon S3 bucket to monitor API usage inside your account.

## Concurrency

- By default, the account-level concurrency within a given region is set with 1,000 functions as a maximum to provide you 1,000 concurrent functions to execute

## Concurrency Limits

- Set a function-level concurrent execution limit.
- The shared concurrent execution pool is referred to as the unreserved concurrency allocation

## Dead Letter Queues

- If any of these failures occur, your function generates an exception, which you handle with a dead letter queue (DLQ). A DLQ is either an Amazon Simple Notification Service (Amazon SNS) topic or an Amazon Simple Queue Service (Amazon SQS) queue, which you configure as the destination for all failed invocation events. If a failure event occurs, the DLQ retains the message that failed, analyzes it further, and reprocesses it if necessary.

## Environment Variables

- AWS recommends that you separate code and configuration settings
- Use environment variables for configuration settings. Environment variables are key-value pairs that you create and modify as part of your function configuration. These key-value pairs pass variables to your AWS Lambda function at execution time

## Versioning

- You can publish one or more versions and aliases for your AWS Lambda functions.
- After you publish a version, it is immutable, and you cannot change it.

## Creating an Alias

- assign an alias to a particular version and use that alias in the application

# Invoking AWS Lambda Functions

- many ways to invoke an AWS Lambda function
  - push method
  - pull method
  - custom application
  - schedule
  - event  

# Monitoring AWS Lambda Functions

- two primary tools to monitor functions

## Using Amazon CloudWatch

- Amazon CloudWatch monitors AWS Lambda functions
- By default, AWS Lambda enables these metrics: invocation count, invocation duration, invocation errors, throttled invocations, iterator age, and DLQ errors.

## Using AWS X-Ray

- a service that collects data about requests that your application serves, and it provides tools to view, filter, and gain insights into that data to identify issues and opportunities for optimization
- For any traced request to the application, information displays about the request and response, but also about calls that the application makes to downstream AWS resources, microservices, databases, and HTTP web APIs.
- Main parts to the X-Ray service:
  - Application code runs and uses the AWS X-Ray SDK (Node.js, Java, and .NET, Ruby, Python, and Go).
  - AWS X-Ray daemon is an application that listens for traffic on User Datagram Protocol (UDP) port 2000, gathers raw segment data, and relays it to the AWS X-Ray API.
  - AWS X-Ray displays in the AWS Management Console.
- With the AWS SDK, you integrate X-Ray into the application code. The AWS SDK records data about incoming and outgoing requests and sends it to the X-Ray daemon, which relays the data in batches to X-Ray
- When the daemon sends the data to X-Ray, X-Ray uses trace data from the AWS resources that power the cloud applications to generate a detailed service graph. The service graph shows the client, your frontend service, and backend services that your frontend service calls to process requests and persist data. Use the service graph to identify bottlenecks, latency spikes, and other issues to improve the performance of your applications.
![AWS X-Ray service map](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c12f005.jpg)

