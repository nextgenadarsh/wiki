Block Storage
================

- Analogous to direct-attached storage (DAS), Storage Area Network (SAN)

# Amazon EBS

- Ultra-low latency, durable, persistent
- Automatically replicated within its AZ
- `Pay only for` what you `provision`
- Features:
  - Availability of 99.999 percent
  - Durability of replication within a single availability zone
  - `Annual failure rate` (`AFR`) of between 0.1 and 0.2 percent
- Usage:
  - `Boot volumes` on Amazon EC2 instances
  - Relational and NoSQL databases
  - Stream and log processing applications
  - Data `warehousing` applications.
  - Big data analytics engines (like the Hadoop/HDFS (Hadoop Distributed File System) ecosystem and Amazon EMR clusters)

## EBS Volumes

- Persist independently from the running life of an Amazon EC2 instance.
- You can `dynamically increase size`, modify provisioned IOPS capacity, and change the volume type on live production volumes `without service interruptions`.

### EBS Volume Types

#### SSD-backed Volumes

- Optimized for `transactional workloads` involving `frequent read/write` operations with `small I/O size`, where the dominant performance attribute is IOPS.

#### HDD-backed Volumes

- Optimized for `large streaming workloads` where throughput (measured in MiB/s) is a better performance measure than IOPS.

#### SSD vs HDD Volumes

|    | SSD General Purpose | SSD Provisioned IPS   | HDD Throughput Optmized  | HDD Cold
| -- | --  | --    | --    | --
| Max Volume Size | 16 TiB  |   
| Max IOPS/Volume| 10000  | 32000 | 500 | 250
| Max Throughput/Volume | 160 MiB/Sec | 500 MiB/Sec |  | 250 MiB/Sec
| Use Cases | Most workloads, Boot Volume, VDI, Apps, Dev/Test Environment | I/O intensive, NoSQL/Relational DBs | Streaming workloads, Big Data, Data warehouse, Log processing, Can't be boot volume | Infrequently accessed throughput oriented workload, Lowest storage cost, Can't be boot volume

## Elastic Volumes

- Feature of EBS which allows you to increase capacity dynamically.

## EBS Snapshot

- Protect your data by creating point-in-time snapshots of EBS without attaching/detaching and store in S3 for long term durability.
- Snapshots are `incremental backups`, making this a cost-effective way to back up your block data.
- Snapshot deletion process is designed so that you need to retain only the most recent snapshot to restore the volume.

## EBS Optimization

- On Amazon EBS–optimized instances, traffic between instance and EBS uses dedicated network.

## EBS Encryption

- Supports encryption for data at rest
- Uses `AES-256` and `AWS KMS` for encryption of data in transit
- Snapshots of encrypted Amazon EBS volumes are automatically encrypted

## Amazon EBS Performance

- Use Amazon EBS-optimized instances
- Understand how performance is calculated
- Understand your workload
- Be aware of the performance penalty when initializing volumes from snapshots
- Factors that can degrade HDD performance
- Increase read-ahead for high-throughput, read-heavy workloads
- Use RAID 0 to maximize utilization of instance resources
- Track performance with Amazon CloudWatch

# Amazon Instance Store

- Provides `temporary` block-level storage, and the storage is `located on disks that are physically attached` to the host computer.

## Instance Store Volumes

- Should not be used for persistent storage.
- Ephemeral (short-lived) storage that does not persist if the instance fails or is terminated.
- Not all instance types come with available instance store volume(s), and the size and type of volumes vary by instance type.
- You must `enable these volumes when you launch` an Amazon EC2 instance, as you cannot add instance store volumes to an Amazon EC2 instance once it has been launched.
- Cannot access them until they are mounted.

## Instance Store–Backed Amazon EC2 Instances

- Instance store–backed Amazon EC2 instances cannot be stopped and cannot take advantage of the auto recovery feature for Amazon EC2 instances.

