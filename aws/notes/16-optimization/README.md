Optimization
===

# Cost Optimization: Everyone’s Responsibility

- Engineers should design the code to consume resources only when needed, control the utilization, build sizing into architecture, and tag the resources to optimize usage

## Tagging

- helps you organize them and assign cost accountability. When you apply tags to your AWS resources and activate the tags, AWS adds this information to the Cost and Usage reports.

### Follow Mandatory Cost Tagging

#### Environment

- Specifying an environment tag reduces analysis time, post-processing, and the need to maintain a separate mapping file of production versus nonproduction accounts

#### Application ID

- Identifies `resources` that are `related to a specific application` for easy tracking of spending changes and that turn off at the end of projects.

#### Automation Opt-In/Opt-Out

- Indicates whether a resource should be included in an automated activity such as starting, stopping, or resizing instances.

#### Cost Center/Business Unit

- Identifies the cost center or business unit associated with a resource, typically for cost allocation and tracking.

#### Owner

- Identify who is responsible for the resource
- Using email addresses supports automated notifications to both the technical and business owners as required

### Tag on Creation

- Make tagging a part of your build process and automate it with AWS management tools like `OpsWorks`
- You can execute management tasks at scale by listing resources with specific tags and then executing the appropriate actions

### Enforce Tag Use

- Using `IAM`, you can `enforce tag use` to gain precise control over access to resources, ownership, and accurate cost allocation
- If the user applies any tag that is not included in the policy, the action is denied

### Tagging Tools

#### AWS Tag Editor

- Finds resources with `search criteria` (including missing and misspelled tags) and enables you to edit tags from Mgmt Console

#### AWS Config

— Identifies resources that do not `comply with tagging policies`

#### Capital One’s Cloud Custodian (open source)

— Ensures tagging compliance and remediation

## Reduce AWS Usage

- Set a continuous practice to review your consumption of AWS resources, and understand the factors that contribute to cost
- Use dashboards to view the estimated costs of your AWS usage, top services that you use most

### Delete Unnecessary EBS Volumes

- Stopping an EC2 instance leaves any attached EBS volumes operational.

### Stop Unused Instances

- Automatically stop dev/test/production instances during non-business hours.

### Delete Idle Resources

Consider following best practices:

- Turn off instances that are no longer being used
- Terminating an instance automatically deletes attached EBS volumes so consider storing a snapshot of the volume
- Spin up instances to test new ideas and spin it down if done
- If an Elastic IP address is not used, you can avoid charges by releasing the IP address

### Update Outdated Resources

- As your requirements change, be aggressive in decommissioning resources, components, and workloads that you no longer require

### Delete Unused Keys

- Each CMK that you create in AWS KMS, incurs a cost you until you delete it

### Delete Old Snapshots

- To reduce storage costs, check for “stale” snapshots—ones that are more than 30 days old—and delete them

# Right Sizing

- Process of matching instance types and sizes to performance and capacity requirements at the lowest possible cost

## Select the Right Use Case

- Identify the following usage needs and patterns so that you can take advantage of potential right-sizing options:

### Steady state

- Load remains constant over time, making forecasting simple. Consider using `Reserved Instances` to gain significant savings

### Variable, but predictable

- Load changes on a predictable schedule. Consider using AWS `Auto Scaling`

### Dev, test, production

- These environments can usually be `turned off` outside of `work hours`

### Temporary Temporary

- Workloads that have flexible start times and can be `interrupted` are good candidates for `Spot Instances` instead of On-Demand Instances

## Select the Right Instance Family

### Amazon Elastic Cloud Compute

- General purpose
- Compute optimized
  - higher ratio of virtual CPUs to memory
- Memory optimized
  - Optimized to deliver tens of thousands of low-latency, random IOPS to applications
- Accelerated computing
  - Provides access to hardware-based compute accelerators, such as GPUs or FPGAs

### Amazon Relational Database Service

- Standard performance
  - for general-purpose database workloads
  - has the most options for provisioning increased IOPS
- Burst-able performance
  - For workloads that require burst-able performance capacity
- Memory optimized
  - Optimized for in-memory functions and big data analysis

## Select the Right Instance Compatibility

- Virtualization type
  - The instances must have the same Linux AMI virtualization type (PV AMI versus HVM) and platform (Amazon EC2-Classic versus Amazon EC2-VPC)
- Network
  - Instances unsupported in Amazon EC2-Classic must be launched in a VPC
- Platform
  - If the current instance type supports 32-bit AMIs, make sure to select a new instance type that also supports 32-bit AMIs (not all Amazon EC2 instance types do)

# Using Instance Reservations

## AWS Pricing for Reserved Instances

- No Upfront
- Partial Upfront
- All Upfront

## Amazon EC2 Reservations

- you commit to a period of usage (one or three years) and save up to 75 percent over equivalent On-Demand hourly rates
- For applications that have steady state or predictable usage

#### Convertible Reserved Instances

- provided for a one-year or three-year term, and they enable conversion to different families, new pricing, different instance sizes, different platforms, or tenancy during the period
- Use when you are uncertain about instance needs in the future
- no limits to how many times you perform an exchange

