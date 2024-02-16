A
---

`access key` A special set of keys linked to a specific AWS IAM user.

ACID The storage consistency of a relational database, based on atomicity, consistency, isolation, and durability.

active-active Multi-region active-active deployment of resources across multiple regions for workloads requiring high availability and failover.

alarm A warning issued when a single metric crosses a set threshold over a defined number of time periods.

Amazon CloudFront The AWS content delivery network (CDN) hosted in all edge locations.

Amazon Elastic Block Storage (EBS) A virtual hard disk block storage device that is attached to Amazon EC2 instances.

Amazon Elastic Compute Cloud (EC2) A web service that provides secure, resizable compute capacity in the cloud. It enables you to launch and manage virtual servers, called Amazon Elastic Compute Cloud (EC2) instances, in the AWS cloud.

Amazon ElastiCache A distributed in-memory data store.

Amazon Machine Image (AMI) A template of an instance’s root drive.

application programming interface (API) A defined set of protocols that enables applications and services to communicate with each other.

archive An Amazon S3 Glacier grouping of compressed and encrypted files.

asymmetric key One key of a public/private key pair.

Auto Scaling An AWS service that adjusts compute capacity to maintain desired performance.

Auto Scaling group A group of Amazon EC2 instances that is controlled (that is, scaled up, scaled down, or maintained) using the EC2 Auto Scaling service.

availability zone (AZ) An insulated separate location within a region that contains at least one data center.

AWS Artifact Allows AWS customers to review the compliance standards supported by AWS.

AWS Direct Connect A dedicated private fiber connection to AWS VPCs or AWS public services.

AWS EC2access control list (ACL) A list that enables you to control access to Amazon S3 buckets by granting read/write permissions to other AWS accounts.

AWS Identity and Access Management (IAM) The hosted security system for the AWS cloud that controls access to AWS resources.

AWS Key Management Service (KMS) An AWS service that centrally manages AWS customers’ cryptographic keys and policies across AWS services that require data encryption.

AWS well-architected framework A framework for designing, deploying, and operating workloads hosted at AWS.

B
---

block storage Data records stored in blocks on a storage area network.

bucket The storage unit for an Amazon S3 object.

bucket policy A resource policy that is assigned directly to a storage entity such as an Amazon S3 bucket.

burst capacity The ability of a storage unit or a compute instance to increase processing power for a short period of time.

burst credits Performance credits that make it possible to burst above a defined performance baseline.

C
---

capacity units A measure of Amazon DynamoDB performance in terms of either reading or writing.

certificate authority (CA) A company or an entity that validates the identities of websites or domains using cryptographic public/private keys.

CloudWatch log group A group that logs information in near real time.

codebase The body of source code for a software program or application.

cold storage Infrequently accessed storage.

condition Special rule in a permission policy.

connection draining The process of deregistering (removing) a registered instance from a load balancer target group.

cooldown period A defined time period when no changes are allowed.

cost allocation tags Tags that are used to categorize and track AWS costs displayed with monthly and hourly cost allocation reports.

Cost and Usage Report (CUR) Tracks your AWS usage and provides estimated charges associated with your account for the current month.

D
---

data consistency A definition of how data records are either the same or not the same due to replication.

data transfer Incoming (ingress) and outgoing (egress) packet flow.

defense in depth (DiD) Deployment of multiple security controls (physical, administrative, and technical) to protect a hosted workload.

dependencies Cloud services, applications, servers, and various technology components that depend upon each other when providing a business solution.

Direct Connect See AWS Direct Connect.

distributed session A user session for which user state information is held in a separate durable storage location.

E
---

EC2 See Amazon Elastic Compute Cloud (EC2).

egress-only Internet gateway (EOIG) A one-way gateway connection for EC2 instances with IPv6 addresses.

Elastic Block Storage (EBS) See Amazon Elastic Block Storage (EBS).

Elastic IP (EIP) address A static public IP address that is created and assigned to your AWS account.

ElastiCache See Amazon ElastiCache.

endpoint A location where communication is made; a private connection from a VPC to AWS services.

ephemeral storage Temporary local block storage.

event notification Communications about changes in the application stack.

externally authenticated user A user that has authenticated outside Amazon before requesting access to AWS resources.

F
---

FedRAMP Federal Risk and Authorization Management Program, establishes the security requirements for usage of cloud services for federal government agencies.

H
---

health check A status check for availability.

high availability A group of compute resources that continue functioning even when some of the components fail.

I
---

IAM group A group of AWS IAM users.

IAM role A permission policy that provides temporary access to AWS resources.

Identity and Access Management (IAM) See AWS Identity and Access Management (IAM).

immutable During deployment and updates components are replaced rather than changed.

input/output operations per second (IOPS) A performance specification that defines the rate of input and output per second when storing and retrieving data.

Internet gateway (IG) An AWS connection to the Internet for a virtual private cloud (VPC).

K
---

Key Management Service (KMS) See AWS Key Management Service (KMS).

key-value An item of data where the key is the name and the value is the data.

L
---

Lambda@Edge A custom-created function to control ingress and egress Amazon CloudFront traffic.

launch template A set of detailed EC2 instance installation and configuration instructions.

LCU See load balancer capacity unit (LCU).

lifecycle hook A custom action to be performed before or after an Amazon EC2 instance is added to or removed from an Auto Scaling Group.

lifecycle policy A set of rules for controlling the movement of Amazon S3 objects between S3 storage classes.

lifecycle rules Rules that allow customers to transition backups that are stored in warm storage to cheaper cold storage.

listener A load balancer process that checks for connection requests using the defined protocols and ports.

