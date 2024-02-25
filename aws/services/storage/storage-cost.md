Storage Types and Costs
---

Storage costs at AWS depend on the storage service being used—whether it’s EBS storage volumes, shared file storage using Amazon EFS or Amazon FSx for Windows File Server, Amazon S3 object storage, or archival storage using Amazon S3 Glacier. The following list describes these AWS storage options and storage and data transfer costs:

# Amazon S3 buckets: An S3 bucket has monthly storage and retrieval costs based on the storage class and location of the request. Other costs are based on the frequency of operation. PUT, COPY, POST, and LIST requests per 1,000 requests for S3 Standard is $0.005. GET, SELECT, and all other requests per 1,000 requests for S3 Standard is $0.004. S3 lifecycle and data transfer requests are charged per 1,000 requests. There are no data transfer charges for storing and retrieving objects from an S3 bucket located in the same region where the EC2 instance is located.
Optional Amazon S3 features such as S3 Lifecycle transitions, data transfer (outbound directly to the Internet or to Amazon CloudFront), S3 Transfer acceleration, and Cross-Region replication to another S3 bucket all have separate and additional costs. Amazon S3 bucket replication within or across AWS regions also has specific bundled costs:
- S3 Same-Region Replication (SRR): Amazon S3 charges for storage in the selected destination Amazon S3 storage class, the primary copy, replication PUT request, and if applicable, an infrequent access storage retrieval charge.
- S3 Cross-Region Replication (CRR): S3 charges for storage in the selected destination S3 storage class, the primary copy, replication PUT requests, and if applicable, an infrequent access storage retrieval charge, and inter-region data transfer out to the selected region.
As an example, storing 500 TiB of standard storage in the us-east-1 (Northern Virginia) region would cost you roughly $12,407.14 per month (see Figure 12-12). It would include 5,000 PUT/COPY/POST/LIST requests and 30,000 GET requests.

# Amazon S3 Glacier

- S3 Glacier archive storage ranges from $0.04 to under $0.01 for archival storage in S3 Glacier Deep Archive:
- S3 Glacier Instant Retrieval storage costs $0.004 per GiB when accessed every 90 days
- Amazon S3 Glacier Flexible Retrieval storage with retrieval from 1 minute to 12 hours ($0.0036 per GiB)
Amazon S3 Glacier Deep Archive storage that is accessed once or twice a year and is restored within 12 hours ($0.004 per GiB)
Amazon S3 Glacier storage is also subject to storage and retrieval pricing that is based on the speed of the data retrieval required. In addition, it is subject to outbound data transfer pricing, which varies based on the destination (for example, outbound directly to the Internet or to CloudFront). A recommended practice is to archive infrequently used data in S3 Glacier Flexible Retrieval and move long-term archived data to Glacier Deep Archive. Storing 100 TiB of archived records in the US-East (Northern Virginia) region with data retrieval of 10 GiB per month and an average of 20 requests per month would cost roughly $411.92.

# EBS volumes: Virtual hard drives can be ordered in several flavors: SSDs, SSDs with provisioned IOPS, throughput-optimized drives, or cold HDDs (infrequently accessed hard drive storage). You are also charged for snapshot storage in Amazon S3 for EBS volume snapshots.
For example, a single general-purpose SSD sized at 16,384 GiB hosted in the US-East-1 (Northern Virginia) region would cost you roughly $1,798 per month. A provisioned IOPS SSD io1 volume sized at 8,000 GiB with 16,000 IOPS hosted in the US-East-1 (Northern Virginia) region would cost you $2,244.50 per month, as shown in Figure 12-13. Note that all prices quoted are subject to change over time.

# Snapshot storage: Snapshot storage costs can be extremely high if snapshots that are no longer required are not deleted. Amazon Data Lifecycle Manager, which is found in the EBS section of the EC2 console, allows you to schedule and manage the creation and deletion of EBS snapshots.

# Shared storage (EFS/FSx for Windows File Server): Amazon EFS and Amazon FSx for Windows File Server are shared file storage services. At a minimum, you pay for the total amount of storage used per month. EFS Infrequent Access storage is priced based on the amount of storage used and the amount of data accessed. You can also optionally pay for faster-provisioned throughput in megabytes per month, depending on your performance requirements. FSx for Windows File Server usage is prorated by the hour, and customers are billed for the average usage each month, paying for the storage and throughput capacity specified and for any backups performed. FSx for Windows File Server customers pay for data transferred across AZs or peering connections in the same region and for data transferred out to other AWS regions.
As an example for EFS, suppose a file system hosted in the US-East-1 (Northern Virginia) region uses 300 GiB of storage for 20 days for a single month. The charges would be as follows: total usage (GiB-hours) = 300 GiB × 20 days × (24 hours/day) = 144,000 GiB-hours. The total charge equates to $43.20 per GiB-month. Moving your files to the EFS Infrequent Access storage tier would reduce your EFS storage costs by up to 92%.

