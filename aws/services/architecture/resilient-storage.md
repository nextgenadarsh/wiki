Resilient Storage Options
---

Storage Service | Resiliency | Additional Resiliency
--  | --  | --
Amazon EBS  | Stored within AZ  | EBS volumes copied across regions (AWS DataSync) Snapshots copied across regions (Amazon Data Lifecycle Manager)<br/> Multi-attach EBS volumes (io1)
Amazon EFS  | Multi-AZ deployment  | Sync data across region/on-prem; back up with AWS Backup | Transfer across AWS storage services (AWS DataSync), AWS Backup
Amazon FSx for Windows File Server | Multi-AZ deployment | AWS DataSync, AWS Backup
Amazon RDS | Single AZ | Multi-AZ, cluster (three AZs), read replicas
Amazon Aurora | Six copies across three AZs | Global Database, read replicas
Amazon DynamoDB | Six copies across three AZs | Global Tables, DynamoDB Accelerator (DAX)
Amazon S3 | Across three AZs minimum | Single-region replication, cross-region replication
Amazon Kinesis Data Streams | Multi-AZ | S3 storage
Amazon Kinesis Data Firehose | S3, Amazon Redshift | Analyze using Athena, EMR, and Redshift Spectrum
Amazon Redshift | Multi-AZ | Continual backup to S3
Amazon SQS | Multi-AZ, 1 minute to 14 days retention of messages | Dead letter queue, backup to S3 using Lambda function
Amazon SNS | Multi-AZ, push notifications | DynamoDB

