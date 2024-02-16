Amazon FSx for Windows File Server
---

- is `supported by EC2 instances and containers`, as well as `Amazon WorkSpaces` instances.
- also supports the use of the Distributed File System (DFS) namespace. - `integrates with on-premises Microsoft Active Directory` and with AWS Managed Microsoft AD.
- Specify the level of redundancy by selecting either a `Single-AZ or Multi-AZ` deployment.
- file systems `can be accessed` from servers located in select `VPCs or from an on-premises server` using either a `VPN or a Direct Connect` connection.

# Features of FSx

## Single-AZ deployment

- FSx `automatically replicates data within the selected availability zone`.
- FSx uses the Windows Volume Shadow Copy Service to create daily backups stored in Amazon S3.
- Multi-AZ deployment
- Each AZ has a dedicated file server.
- All file changes are `synchronously replicated` to both file servers in each AZ.
- FSx falls back to the preferred file server in the preferred AZ.
- Failover and recovery typically take less than `30 seconds.`
- Automatic failover occurs when any of these situations occur:
  - Availability zone outage
  - The preferred file server is unavailable
  - The preferred file server is down due to maintenance

## Throughput

- FSx file servers use an `in-memory cache` for accessing active files to maintain performance.
- Storage choices include SSD storage, which provides sub-millisecond file operations, or HDD storage, which provides single-digit-millisecond performance.
- FSx throughput capacity can be adjusted from 8 MiB/s to 2,048 MiB/s. Network baseline capacity ranges from 16 MiB/s to over 3,000 MiB/s.
- An FSx file system configured with 2 TiB of hard disk drive storage capacity and 32 MiB/s throughput capacity has the following throughput parameters:
  - Network throughput of 32 MiB/s baselines and bursting up to 600 MiB/s when required
  - Disk throughput of 24 MiB/s baselines and 160 MiB/s when required

## Windows Shares

- FSx is `built using Windows file servers and accessed using SMB` Version 2.0 to 3.11, allowing you to support older Windows 7 clients and Windows Server 2008 up to present-day versions.

## File system

- FSx file systems, `built on SSDs`, can be up to 64 TIB in size with more than 2 MIB/s of throughput.
- `Multi-AZ support` for FSx allows you to use the Microsoft DFS namespace to replicate between multiple locations with up to 300 PB of storage.

## Redundancy

- FSx `data is stored within a single AZ or multiple AZs`.
- `Incremental snapshots` are automatically taken every day.
- `Manual snapshots` are supported for additional redundancy concerns.

## Data Deduplication

- Data deduplication can be enabled with `compression to automatically reduce costs for redundant data records` storing duplicated files.

## Active Directory

- Existing Microsoft Windows environments can be integrated with Active Directory deployments and FSx file systems; end users can use their existing identities for access to FSx resources.
- Your Active Directory deployment can be self-managed or hosted and deployed using Managed AD Directory Services for Microsoft Active Directory.

<h2 style="background-color:lightgreen">Amazon FSx for Windows File Server Cheat Sheet</h2>

- FSx supports the SMB protocol, allowing connections to EC2 instances and ECs containers, VMware Cloud on AWS, and Linux and Windows applications.
- FSx supports all Windows versions from Windows Server 2012 and Windows 7 forward.
- FSx supports on-premises access via AWS Direct Connect or AWS VPN connections.
- FSx supports access across multiple VPCs using VPC peering or AWS Transit Gateway connections.
- FSx file systems are encrypted automatically at rest and in transit with keys managed by AWS Key Management Service.
Daily backups are automatically stored in S3 storage.
- FSx is integrated with the AWS Backup service.