# Amazon S3, EBS, EFS, and FSx for Windows File Server Comparison

Feature | Simple Storage Service (S3) | Elastic Block Store (EBS) | Elastic File System (EFS) | FSx for Windows File Server
--  | --  | --  | --  | --
Costs of storage  | Scaled cost based on the first 50 TiB of storage used and the number of requests made (POST, GET) Data transfer per GiB out of S3 | General-purpose SSD: $0.8 per GiB per month. Provisioned IOPS SSD: $0.125 per GiB per month; $0.065 per provisioned IOPS per month. Throughput-optimized HDD: $0.045 per GiB per month. Cold HDD: $0.015 per GiB per month | Standard storage: $0.03 per GiB per month. Infrequent access storage: $0.045 per GiB per month. Infrequent Access requests: $0.01 per GiB transferred | SSD storage: $0.230 per GiB per month. HDD storage: $0.025 per GiB per month. Throughput capacity: $4.500 per MiBps per month
Storage size  | No limit  | Maximum storage size 65 GiB | Petabytes | Petabytes
Storage classes | Standard, Intelligent-Tiering, Standard IA, One Zone IA, Glacier Instant/Flexible Retrieval/Deep Archive  | General-purpose SSD, Provisioned IOPS SSD io1, io2, Throughput optimized HDD volumes, Cold HDD volumes  | EFS Standard or Infrequent Access and EFS One Zone or One Zone Infrequent Access  | Single AZ and Multi-AZ deployment options
File size | 5 TiB | 64 TiB maximum volume size  | 47.9 TiB single file  | 47.9 TiB single file
How to reduce storage costs | Intelligent-Tiering, One Zone-Infrequent Access | Reduce volume size and type, reduce IOPS  | Provisioned throughput, EFS Infrequent Access (EFS Standard-IA or EFS One Zone-IA)  | HDD and SSD storage options, data deduplication, user quotas
Backup Tools  | Cross-Region and Same-Region Replication  | Snapshots, Data Lifecycle Manager | EFS Lifecycle Management, EFS Intelligent-Tiering | Automated backups to S3
Associated AWS service  | AWS Backup, Snow Family | AWS Backup, EFS to EFS, or S3 backup with Lambda function | AWS Backup  | AWS Backup
Data location | Data stays within the region or requested AZ  | Data stays within the same AZ | Data stored within AZs of region  | Data stored within AZs of region
Data access options | Public (HTTP, HTTPS) or private network endpoints (Gateway) | Private AWS network from an EC2 instance  | Private network from multiple instances or from on-premises locations | Private network from multiple instances or from on-premises locations
Encryption  | SSE: Amazon S3, AWS-KMS, SSE-C  | AWS and KMS: managed (CMK) with AES 256-bit encryption  | AWS and KMS: managed CMK with AES 256-bit encryption  | AWS and KMS: managed CMK with AES 256-bit encryption
Availability  | Four 9s; can survive the loss of two facilities | EBS volumes unavailable during AZ failure | Stored across multiple AZs  | Stored across multiple AZs
Use Case  | Static files  | Boot drives, database instances SQL, NoSQL  | Big data analytics, media workflows (media editing, studio production), or home directories | Big data analytics, media workflows (media editing, studio production), or home directories

# AWS Backup

AWS Backup is a centralized backup service for managing data backups across multiple AWS regions for AWS compute, storage services, and database services (see Figure 12-14). Backups can be on-demand, scheduled, or continuous. A continuous backup includes a continuous backup of Amazon RDS database instances and continuous backup of the transaction logs. Continuous backups can restore RDS deployments with a point-in-time recovery (PITR) within 5 minutes of activity within a defined 35-day time period. Amazon S3 buckets can be restored within 15 minutes of recent activity. Backups can also be automated per EC2 instance with crash-consistent backups of attached EBS volumes. AWS Backup also integrates with AWS Organizations.

The following AWS services can be backed up with AWS Backup:

