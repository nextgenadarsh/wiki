
File Storage
==================

# Amazon EFS

- Enable you to share access to files that reside on the cloud.
- Common data source for workloads and application running on multiple instances.
- Use when you need:
  - Multi-attach
  - GB/s throughput
  - Multi-AZ availability/durability
  - Automatic scaling (growing/shrinking of storage)
- Use cases:
  - Web serving
  - Database backups
  - Container storage
  - Home directories
  - Content management
  - Analytics
  - Media and entertainment workflows
  - Workflow management
  - Shared state management

# Creating your own file system

## File System

- Up to 125 file systems per account.
- Belongs to a region and spans all Availability Zones in that region

## Mount Target

- A Network File System (NFS) endpoint within your VPC 
- To access your file system from within a VPC

# Accessing an Amazon EFS File System

## Amazon EC2

- Must mount the file system by using the standard Linux mount command

## AWS Direct Connect

- Mount your on-premises servers to Amazon EFS

# Syncing Files Using AWS DataSync

- Can synchronize your file data and also file system metadata such as ownership, time stamps, and access permissions
- Download and deploy a sync agent from the Amazon EFS console
- Create a sync tack and configure your source and destination file systems.

# Performance

## General Purpose (default)

- Used for latency-sensitive applications and general-purpose workloads
- Limit of 7,000 operations per second

## Max I/O

- Used for large-scale and data-heavy applications
- Provides you with a virtually unlimited ability to scale out throughput and IOPS with latency trade-off

| Mode            | Used for        | Advanatages   | Trade-off   | When to use?
| --              | --              | --            | --          | --
| General purpose | General purpose, latency sensitive | Lowest latency | 7000 ops/sec | Most workloads
| Max I/O     | Large scale, data heavy | Unlimited scale | Higher latency | 10 or more instances accessing

# Security

- You can control security by using:
  - Network traffic to/from file system using:
    - VPC security groups
    - Network ACLs
  - File/directory access using POSIX permission
  - API access to file system using IAM
    - Action level permission
    - Resource level permission

# Storage Comparisons

## Use case comparison

| If you need     | Consider using
| --              | --
| Persistent local storage for EC2, Relation and NoSQL DB, Warehousing, Big Data processing, Backup Recovery | EBS
| File system interface available to more EC2, Media processing workflow, Big Data storage, backup or recovery | EFS
| A scalable, durable platform to make data accessible from any internet location for user-generated content, active archive, serverless computing, Big Data storage, or backup and recovery | S3
| Highly affordable, long-term storage that can replace tape for archive and regulatory compliance | Glacier
| A hybrid storage cloud augmenting your on-premises environment with AWS cloud storage for bursting, tiering, or migration | Storage Gateway
| A portfolio of services to help simplify and accelerate moving data of all types and sizes into and out of the AWS Cloud | Cloud Data Migration Service

# Storage Temperature Comparison

## Comparison of Amazon EBS and Instance Store

|                 | Instance store  | EBS   | S3    | Glacier
| --              | --              | --    | --    | --
| Average latency | ms              |       | ms, sec, min ~size | hrs
| Data volume     | 4 GB to 48 TB   | 1 GiB to 1 TiB | No limit
| Item size       | Block storage   |       | 5 TB max | 40 TB max
| Request rate    | Very high       |       | Low to very high (no limit) | Very low (no limit)
| Cost /GB/Month  | EC2 instance cost | 
| Durability      | Low             | High  | Very high | Very high
| Temperature     | Hottest         | Hot   | Cold      | Coldest

# Cloud Data Migration

- AWS offers a suite of tools to help you move data `via`` networks, roads, and technology partners in and out of the cloud through `offline`, `online`, or `streaming` models.
- To determine the best-case scenario for efficiently moving your data, use this formula:
  ```js
  Number of Days = (Total Bytes)/(Megabits per second * 125 * 1000 * Network Utilization * 60 seconds * 60 minutes * 24 hours)
  ```
## AWS Storage Gateway

- Enables your `on-premises applications to use AWS cloud storage` seamlessly.
- You can use this service for the following:
  - Backup and archiving
  - Disaster recovery
  - Cloud bursting
  - Storage tiering
  - Migration

## File Gateway

- A file interface into Amazon S3
- Combines a cloud service with a virtual software appliance that is deployed into your on-premises environment as a VM

## Volume Gateway

- Cloud-based storage volumes
- Can mount as iSCSI devices from your on-premises application servers
- Supports cached mode and stored volume mode configurations.

### Cached Mode

- Data is stored in Amazon S3

### Stored Volume Mode

- Data is stored on your local storage with volumes backed up asynchronously as Amazon EBS snapshots stored in Amazon S3

## Tape Gateway

- Used for backup to migrate off of physical tapes and onto a cost-effective and durable archive backup such as Amazon S3 Glacier

## AWS Import/Export

- accelerates moving large amounts of data into and out of the AWS Cloud using portable storage devices for transport
- Transfers your data using AWS internal network bypassing internet

## AWS Snowball

- a petabyte-scale data transport solution that uses physical storage appliances, bypassing the internet, to transfer large amounts of data into and out of Amazon S3.

## AWS Snowball Edge

- a 100-TB data transfer service with on-board storage and compute power for select AWS capabilities.


## AWS Snowball vs Snowball Edge

| Use case                      | AWS  Snowball | AWS Snowball Edge
| --                            | --            | --
| Import data into Amazon S3	  | ✓             | ✓
| Copy data directly from HDFS	| ✓             
| Export from Amazon S3	        | ✓             | ✓
| Durable local storage		      |               | ✓
| Use in a cluster of devices		|               | ✓
| Use with AWS IoT Greengrass		|               | ✓
| Transfer files through NFS with a GUI |       | ✓

## AWS Snowmobile

- an exabyte-scale data transfer service used to move extremely large amounts of data from on premises to AWS

## Amazon Kinesis Data Firehose

- Lets you prepare and load real-time data streams into data stores and analytics tools
- Can capture, transform, and load streaming data into destination
- Supports destinations including:
  - Amazon S3
  - Amazon Redshift
  - Amazon Elasticsearch Service
  - Splunk

### Key Concepts

- Kinesis Data Delivery Stream
  - You use Amazon Kinesis Data Firehose by creating an Amazon Kinesis data delivery stream and then sending data to it.
- Record
  - Data that your producer sends to a Kinesis data delivery stream, with a `maximum size of 1,000 KB`.
- Data Producer
  - send records to Amazon Kinesis data delivery streams
- Buffer Size and Buffer Interval
  - Firehose buffers incoming data to size in megabytes or for period in seconds of time before delivering it to destinations
- Data Flow
  - ![Streaming to Amazon S3](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c03f027.jpg)

## AWS Direct Connect

- Used to establish private connectivity between AWS and your data center

## VPN Connection

- Used to connect your Amazon VPC to remote networks


