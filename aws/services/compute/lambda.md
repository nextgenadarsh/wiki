AWS Lambda
---

- a `serverless` `computing` service that enables you to `run custom functions in response to events or specific triggers`.
- provides compute processing power `on demand`, executing functions.
- You can create functions without the need to provision or maintain any infrastructure.
- `charges` you only for the `time your code executes`.
- can be triggered by a wide range of events, such as object changes in an Amazon S3 bucket or an Amazon DynamoDB table, or from an HTTP request to an Amazon API Gateway endpoint.
- can communicate with other AWS services.
- is compatible with code written in a `variety of programming languages`, including Node.js, Java, Python, and C#.
- supports two types of `deployment packages`
  - Container images stored in ECR
  - .zip file archives stored in S3

# Firecracker

- Lambda functions run in a specialized virtualization format called Firecracker hosted on EC2 instances.
- It was developed by Amazon and is used as the virtualization technology for AWS Lambda and AWS Fargate.
- uses a `microVM architecture`, creating a `lightweight VM for each function` that is executed.
- microVMs are based on the Kernel-based Virtual Machine (KVM) hypervisor and are designed to be small, fast, and secure.
- utilizes a small footprint of approximately 5 MB of RAM.
- microVM is launched in less than 100 ms.
- `VM runs in an isolated guest mode`, using a network device for communication, a block I/O device to store the function code, and a programmable interval timer for security.
- The libraries required for execution are included in the local executable code; no outside libraries are required or allowed.

# AWS Lambda Integration

AWS Service | Lambda triggered when
--  | --  
S3 Bucket | an object is uploaded
DynamoDB Table  | an entry is made in a DynamoDB table
Amazon Kinesis  | data is added to an Amazon Kinesis stream
Amazon SNS      | a message is published to an SNS topic
Amazon Cognito  | a user signs up or signs in to an Amazon Cognito user pool, customizing the user experience or sending confirmation emails
Amazon API Gateway  | AWS Lambda can be integrated with Amazon API Gateway to build serverless backends for web, mobile, and IoT applications
Amazon CloudWatch logs  | content is delivered to an AWS CloudWatch log
AWS Config  | AWS resource deployments don’t meet defined compliance requirements
Application Load Balancer (ALB) | incoming mobile application requests can be directed to AWS Lambda functions hosted by a target group
AWS Step Functions  |  Step Functions can utilize Lambda functions as part of the state machine workflow.
CloudFront  | Both ingress and egress traffic flow to and from an edge location can be intercepted and queried using Lambda@Edge functions hosted at edge locations for a CloudFront CDN distribution

# Lambda Settings

- Function name
  - must be `unique within the region and account`
- Runtime
  - Node.js, Python, Java, C#, and Go.
- Role
  - defines the permissions that your function has to access other AWS resources or perform actions
- Memory
  - value between `128 MB` and 3,008 MB in `64 MB increments`
- Timeout
  - maximum amount of time that your function is allowed to run before it is terminated
  - specify a value between `1 second and 15 minutes`.
- VPC
  - specify a VPC to give your function access to resources in a private network, such as an Amazon RDS database

<h2 style="background-color:lightgreen"># AWS Lambda Cheat Sheet</h2>

- allows you to `run code as custom functions without having to provision servers` to host and execute the function.
- manages the required vCPU/RAM, storage, and execution of Lambda functions
- consist of programming code and any associated dependencies
- `Firecracker runs AWS Lambda functions` in a lightweight virtual machine (microVM).
- `Uploaded AWS Lambda code` is stored in an `S3` bucket or the `ECR`.
- receives `500 MB of temporary disk space` for use during execution.
- `monitors executing functions` using real-time Amazon `CloudWatch` metrics.
- A `Savings Plan can reduce the cost` of running AWS Lambda functions.

# AWS Lambda@Edge

- enables you to `run serverless functions in response to CloudFront requests` to website data records.
- functions `execute at edge locations`, providing fast and reliable performance for requests and queries.
- functions are written in `JavaScript using the Node.js runtime`.
- can be triggered in response to four different types of CloudFront events:
  - viewer request
  - viewer response
  - origin request
  - origin response
- executed in the `context of a specific CloudFront distribution` can access information about request and response details, such as request headers and cookies.