EBS volumes
EC2 instances and Windows applications (including Windows Server, Microsoft SQL Server, and Microsoft Exchange Server)
Amazon RDS databases (including Aurora clusters)
DynamoDB tables
Amazon Elastic File System file systems
Amazon FSx for Windows File Server file systems
Amazon FSx for Lustre, ONTAP, and OpenZFS file systems
Neptune and DocumentDB clusters
AWS Storage Gateway – Volume Gateway
Amazon S3 buckets, objects, tags, and custom metadata
Amazon Outposts, VMware Cloud on AWS, and on-premises VMware virtual machines (require AWS Backup gateway software to be installed on each VMware VM)

You can select templates when creating a backup plan with AWS Backup, or create a new backup plan (see Figure 12-15). When you assign a storage resource to a backup plan, the selected resource is backed up automatically on a defined schedule. A backup plan requires the following information:

- Backup schedule: Every hour (cron expression), 12 hours, daily, weekly, monthly
- Backup window: Starting time and duration
Lifecycle rules: When a backup is transitioned to cold storage and when the backup expires
A backup vault: For storing encrypted backups with KMS encryption keys
Regional copies: Backup copies in another AWS region
Tags: Associating multiple resources with tag-based backup policies

## Lifecycle Rules

AWS Backup can be stored in either a warm or cold storage tier. Lifecycle rules allow customers to transition backups that are stored in warm storage to cheaper cold storage. In us-east-1, warm storage is $0.05 per GiB; cold storage is $0.01 per GiB. The defined lifecycle in each backup plan defines when a backup will transition into cold storage. Each backup stored in cold storage is a full backup. Backups that have transitioned to cold storage must remain in cold storage for 90 days. In Figure 12-16, transition rules have been set to transition the monthly backup to cold storage after 8 days and retain the backup for 1 year.

## AWS Backup Cheat Sheet

A backup of an EC2 instance includes snapshots of all volumes and launch configuration.
A continuous backup allows you to restore RDS deployments any point in time within 35 days within 5 minutes of activity
Periodic backups retain data for the specified duration.
On-demand backups back up the selected resource type at once.
Backup plans create incremental backups.
Incremental backups are lower cost than an on-demand or periodic backup.
The first backup is always a full backup; subsequent backups are incremental.
When an EFS file system is created, automatic backups with AWS Backup are turned on.
AWS Backups are stored in vaults.
AWS Backup vaults are encrypted with KMS encryption keys.
AWS Backup Vault Lock enforces a write-once, read-many (WORM) setting for all backups stored in a backup vault.
AWS Backup Audit Manager audits the compliance of your AWS Backup policies.
Amazon S3 backups require versioning to be enabled.
AWS Backup charges by the GiB-month depending on the amount of resource type stored and restored per month.
The AWS Backup lifecycle feature automatically transitions your recovery points from a warm storage tier to a lower-cost cold storage tier for backups of Amazon EFS file systems, DynamoDB tables, and VMware virtual machines.
Individual files can also be restored without having to restore the entire file system.

# Data Transfer Costs

There is no charge for inbound data transfer into AWS from the Internet, from an edge location, or Direct Connect connection.

- When data is transferred to the Internet from an AWS service, data transfer charges apply based on the service and the AWS region where the service is located.
- Data transfers across the Internet are billed at AWS region-specific and tiered data transfer rates.
Data transferred into and out from Amazon EC2, Amazon RDS, Amazon Redshift, DynamoDB, Amazon ElastiCache instances, an Elastic Network Adapter, or VPC peering connections across AZs in the same AWS region is charged at $0.01/GiB in each direction.
Data transferred across regional endpoints between Amazon S3, Amazon S3 Glacier, DynamoDB, Amazon Simple Queue Service (SQS), Amazon Kinesis, Amazon Elastic Container Registry (ECR), Amazon SNS, and Amazon EC2 instances in the same AWS region is free of charge. However, if data is transferred across a PrivateLink connection, VPC endpoint, AWS NAT Gateway Service, or AWS Transit Gateway, data transfer charges will apply.

## What Type of Data Do You Need to Transfer from On Premises to AWS?

Data Type | Transfer Option | Costs
--  | --  | --
Virtual server images | AWS Application Migration Service, AWS Server Migration Service (SMS) | Free for the first 90 days for each server migrated. EC2 and EBS charges.
Database  | AWS Database Migration Service (DMS)  | Data transfer into AWS DMS is free. Data transferred between DMS and databases in RDS and EC2 instances in the same AZ is free.
Bulk storage files  | AWS Transfer Family (SFTP, FTPS, and FTP) | $0.30 per hour for enabled service. $0.04 per gigabyte for the amount of data uploaded/downloaded.

## Where Will On-Premises Data Be Stored at AWS?

