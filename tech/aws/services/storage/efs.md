Amazon Elastic File System (EFS)
---

- is a fully managed, elastic file storage service that `scales on demand up to petabytes` for Linux, Windows, and macOS instances.
- removes the need to provision and attach EBS volumes for data storage, and `operates as a shared storage` service that allows you to `concurrently serve EC2 instances hosted on subnets` within select VPCs by using `NFS mount points`.
- The key features of EFS include the following:
  - Availability and durability
    - Choose `Regional to store data redundantly across multiple AZs`.
    - Choose `One Zone to store data redundantly within a single AZ`.
  - No networking or file layer to manage
    - There are no EBS drives to provision, manage, and pay for.
    - `Pay for the storage used` and the level of performance.
  - Elastic
    - The EFS file system `automatically scales` as you add and remove files; you do not need to select an initial storage size.
  - Scale
    - EFS can scale to petabytes of capacity and performance can scale along with the increase in size.
  - Performance
    - Two performance modes are available:
      - General Purpose
      - Max I/O
        - is designed `for thousands of instances` that need access to the same files at the same time.
  - Compatible
    - Amazon EFS supports the Network File System (NFS) protocol supported by a wide range of applications and operating systems.
  - Lifecycle management
    - Amazon EFS Intelligent-Tiering automatically transitions files in and out of Standard-infrequent Access storage based on a defined number of days since last access.

# EFS Performance Modes

## General Purpose

- is assigned a throughput performance profile that supports up to 7,000 operations per second per file system deployment.
- is recommended as the starting mode of operation.
- Amazon recommends that you continue to monitor each EFS file system using the CloudWatch metric PercentIOLimit; if the file system is operating close to 100%, choose Max I/O.

## Max I/O
 
  - Max I/O scales to a much higher level of throughput and operations per second and was designed for situations where thousands of EC2 instances are attached to a single EFS file system deployment, or `for big data and data warehousing workloads`.

# EFS Throughput Modes

## Bursting

- Amazon EFS `automatically adjusts the throughput` of the file system up or down `in response to changes in demand`, enabling you to burst to higher levels of throughput when required.
- When the EFS file system throughput remains below the assigned baseline rate, it `earns burst credits` that are saved for future throughput requirements.
- When the file system requires additional throughput, the saved burst credits are utilized for read and write performance throughput above the current baseline.
- New file systems have an initial credit burst balance of 2.1 TiB.
- The overall throughput is designed to increase as the number of stored files increases.
- As files are added to the file system, the amount of throughput allowed is increased based on the allotted file size.
- Using the CloudWatch metric BurstCreditBalance, you can monitor the current burst credit balance.
- Move up to the Provisioned throughput mode with a few mouse clicks.

## Provisioned

- Specify the desired level of throughput for the file system, and Amazon EFS will `automatically provision the necessary resources` to meet the requested throughput.
- Provisioned Throughput can scale up to 3 GiB/s for read operations and 1 GiB/s for write operations per file system deployment.
- Customers are `billed for the EFS storage used` and any throughput that has been provisioned above the baseline.

# EFS Security

- Use `security groups to control the EC2 instance access` to the EFS mount points.
- All data stored within EFS can be `encrypted at rest`, and encryption keys are `managed by AWS KMS`.

# EFS Storage Classes

## Standard

- The default storage class is selected by default.

## Infrequent Access

- is for files that are accessed infrequently but require `rapid access when needed`.
- Transition into the IA tier can be set from 1 day to 90 days since the file was last accessed.
- The Infrequent Access tier provides a `lower storage cost` than the Standard storage tier, but has `higher access fees`.

## One-Zone Infrequent Access

- is similar to the Infrequent Access storage class with the added benefit of being stored in a `single AZ`.
- This can be useful for data that is `not defined as critical`.
- provides a `lower storage cost` than Standard storage and Infrequent Access but has `higher access fees`.

# EFS Lifecycle Management

- provides `cost-effective` file management.
- Files that have not been accessed for a `defined period of time` are `moved to the Standard-Infrequent Access (IA) storage` class from the Standard storage class.
- A `lifecycle policy` defines the period of time which range from 7 to 90 days.
- Files remain in IA storage and are `transitioned out of IA storage when accessed once again`.

<h2 style="background-color:lightgreen"># Amazon EFS Cheat Sheet</h2>

- EFS storage is `accessed using NFS mount points` using the NFS protocol.
- Storage capacity is elastic; you pay for what you use.
- EFS storage can be attached from on-premises systems using a VPN connection or Direct Connect.
- Concurrent connections to an EFS file system can be made from multiple subnets.
- There are two EFS performance modes:
  - General Purpose
  - Max I/O
- Access to files and directories can be controlled with POSIX-compliant user and group-level permissions.
- AWS Key Management Service (KMS) manages encryption keys for encrypting and decrypting the EFS file system.
- Data encryption in transit uses TLS 1.3.
- EFS supports VMware ESXi.
- EFS supports AWS Outposts.

