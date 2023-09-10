Storage
=============

# Storage Types

## [Block Storage](./block-storage.md)

## File Storage

- Network-Attached Storage (NAS) server
- File sharing with file system

## [Object Storage](./object-storage.md)

- Vast scalability and metadata characteristics
- Store `virtually limitless` amounts of data.

# Data Movement

- Hybrid Storage
- Streaming Data
- File Data
- WAN Acceleration
- Private Networks
- Third-Party Applications
- Physical Appliances

# Data Security & Management

- Data Discovery & Protection
- Data Visualization
- Serverless Computing
- Automation
- Audit Trails
- Monitoring & Metrics
- Access Controls
- Encryption

# Storage Fundamentals

## Data Dimensions

Think in terms of data storage mechanism that is most suitable.

### Velocity

- `Speed` at which data is being `read or written`

### Variety

How structured the data is and how many different structures exist in the data.

- `Highly structured` data has a predefined schema
- `Loosely structured` data has entities, which have attributes/fields.
- `Unstructured` data does not have any sense or structure.
- `BLOB` data is useful as a whole.

### Volume

- Total size of the dataset.

## Storage Temperature

- How `“lively”` the data is: how much is being written or read and how soon it needs to be available.

- `Hot` data is being worked on actively.
- `Warm` data is still being `actively accessed`, but less frequently than hot data.
- `Cold` data still needs to be `accessed occasionally`, but updates to this data are rare, so reads can tolerate higher latency.
- `Frozen` data needs to be `preserved` for business continuity or for `archival` or regulatory reasons, but it is not being worked on actively.

## Data Value

### Transient Data

- Often `short-lived`
- Example; `clickstream` or `Twitter data`

### Reproducible Data

- Contains a `copy of useful information` that is often created to improve performance or simplify consumption, such as adding more structure or altering a structure to match consumption patterns.
- Examples; `Data warehouse` data, read replicas of OLTP.

### Authoritative Data

- Source of truth.

### Critical or Regulated Data

- Business must retain at almost any cost.

# AWS Shared Responsibility Model and Storage

- AWS is responsible for:
  - Securing the storage services
- Developer is responsible for:
  - Securing Access using the principle of least privilege
  - Using encryption
  - Ensure that read and write access are separated and controlled.

# Confidentiality, Integrity, Availability (CIA) Model

- `Confidentiality`
  - Privacy level of your data.
  - Levels of encryption or access policies for your storage or individual files.
- `Integrity`
  - Whether your data is trustworthy and accurate.
  - Restrict permission of who can modify data and enable backup and versioning.
- `Availability`
  - Availability of a service on AWS for storage, where an authorized party can gain reliable access to the resource.
  - Restrict permission of who can delete data, enable multi-factor authentication (MFA) for Amazon S3 delete operation, and enable backup and versioning.

# 