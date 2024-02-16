Amazon S3 Glacier Storage at Rest
---

- Objects stored in Amazon S3 Glacier are `automatically encrypted using SSE and AES-256 encryption`.
- Amazon S3 Glacier Vault Lock enables you to `deploy and enforce regulatory and required compliance controls` by applying a Vault Lock policy on an Amazon S3 Glacier vault.
- Once a WORM policy has been applied to an S3 Glacier vault, the `policy cannot be changed`.
> Note:  Both EFS and FSx use AES-256 encryption to encrypt EFS data and metadata at rest. When your file system is mounted, you can also encrypt your EFS data in transit with TLS. FSx also supports the encryption of data in transit on file shares mapped on a computer instance that supports SMB Version 3.0 or newer. Encryption of data records at rest is automatically enabled when an FSx file system is created.

# Data Backup and Replication

Amazon S3 object backups can be carried out with the services and utilities:

AWS Services    | Use         | Data Types
--              | --          | --
AWS Backup      | Back up all AWS storage services  | EBS volumes and snapshots, S3 buckets, EFS, FSx for Windows File Server, RDS, DynamoDB
Amazon S3 Same-Region Replication (SRR) | Replicate objects to an S3 bucket in the same AWS region  | Objects and versioned objects
Amazon S3 Cross-Region Replication (CRR)  | Replicate objects to an S3 bucket in a different AWS region | Objects and versioned objects
Amazon S3 Multi-Region Access Points  | Replicate data sets across multiple AWS regions | Objects and versioned objects
AWS DataSync  | Copy data to and from AWS storage services  | Network File System (NFS) or Server Message Block (SMB) shares, Hadoop Distributed File Systems (HDFS), AWS Snowcone, S3 buckets, EFS, FSx for Windows File Server

