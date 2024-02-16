Amazon Elastic Block Store (EBS)
---

- is a `block-level storage` service for `use with Amazon EC2` instances.
- It provides `persistent storage`, and it can be configured to deliver high levels of I/O performance.

# EBS Volume

- `attached to EC2 instances` and are exposed as block devices.
- can be used as raw block devices or can be formatted with a file system and used to store files.
- can also be backed up by creating `snapshots of each EBS volume` that are `stored in Amazon S3` as a `point-in-time backup`.
- `Multiple EBS volumes` can also be attached `to a single EC2` instance.
- Multi-Attach
  - allows up to `16 Nitro-backed EC2 instances to concurrently attach to a single EBS volume` at the same time.
  - is only `supported on Amazon EBS Provisioned IOPS SSD io1 and io2 volume` types and is supported on a limited number of EC2 instance types.
- Boot and data records should always be separated.
- The “E” in EBS defines the “elastic volumes” feature that enables you to increase your current volume capacity and performance or `change your volume after an EBS volume has been created`.

## EBS Volume - Increase Capacity Dynamically

- Amazon CloudWatch metrics and alarms can be used to define and monitor a desired baseline for each EBS volume.
- When baseline values for capacity or performance have been breached, Amazon CloudWatch alarms can alert the Simple Notification Service (SNS).
- SNS, in turn, can notify Amazon Lambda, which can execute a custom function to increase capacity and performance or carry out any specific task as required.
- When an EBS volume is created, the blocks for the volume are `spread across multiple storage arrays`, providing a high level of redundancy and durability.
- EBS volumes are `stored within the same availability zone` (AZ) `where your instances reside` providing 99.8% to 99.999% durability, depending on the type of EBS volume created.

Performance Specifications for EBS Volume Types
---

Parameter | EBS Provisioned IOPS SSD Block Express  | io2 | io1 | gp3 | gp2
--  | --  | --  | --  | --  | --
Use case  | SAP HANA  | I/O-intensive NoSQL | I/O-intensive NoSQL | Virtual desktops  | Single-instance databases
Durability  | 99.999% | 99.999% | 99.8%–99.9% | 99.8%–99.9% | 99.8%–99.9%
Size  | 4 GB–64 TiB | 4 GB–16 TiB | 4 GB–65 TiB | 1 GB–16 TiB | 500 GB–16 TiB
Max IOPS/volume | 256,000 | 64,000  | 64,000  | 16,000  | 16,000
Max IOPS/instance | 260,000 | 160,000 | 260,000 | 260,000 | 260,000
Max throughput/volume | 7,500 MiB/s | 4,750 MiB/s | 7,500 MiB/s | 7,500 MiB/s | 7,500 MiB/s

General Purpose SSD (gp2/gp3)
---

- If a gp2 volume runs out of I/O credits, its I/O performance will be limited to the baseline level until it earns more I/O credits.
- `Bursting` is designed for the `use case where applications have periods of idle time followed by periods of high IOPS`.
- The smallest `gp2 drive can burst to 3,000 IOPS` while maintaining a single-digit-millisecond latency with throughput up to 160 MiB/s.
- General Purpose SSD `gp3 volumes do not support bursting` but include 3000 IOPS per second and 125 MiB/s of consistent performance at no additional cost. EBS volumes created with the desired IOPS value meet their desired performance requirements 99.9% of the time.

<h2 style="background-color:lightgreen"># Amazon EBS Cheat Sheet</h2>

- EBS volumes are network-attached storage volumes attached to an EC2 instance.
- There are eight volume types:
  - Provisioned IOPS SSD (io2 Block Express, io2, io1)
  - General Purpose SSD (gp2, gp3)
  - Throughput Optimized (st1)
  - Cold HDD (sc1)
- EBS volumes support three storage categories: SSD storage for transactional workloads, HDD storage for cold storage and throughput optimized workloads, and magnetic hard drives.
- Multiple EBS volumes can be attached to a single EC2 instance.
- EBS volumes can be attached and detached from a running EC2 instance.
- EBS volumes must be in the same AZ where the EC2 instance is located to be attached.
- Use AWS Backup to back up your attached EBS volumes with EBS snapshots on a schedule.
- By default, root EBS volumes are set for deletion on termination.
- By default, non-boot volumes are not deleted on termination.
- EBS data volumes should have a snapshot schedule in place for backing up EBS data volumes as required.
- Don’t store application data on your root EBS boot volumes.
- EC2 instances can be created with encrypted EBS boot and data volumes.
- EBS volumes allow volume size, volume type, and IOPS changes while online.
- Create separate EBS volumes for boot volumes.
- Ephemeral storage volumes are faster than EBS volumes for storing temporary files.