#### Reserved Instance Marketplace

- Used to sell your unused Reserved Instances and buy Reserved Instances from other AWS customers

## Amazon Relational Database Service Reservations

# Using Spot Instances

- Offer spare compute capacity in the AWS Cloud at steep discounts compared to On-Demand Instances
- Save up to 90 percent on stateless web applications, big data, containers, continuous integration/continuous delivery (CI/CD), high performance computing (HPC), and other fault-tolerant workloads

### Spot Fleets

- Use to request and manage multiple Spot Instances automatically, which provides the lowest price per unit of capacity for your cluster or application, such as a batch-processing job, a Hadoop workflow, or an HPC grid computing job
- enable you to launch and maintain the target capacity and to request resources automatically to replace any that are disrupted or manually terminated.

#### Amazon EC2 Fleets

- enables you to provision compute capacity across different instance types, Availability Zones, and across On-Demand, Reserved Instances, and Spot Instances purchase models to help optimize scale, performance, and cost.

### Design for Continuity

#### Using Termination Notices

#### Using Persistent Requests

#### Using Block Durations

#### Minimizing the Impact of Interruptions

- Adding checkpoints
- Splitting up the work

# Using AWS Auto Scaling

- automatically increases the number of resources during the demand spikes to maintain performance and decreases capacity when demand lulls to reduce cost.

### Amazon EC2 Auto Scaling

- helps you scale your Amazon EC2 instances and Spot Fleet capacity up or down automatically according to conditions that you define. 
- generally used with Elastic Load Balancing to distribute incoming application traffic across multiple Amazon EC2 instances in an AWS Auto Scaling group

#### Dynamic Scaling

- refers to the functionality that automatically increases or decreases capacity based on load or other metrics

#### Scheduled Scaling

- allows you to scale your application ahead of known load changes, such as the start of business hours, thus ensuring that resources are available when users arrive

#### Fleet Management

- refers to the functionality that automatically replaces unhealthy instances in your application, maintains your fleet at the desired capacity, and balances instances across Availability Zones
- ensures that your application is able to receive traffic and that the instances themselves are working properly

#### Instances Purchasing Options

- You have the option to define the desired split between On-Demand and Spot capacity

#### Golden Images

- a snapshot of a particular state of a resource, such as an Amazon EC2 instance, Amazon EBS volumes, and an Amazon RDS DB instance

### AWS Auto Scaling

- Monitors your applications and automatically adjusts capacity of all scalable resources to maintain steady, predictable performance at the lowest possible cost

#### Predictive Scaling

- Uses machine learning algorithms to detect changes in daily and weekly patterns, automatically adjusting their forecasts

### DynamoDB Auto Scaling

- uses the AWS Auto Scaling service to adjust provisioned throughput capacity dynamically on your behalf in response to actual traffic patterns

### Amazon Aurora Auto Scaling

- dynamically adjusts the number of Aurora Replicas provisioned for an Aurora DB cluster

#### Amazon Aurora Serverless

- An on-demand, automatic scaling configuration for the MySQL-compatible edition of Amazon Aurora. An Aurora Serverless DB cluster automatically starts up, shuts down, and scales capacity up or down based on your application’s needs

### Accessing AWS Auto Scaling

# Using Containers

## Containerize Everything

## Containers without Servers

- AWS Fargate technology is available with Amazon ECS. With Fargate, you no longer have to select Amazon EC2 instance types, provision and scale clusters, or patch and update each server. You do not have to worry about task placement strategies, such as binpacking or host spread, and tasks are automatically balanced across Availability Zones. Fargate manages the availability of containers for you. You define your application’s requirements, select Fargate as your launch type in the AWS Management Console or AWS CLI, and Fargate takes care of all of the scaling and infrastructure management required to run your containers.

# Using Serverless Approaches

- ideal for applications whereby load can vary dynamically

### Optimize Lambda Usage

- monitor the execution duration and configuration of your functions closely

#### Optimal memory size

- By analyzing the Max Memory Used: field in the Invocation report, you can determine whether your function needs more memory or whether you over-provisioned your function’s memory size.

#### Language runtime performance

- If your application use case is both latency-sensitive and susceptible to incurring the initial invocation cost frequently (spiky traffic or infrequent use), then recommend one of the interpreted languages, such as Node.js or Python.

#### Optimizing code

- Pay attention to reusing the objects and using global/static variables. Keep live or reuse HTTP/session connections, and use default network environments as much as possible

# Optimizing Storage

- consider data storage options for each workload separately.
- First understand the performance levels of your workloads
- Conduct a performance analysis to measure input/output operations per second, throughput, quick access to your data, durability, sensitivity, size, and budget

## Object Storage

## Block Storage

## File Storage

## Optimize Amazon S3

- Identifying the right storage class and moving less frequently accessed Amazon S3 data to cheaper storage tiers yields considerable savings

### Storage Management Tools/Features

#### Cost Allocation S3 Bucket Tags

- A `cost allocation tag` is a key-value pair that you associate with an S3 bucket.