Data Usage  | Storage Options
--  | --
Daily use at AWS  | Amazon S3, Amazon EFS, or FSx for Windows File Server
Archived storage  | Amazon S3 Glacier
Stored long-term  | Amazon S3 Glacier Deep Archive

## How Much Data Needs to Be Transferred?

Data Size | Data Transfer Option
--  | -- 
Gigabytes | AWS Transfer Family
Terabytes | AWS Snowball, AWS Snowcone, or AWS Snowball Edge
Exabytes  | AWS Snowmobile

## What Data Transfer Method and Hybrid Solution Could You Choose?

Private Network Connection to AWS | AWS Direct Connect
Edge location transfer  | S3 Transfer Acceleration
Internet transfer | AWS DataSync or AWS Transfer for SFTP
Offline data transfer | AWS Snowball, AWS Snowball Edge, or AWS Snowmobile
Hybrid storage  | AWS Storage Gateway

Options for moving data records from on-premises locations into the AWS cloud are as follows:

- AWS Direct Connect: AWS Direct Connect allows you to create a private single-mode fiber connection from your on-premises data center or a co-location into AWS; a connection can be partitioned into up to 50 private virtual interfaces connecting to public and VPC resources at AWS.

- AWS DataSync: AWS DataSync can automate the movement of large amounts of data from on-premises locations to either Amazon S3 buckets or Amazon EFS storage across the Internet, or with an AWS Direct Connect or AWS VPN connection. Both one-time and continuous data transfers are supported using the NFSv4 protocol. Parallel processing creates fast data transfers using an AWS DataSync virtual machine agent downloaded and installed on your network. The first step is to create a data transfer task from your on-premises data source (NAS or file system) to the selected AWS destination, and then start the transfer. Data integrity verification is continually checked during the data transfer; data records are encrypted using Transport Layer Security (TLS). AWS DataSync supports both PCI DSS and HIPPA data transfers.

- The AWS Snow Family: The Snow family includes AWS Snowcone, AWS Snowball, and AWS Snowball Edge network-attached devices, or an AWS Snowmobile truck with a 40-foot storage container. Configuration involves logging in to the Snowball dashboard to create a job, selecting the parameters of the Snow device you wish to order, and select the S3 bucket that will store the locations of the Snow device once it is shipped back to AWS. When data has been moved to the selected S3 bucket and verified, the Snow device is securely erased and sanitized, removing all customer information. AWS Snow pricing is based on data transfer job fees, the commitment period, data transfer, and storage and shipping fees. Data transfer into Amazon S3 from an external location is free. The following Snow Family options are available:

  - AWS Snowcone: This is the smallest member of the Snow Family, with two vCPUs, 4 GiB of memory, and 8 TiB of object or block storage. It also has wired network access and USB-C power.
  - AWS Snowball: Petabyte data transfer is possible using multiple Snowball devices; each device can hold either 42 TiB or 80 TiB of object or block storage. After you create a job request, as shown in Figure 12-17, a Snowball device will be shipped to you via UPS. When you receive the device, hook it up to your network using an RJ-45 connection. The Snowball client software must be installed, and predefined security information must be entered before data transfer begins. After the data is transferred into the Snowball device, the device is shipped back to AWS and the device’s data is deposited into an S3 bucket. This process can also be reversed, transferring object data from AWS back to your on-premises location. All data that is transferred to Snowball is encrypted with 256-bit encryption keys defined using AWS Key Management Service (KMS). The following use case options are available for Snowball devices:
    - Compute-optimized Snowball: 42-TiB GPU option for machine learning or advanced video analysis use cases ($1,200 to $1,600 per job)
    - Storage-optimized Snowball: Large data transfers and local storage ($300 to $500 per job)
    - AWS Snowball Edge: The Snowball Edge device supports the installation of a local instance to carry out the local processing duties that can be built from your AMIs. Snowball Edge compute options are designed for local data processing within the device with storage for processing or analysis before being stored back at AWS.
    - AWS Snowmobile: Move up to 100 PB of data with an AWS Snowmobile truck. AWS employees show up with a transport truck containing a 45-foot shipping container and attach it to your data center. After the shipping container is filled with data, it is carefully driven back to AWS accompanied by an escort vehicle for safety, and the data is uploaded into S3 storage.
  - AWS Transfer Family: Transfer files into and out of S3 buckets using the SSH File Transfer Protocol (SFTP). Connect existing SFTP software to the SFTP endpoint at AWS, set up user authentication, select an S3 bucket, assign IAM access roles, and transfer data records to AWS.

  