load balancer capacity unit (LCU) Defines the maximum resource consumed calculated on new connections, active, connections, bandwidth, and rule evaluations.

Local Zone A single deployment of compute, storage, and select services close to a large population center.

M
---

metric Data collected for an AWS CloudWatch variable.

mount point A logical connection to a directory in a file system; a method to attach Amazon EFS storage to a Linux workload.

multi-factor authentication (MFA) Authentication that involves multiple factors, such as something you have and something you know.

multipart upload An upload in which multiple parts of a file are synchronously uploaded.

N
---

NAT gateway service A service that provides indirect Internet access to Amazon EC2 instances that are located on private subnets.

network access control list (NACL) A stateless subnet firewall that protects both inbound and outbound subnet traffic.

Nitro The latest AWS hypervisor, which replaces the Xen hypervisor and provides faster networking, compute, encryption, and management services.

NoSQL A database that does not follow SQL rules and architecture, hence the name “no” SQL.

NVMe Non-Volatile Memory Express, a standard hardware interface for SSD drives connected using PCI Express bus.

O
---

object storage Data storage as a distinct object with associated metadata containing relevant information.

origin access identity (OAI) A special AWS IAM user account that is provided the permission to access the files in an Amazon S3 bucket.

origin failover An alternate data source location for Amazon CloudFront distributions.

P
---

password policy A policy containing global password settings for AWS account IAM users.

peering connection A private networking connection between two VPCs or two transit gateways.

Pilot light An active/passive disaster recovery design that involves maintaining a limited set of compute and data records to be used in case of a disaster to the primary application resources. The compute records are turned off until needed, but the data records are active and are kept up-to-date.

primary database The primary copy of database records.

Q
---

queue A redundant storage location for messages and application state data for processing.

R
---

read capacity unit One strongly consistent read per second, or two eventually consistent reads per second, for items up to 4 KB in size.

read replica A read-only copy of a linked primary database.

recovery point objective (RPO) A metric that specifies the acceptable amount of data that can be lost within a specified period.

recovery time objective (RTO) A metric that specifies the maximum length of time that a service can be down after a failure has occurred.

region A set of AWS cloud resources in a geographic area of the world.

regional edge cache A large throughput cache found at an edge location that provides extra cache storage.

regional endpoint A device that provides HTTPS access to AWS services within a defined AWS region.

reliability The reasonable expectation that an application or service is available and performs as expected.

Reserved instance An Amazon EC2 instance for which you have prepaid.

RPO See recovery point objective (RPO).

RTO See recovery time objective (RTO).

S
---

scale out To increase compute power automatically.

scaling policy A policy that describes the type of scaling of compute resources to be performed.

security group A stateful firewall protecting Amazon EC2 instances’ network traffic.

Server Message Block (SMB) A network protocol used by Windows systems on the same network to store files.

serverless A type of computing in which compute servers and integrated services are fully managed by AWS.

server-side encryption (SSE) Encryption of data records at rest by an application or a service.

service-level agreement (SLA) A commitment between a cloud service provider and a customer indicating the minimum level of service to be maintained.

service-level indicator (SLI) Indicates the quality of service an end user is receiving at a given time. SLIs are measured as a level of performance.

service-level objective (SLO) An agreement defined as part of each service-level agreement. Objectives could be uptime or response time.

service quota A defined limit for AWS services created for AWS accounts.

simple scaling Scaling instances up or down based on a single AWS CloudWatch metric.

SLA See service-level agreement (SLA).

snapshot A point-in-time incremental backup of an EBS volume.

Snow device A variety of network-attached storage devices that can be used to transfer and receive data records to and from Amazon S3 storage.

standby database A synchronized copy of a primary database that is available in the event of a failure.

stateful Refers to a service that requires knowledge of all internal functions.

stateless Refers to a self-contained redundant service that has no knowledge of its place in the application stack.

step scaling Scaling up or down by percentages.

sticky session A user session for which communication is maintained with the initial application server for the length of the session. It ensures that a client is bound to an individual backend instance.

Structured Query Language (SQL) The de facto programming language used in relational databases.

subnet A defined IP address range hosted within a VPC.

symmetric key A key that can both lock and unlock.

T
---

T instance An instance provided with a baseline of compute performance.

table A virtual structure in which Amazon DynamoDB stores items and attributes.

target group A group of registered instances that receives specific traffic from a load balancer.

task definition A blueprint that describes how a Docker container should launch.

Throughput Optimized An EBS hard disk drive (HDD) volume option that provides sustained throughput of 500 Mb/s.

tiered pricing The more you use the less you are charged.

time to live (TTL) A value that determines the storage time of an Amazon CloudFront cache object.

U
---

uptime the percentage of time that a website is able to function during the course of a calendar year.

user state Data that identifies an end user and the established session between the end user and a hosted application.

V
---

versioning A process in which multiple copies of Amazon S3 objects, including the original object, are saved.

virtual private cloud (VPC) A logically isolated virtual network in the AWS cloud.

virtual private gateway (VPG) The AWS side of a VPN connection to a VPC.

W
---

warm standby An active/passive disaster recovery design that maintains a limited set of compute and data records that are both on and functioning. When the primary application resources fail, the warm standby resources are resized to production values.

write capacity unit (WCU) One write per second for items up to 1 KB in size.

write-once/read-many (WORM) A security policy that can be deployed on an Amazon S3 bucket or in S3 Glacier storage. The policy indicates that the contents can be read many times but are restricted from any further writes once the policy is enacted.

Z
---

zonal Refers to an availability zone location.