#### Amazon S3 Analytics: Storage Class Analysis

- analyze storage access patterns to help you decide when to transition the right data to the right storage class

#### Amazon S3 Inventory

- audits and reports on the replication and encryption status of your S3 objects on a weekly or monthly basis

#### Amazon CloudWatch

- Amazon S3 can also publish storage, request, and data transfer metrics to Amazon CloudWatch

#### Use Amazon S3 Select

- enables applications to retrieve only a subset of data from an object by using simple SQL expressions. By using Amazon S3 Select to retrieve only the data needed by your application, you can achieve drastic performance increases—in many cases, you can get as much as a 400 percent improvement

#### Use Amazon Glacier Select

- unlocks an opportunity to query your archived data easily. With Glacier Select, you can filter directly against an Amazon S3 Glacier object by using standard SQL statements.

## Optimize Amazon EBS

- Monitor volumes periodically to identify ones that are unattached or appear to be underutilized or over-utilized, and adjust provisioning to match actual usage
- Check Configuration:
  - launch instances as EBS optimized
  - Choose an EBS-optimized instance that provides more dedicated EBS throughput than your application needs
  - New EBS volumes do not require initialization but snapshot restored volume must be initialized

### Use Monitoring Tools

- Amazon CloudWatch
  - BurstBalance
  - VolumeQueueLength
  - VolumeReadBytes, VolumeWriteBytes, VolumeReadOps, VolumeWriteOps
- AWS Trusted Advisor
  - identify unattached, underutilized, and overutilized EBS volumes

### Delete Unattached Amazon EBS Volumes

### Resize or Change the EBS Volume Type

### Delete Stale Amazon EBS Snapshots

# Optimizing Data Transfer

- ensures that you minimize data transfer costs
- Use Amazon CloudFront
- `Amazon S3 transfer acceleration` enables fast transfer of files over long distances between your client and your S3 bucket
- use multipart uploads with multiple parts uploading at once to help maximize network throughput
- Using Amazon Route 53 to serve their requests from the AWS Region for which network latency is lowest

## Caching

### Amazon ElastiCache

## Amazon DynamoDB Accelerator (DAX)

# Relational DB and Amazon DynamoDB

- Apply NoSQL Design
- Keep Related Data Together
- Keep Fewer Tables
- Distribute Workloads Evenly
- Designing Partition Keys
  - The more distinct partition key values that your workload accesses, the more those requests are spread across the partitioned space
- Implementing Write Sharding
- Upload Data Efficiently
  - You can distribute your upload work by using the sort key to load one item from each partition key value, then another item from each partition key value, and so on.
- Use Sort Keys for Version Control
- Keep the Number of Indexes to a Minimum
- Choose Projections Carefully
  - Every time you update an attribute that is projected in an index, you incur the extra cost of updating the index as well.
- Optimize Frequent Queries to Avoid Fetches
- Use Sparse Indexes
- Avoid Scans as Much as Possible

# Monitoring Costs

- AWS provides tools to help you identify those cost-saving opportunities and keep your resources right-sized. Use these tools to help you access, organize, understand, control, and optimize your costs.

## AWS Trusted Advisor

- an online tool that provides you with real-time guidance to help you provision your resources following AWS best practices.

## AWS Cost Explorer

- Use to dive deeper into your cost and usage data to identify trends, pinpoint cost drivers, and detect anomalies
- AWS Cost Explorer built-in reports include the following:
  - Monthly Costs by AWS Service
  - Amazon EC2 Monthly Cost and Usage
  - Monthly Costs by Linked Account
  - Monthly Running Costs
  - RI Utilization Report 
  - RI Coverage Report

### AWS Cost Explorer API

- Use to query your cost and usage data programmatically 

## AWS Budgets

- you can set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.
- Budgets can be tracked at the monthly, quarterly, or yearly level, and you can customize the start and end dates

## AWS Cost and Usage Report

- tracks your AWS usage and provides estimated charges associated with that usage
- updated at least once a day until it is finalized at the end of the billing period
- gives you the most `granular` insight possible into your costs and usage, and it is the `source of truth` for the billing pipeline

## Amazon CloudWatch

- a monitoring service for AWS Cloud resources and the applications you run on AWS

## AWS Cost Optimization Monitor

- an automated reference deployment solution that processes detailed billing reports to provide granular metrics that you can search, analyze, and visualize in a customizable dashboard

## Cost Optimization: Amazon EC2 Right Sizing

- an automated AWS reference deployment solution that uses managed services to perform a right-sizing analysis and offer detailed recommendations for more cost-effective instances. The solution analyzes two weeks of utilization data to provide detailed recommendations for right sizing your Amazon EC2 instances.

# Monitoring Performance

- Use monitoring metrics to raise alarms when thresholds are breached
- AWS provides tools to monitor the performance, reliability, and availability of your resources

## Amazon CloudWatch

- You can create an alarm to monitor any Amazon CloudWatch metric in your account

## AWS Trusted Advisor

- inspects your AWS environment and makes recommendations that help to improve the speed and responsiveness of your applications