# EBS Snapshot

- can be used to `recover data` in the event of data loss, corruption, or accidental deletion, or to create new EBS volumes with the same data as the original volume.
- can be used to `migrate data from one AWS region to another`, or to create a new EBS volume in a different Availability Zone or region for `disaster recovery` purposes.
- is a `point-in-time copy of an EBS volume`.
- are `stored in controlled Amazon S3` object storage linked to your AWS account.
- `Controlled storage means that AWS creates and manages the S3 storage location`, but each customer has access to their snapshots through the EBS console or CLI.
- `can be shared` by modifying the permissions of the snapshot.
- can be shared publicly or privately with other AWS accounts using the EC2 Dashboard, selecting Private or Public Snapshots.

## EBS Snapshot Process

- The first time a snapshot of an EBS volume is taken, every block of the EBS volume is part of the primary snapshot captured and stored in controlled S3 storage.
- From this point forward, every additional snapshot is created as an `incremental snapshot` that records all the changes since the last snapshot.
- Only newly written and changed volume blocks are pushed to the incremental snapshot.
- When you delete a snapshot, only the data exclusive to the snapshot copy is retained.
- Each snapshot has a unique identifier, and new EBS volumes can be created from any snapshot.

## Fast Snapshot Restore (FSR)

- is a feature of Amazon EBS that enables you to `quickly restore an EBS volume from a snapshot`, creating a new volume from the snapshot and attaching it to an Amazon Elastic Compute Cloud (EC2) instance.
- enables you to `skip the process of creating a new volume and then copying the data` from the snapshot to the new volume.
- Instead, the `new volume is created directly from the snapshot`, which can save a significant amount of time.
- enables you to speed up restoring data to multiple EBS volumes from a snapshot.
- has been designed to help speed up the snapshot restore process for virtual desktop environments and custom AMIs.

## Snapshot Administration

- Within an AWS region
  - Snapshots can be used to create an EBS volume within any AZ within the same region where the snapshot is stored.
- To another AWS region
  - By using the EBS copy utility via the AWS CLI or Amazon Data Lifecycle Manager, snapshots can be copied to multiple AWS regions.
- Launching EC2 instances
  - EBS boot volumes can be used to create a new EC2 instance.
- Rebuilding a database
  - AWS RDS database instance snapshots can be used to create a new database instance.
- Creating volumes
  - Existing snapshots can be used to create new EBS volumes.

## EBS Recycle Bin

- enables you to `recover EBS snapshots and volumes` that were deleted within the `past 90 days`.
- When an EBS snapshot or volume is deleted, it is moved to the Recycle Bin, where it can be recovered if needed.
- To use the EBS Recycle Bin, you must first `enable the feature` in the AWS Management Console.
- View and recover deleted snapshots and volumes by navigating to the EBS Dashboard and select the Recycle Bin, selecting the snapshots or volumes that you want to recover.
- Both tag-level and region-level retention rules are supported.

<h2 style="background-color:lightgreen">Snapshot Cheat Sheet</h2>

- Snapshots are `saved incrementally` in Amazon S3 controlled storage.
- Snapshots are region-specific, whereas EBS volumes are AZ-specific.
- A snapshot can be copied to another AWS region.
- Snapshots can be archived for low-cost, long-term retention.
- When a snapshot is encrypted, encryption keys are created and managed by the AWS Key Management Service (KMS).
- Snapshots use AES-256 encryption.
- The Amazon Data Lifecycle Manager can be used to create a snapshot management schedule that controls the creation and deletion of snapshots.
- The Amazon Data Lifecycle Manager can be used to create a snapshot management schedule that stores snapshots across multiple AWS Regions.
- Snapshots that have accidently been deleted can be restored from the EBS Recycle Bin.
- EBS snapshots can be stored locally in a local AWS Outposts deployment.
