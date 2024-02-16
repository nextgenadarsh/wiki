Data Security Controls
---

# Infrastructure Security

Infrastructure security requires deploying the following protections:

- DDoS Protection
  - Amazon deploys AWS `WAF and Shield` to protect the AWS cloud from `DDoS` attacks.
- Network isolation
  - EC2 instances must be hosted in a virtual private cloud (VPC). Many AWS services can be accessed from a VPC with private VPC endpoints (Interface and Gateway endpoints), ensuring workload traffic remains on the private AWS network.
- Application-layer threat protection
  - The `WAF` allows organizations to create rules and filters to `accept or reject incoming requests` to Amazon CloudFront distributions, Amazon API Gateway deployments, and Application Load Balancers, and HTTP/HTTPS traffic to web servers.
- Security groups
  - Security groups must be designed to `allow ingress traffic from associated security groups`.
- Network ACL
  - Design network `ACLs` to implement `zone-based models` for your workload (web/app servers/database), allowing only legitimate traffic to reach each subnet.

# Detective Controls

Detective controls at AWS include the following security services:

- VPC Flow Logs
  - A feature of Amazon VPC that monitors network traffic at the elastic network interface, subnet, or entire VPC. Captured network traffic can be used for troubleshooting connectivity issues and to check current network access rules.
- AWS CloudTrail
  - Continuously monitor and record API usage and user activity across AWS infrastructure.
- AWS CloudWatch
  - Monitors AWS cloud services such as Amazon RDS databases, EC2 instances, and DynamoDB tables and hosted applications by collecting and tracking metric data, application and operating system log files, and using automated responses to defined alarms.
- Amazon GuardDuty
  - Provides continuous threat detection and analysis of VPC Flow Logs, Amazon Route 53 DNS query logs, and AWS CloudTrail S3 data event logs, and protecting AWS accounts and data stored in Amazon S3 from malicious activity. AWS GuardDuty malware protection can help detect malicious files stored on EBS volumes, protecting attached EC2 instances and Amazon Elastic Kubernetes Service (EKS) clusters.
- AWS Config
  - Detects configuration changes in RDS AWS infrastructure including Amazon RDS, EC2 instances, VPC and database architecture, including security groups, database instances, snapshots, and subnet groups.
- Amazon Macie
  - Uses machine learning and pattern matching to protect Amazon S3 objects and sensitive data types.
- Access Analyzer for S3
  - Monitors Amazon S3 buckets and details public or cross-account access.
- Amazon Detective
  - Graphically analyzes AWS CloudTrail management events, VPC Flow Logs, AWS GuardDuty findings, and Amazon EKS audit logs to help identify the cause of potential security issues.

# Encryption in Transit

- AWS SDKs and the AWS Command Line Interface (AWS CLI) automatically use the default endpoint for each service per AWS Region, but an alternative endpoint can be specified for API requests.
- Most AWS services have regional endpoints that can be used to make requests.
- Global endpoints are used for global services and services located in edge locations.
- The global AWS services are:
  - Amazon CloudFront
  - AWS Global Accelerator
  - AWS Identity and Access Management (IAM)
  - AWS Organizations
  - Amazon Route 53
  - AWS Shield Advanced
  - AWS WAF Classic
- HTTP endpoints for domains and hosted workloads hosted at AWS can be be blocked with Security Groups and Network ACLs and can automatically be redirected to HTTPS endpoints when using Amazon CloudFront or an Amazon ELB.
