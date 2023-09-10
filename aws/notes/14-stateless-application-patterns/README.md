Stateless Application Patterns
===

# Introduction to the Stateless Application Pattern

## Stateless Application

- requires no knowledge of previous interactions and stores no session information. Given the same input, an application can provide the same response to any user
- can scale horizontally because requests can be serviced by any of the available compute resources

# Amazon DynamoDB

- A fast and flexible NoSQL database service that applications use that require consistent, single-digit millisecond latency at any scale
- A `fully managed` NoSQL database supports both `document and key-value` store models
- Ideal for mobile, web, gaming, ad tech, and Internet of Things (IoT) applications
- Provides an effective solution for sharing session states across web servers, Amazon EC2 instances, or computing nodes.

## Using Amazon DynamoDB to Store State

- offers encryption at rest
- provides on-demand backup capability to create full backups of tables for long-term retention and archives for regulatory compliance
- automatically spreads data and traffic for tables over a sufficient number of servers to handle throughput and storage requirements
- use global tables to keep DynamoDB tables synchronized across AWS Regions
- use `Amazon DynamoDB Streams` to capture data modification events in DynamoDB tables.

## Primary Key, Partition Key, and Sort Key

- The primary key uniquely identifies each item in the table
- DynamoDB supports two different kinds of primary keys
  - Partition key
    - composed of only a partition key attribute
    - also known as its hash attribute.
  - Sort key
    - also known as its range attribute

### Best Practices for Designing and Using Partition Keys

- design your partition keys to spread I/O requests as evenly as possible across the table’s partitions to prevent “hot spots” that use provisioned I/O capacity inefficiently

### Designing Partition Keys to Distribute Even Workloads 

### Using Write Shards to Distribute Workloads Evenly

- A shard is a uniquely identified group of stream records within a stream

#### Random Suffixes in Shards

- To distribute loads more evenly across a partition key space, add a random number to the end of the partition key values and then randomize the writes across the larger space
- For example, if a partition key represents today’s date, choose a random number from 1 through 200, and add it as a suffix to the date

#### Calculated Suffixes in Shards

- use a number that you can calculate based on what you want to query.

## Items

- A group of attributes that is uniquely identifiable among all other entities in the table

## Attributes

- a fundamental data element, something that does not need to be broken down any further

## Data Types

### Scaler

- Represent exactly one value.
- The scalar types are:
  - Number
  - String
  - Binary
  - Boolean
  - Null

## Document

- There are two document types, list and map, which you can nest within each other to represent complex data structures up to 32 levels deep. There is no limit on the number of values in a list or a map, as long as the item containing the values fits within the DynamoDB item size limit of 400 KB.

### List

- A list type attribute can store an ordered collection of values.

### Map

- A map type attribute can store an unordered collection of name/value pairs
- Maps are enclosed in curly braces { … } and are similar to a JSON object

## Set

- DynamoDB supports types that represent sets of number, string, or binary values. There is no limit on the number of values in a set, as long as the item containing the value fits within the DynamoDB 400 KB item size limit.

## Amazon DynamoDB Tables

- DynamoDB global tables provide a fully managed solution for deploying a multi-region, multi-master database, without having to build and maintain your own replication solution

### Provisioned Throughput

- For any table or global secondary index, the minimum settings for provisioned throughput are one read capacity unit and one write capacity unit.
- You can apply all of the available throughput of an account to a single table or across multiple tables

### Throughput Capacity for Reads and Writes in Tables and Indexes

### Setting Initial Throughput Settings

#### Item sizes

#### Expected read and write request rates

#### Read consistency requirements

### Item Sizes and Capacity Unit Consumption

### Capacity Unit Consumption for Reads

#### GetItem

#### BatchGetItem

#### Query

#### Scan

#### Read operations and read consistency

#### Read consistency for Scan

### Capacity Unit Consumption for Writes

#### PutItem

#### UpdateItem

#### DeleteItem

#### BatchWriteItem

#### Total

#### Indexes

#### None

### Creating Tables to Store the State

### Control Plane

- Control plane operations let you create and manage DynamoDB tables and work with indexes, streams, and other objects that are dependent on tables.

- CreateTable Creates a new table. You can create one or more secondary indexes and enable DynamoDB Streams for the table.
- DescribeTable Returns information about a table, such as its primary key schema, throughput settings, and index information.
- ListTables Returns the names of all of the tables in a list.
- UpdateTable Modifies the settings of a table or its indexes, creates or remove new indexes on a table, or modifies settings for a table in DynamoDB Streams.
- DeleteTable Removes a table and its dependent objects from DynamoDB.

### Data Plane

- Data plane operations let you perform create/read/update/delete (CRUD) actions on data in a table. Some data plane operations also enable you to read data from a secondary index.

### Requesting Throttle and Burst Capacity

### Amazon DynamoDB Secondary Indexes: Global and Local

- A secondary index is a data structure that contains a subset of attributes from a table
- A table can have multiple secondary indexes,
- DynamoDB supports the following kinds of indexes:
  - Global secondary index A global secondary index is one with a partition key and sort key that can be different from those on the table.
  - Local secondary index A local secondary index is one that has the same partition key as the table but a different sort key.

# Amazon ElastiCache

- a web service that makes it easy to set up, manage, and scale distributed in-memory cache environments on the AWS Cloud

## Considerations for Choosing a Distributed Cache

- Determining the number of nodes necessary to manage the user sessions
  - In a distributed session cache, the sessions are divided by the number of nodes in the cache cluster
  - In the event of a failure, only the sessions that are stored on the failed node are affected.
- Whether the sessions must be replicated
  - ElastiCache for Memcached does not support replication
- Use Memcached if you require the following:
  - Use a simple data model
  - Run large nodes with multiple cores or threads
  - Scale out or scale in
  - Partition data across multiple shards
  - Cache objects, such as a database
- Use Redis if you require the following:
  - Work with complex data types
  - Sort or rank in-memory datasets
  - Persist the key store
  - Replicate data from the primary to one or more read replicas for read-intensive applications
  - Automate failover if the primary node fails
  - Publish and subscribe (pub/sub): the client is informed of events on the server
  - Back up and restore data
- Memcached vs Redis
  Capability                        |	Memcached   | Redis
  --                                | --          | --
  Simple cache to offload DB burden	| ✓           | ✓
  Ability to scale horizontally	    | ✓
  Multithreaded performance	        | ✓           |
  Advanced data types		            |             | ✓
  Sorting/ranking datasets          |             | ✓
  Pub/sub capability                |             | ✓
  Multi-AZ with auto-failover       |             | ✓
  Persistence                       |             | ✓

## ElastiCache Terminology

### Nodes

- smallest building block of an ElastiCache deployment
- fixed-size chunk of secure, network-attached RAM
- Each node type has a preconfigured amount of memory, with a small portion of that memory reserved for both the caching engine and operating system.

### Clusters

- Each ElastiCache deployment consists of one or more nodes in a cluster
- One Memcached cluster can be as large as 20 nodes.
- Redis clusters consist of a single node; however, you can group multiple clusters into a Redis replication group.

### Replication group

- a collection of Redis clusters with one primary read/write cluster and up to five secondary, read-only clusters called read replicas
- Read replicas enhance scalability and guard against data loss.

### Endpoint

- unique address your application uses to connect to an ElastiCache node or cluster
- A Memcached cluster has its own endpoint and a configuration endpoint.
- A standalone Redis cluster has an endpoint to connect to the cluster for both reads and writes.
- A Redis replication group has two types of endpoints.
  - The primary endpoint connects to the primary cluster in the replication group.
  - The read endpoint points to a specific cluster in the replication group.

## Cache Scenarios

### Time to live (TTL)

- An integer value that specifies the number of seconds until the key expires.

### Cache Hit

- Occurs when an application requests data from the cache, the `data is both present and not expired in the cache`

### Cache Miss

- Occurs if an application requests data from the cache, and it is `not present in the cache` (returning a null)

## Strategies for Caching

### Lazy Loading

- loads data into the cache only when necessary
![Lazy loading caching](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c14f014.jpg)

### Write-Through

- adds data or updates data in the cache whenever data is written to the database

## Scaling Your Environment

### Scale horizontally

- With Memcached, you can partition your data and scale horizontally to 20 nodes or more
- A Redis cluster consists of a single cache node that handles read and write transactions

### Scale vertically

- ElastiCache service does not directly support vertical scaling of your cluster

## Replication and Multi-AZ

### Multi-AZ Replication Groups

- you can provision a Multi-AZ replication group that allows your application to raise the availability and reduce the loss of data

## Backup and Recovery

- ElastiCache clusters that run Redis support snapshots.
- Snapshots are not available to clusters that use the Memcached caching engine

## Control Access

- The primary way to configure access to your ElastiCache cluster is by restricting connectivity to your cluster through a security group

# Amazon Simple Storage Service

- a stateless application that does not save client data that generates in one session for use in the next session with that client

## Amazon S3 Core Concepts

### Buckets

- a container for objects stored in Amazon S3

#### Creating a Bucket

- By default, you can create up to 100 buckets in each of your accounts.

### Objects

- Principal items stored in Amazon S3
- Consist of object data and metadata
- A key (name) and a version ID uniquely identify an object within a bucket

### Keys

- unique identifier for an object within a bucket

### Versioning

- a way to keep multiple variations of an object in the same bucket

## Accessing a Bucket

- AWS recommends that you create buckets with DNS-compliant bucket names.

## Bucket Restrictions and Limitations

- The account that created the bucket owns it
- By default, you can create up to 100 buckets in each of your accounts

### Rules for Naming Buckets

- you cannot change the bucket name

## Working with Amazon S3 Buckets

- An Amazon S3 bucket name is globally unique regardless of the AWS Region in which you create the bucket

## Deleting or Emptying a Bucket

## Deleting a Bucket Using Lifecycle Configuration

- You can configure lifecycle on your bucket to expire objects
- Amazon S3 then deletes expired objects

## Object Lifecycle Management

- To manage your objects so that they are stored cost-effectively throughout their life, configure their lifecycle policy. A lifecycle policy is a set of rules that designates actions that Amazon S3 applies to a group of objects. There are two types of actions:

### Transition actions

- Designate when objects transition from one storage class to another. For instance, you might decide to transition objects to the STANDARD_IA storage class 45 days after you created them, or archive objects to the GLACIER storage class six months after you created them.

### Expiration actions

- Designate when objects expire. Amazon S3 deletes expired objects on your behalf.

## When to Use Lifecycle Configuration

## Bucket Configuration Options

## Amazon S3 Consistency Model

- Amazon S3 provides read-after-write consistency for PUT requests of new objects in your S3 bucket in all regions
- Amazon S3 offers eventual consistency for overwriting PUT and DELETE requests in all regions.
- Amazon S3 does not currently support object locking

## Bucket Policies

- A centralized way to control access to buckets and objects based on numerous conditions, such as operations, requesters, resources, and aspects of the request. The policies are written using the IAM policy language and enable centralized management of permissions

## Amazon S3 Storage Classes

### Storage Classes for Frequently Accessed Objects

#### STANDARD

#### REDUCED_REDUNDANCY

### Storage Classes for Infrequently Accessed Objects

#### STANDARD_IA

- Use for your primary copy (or only copy) of data that cannot be regenerated.

#### ONEZONE_IA

- Use if you can regenerate the data if the Availability Zone fails.

### GLACIER Storage Class

## Amazon S3 Default Encryption for S3 Buckets

### Protecting Data Using Encryption

#### Use server-side encryption

- request Amazon S3 to encrypt your object before saving it on disks in its data centers and then decrypt the object when you download it.

##### Use server-side encryption with Amazon S3 Managed Keys (SSE-S3) 

##### Use server-side encryption with AWS KMS Managed Keys (SSE-KMS)

##### Use server-side encryption with customer-provided keys (SSE-C) 

#### Use client-side encryption

- You can encrypt data on the client side and upload the encrypted data to Amazon S3 and then manage the encryption process, the encryption keys, and related tools.

## Working with Amazon S3 Objects

### Key

- The key is the name that you assign to an object. The object key is used to retrieve the object.

### Version ID

- Within a bucket, a key and version ID uniquely identify an object. The version ID is a string that Amazon S3 generates when you add an object to a bucket.

### Value

- The information being stored. An object value can be any sequence of bytes. Objects can range in size from 0 to 5 terabytes (TB).

### Metadata

- A set of key-value pairs with which you can store information about the object. You can assign metadata, referred to as user-defined metadata, to your objects in Amazon S3. Amazon S3 also assigns system metadata to these objects, which it uses for managing objects.

### Subresources

- Amazon S3 uses the subresource mechanism to store object-specific additional information. Because subresources are subordinates to objects, they are always associated with an entity, such as an object or a bucket.

### Access control information

- You can control access to the objects that you store in Amazon S3. Amazon S3 supports both the resource-based access control, such as an access control list (ACL) and bucket policies, and user-based access control.

### Object Tagging

### Sharing an Object with Others

## Storing Large Attribute Values in Amazon S3

- Amazon DynamoDB currently limits the size of each item that you store in a table to 400 KB

# Amazon Elastic File System

- Provides simple, scalable file storage for use with Amazon EC2
- Storage capacity is elastic, growing and shrinking automatically as you add and remove files so your applications have the storage they need when they need it
- supports the Network File System versions 4.0 and 4.1 (NFSv4) protocol

## How Amazon EFS Works

![VPC accessing an Amazon EFS](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c14f019.jpg)

- You can mount an Amazon EFS file system in your VPC through the NFSv4 protocol
- You can mount an Amazon EFS file system on instances in only one VPC at a time
- Both the file system and VPC must be in the same AWS Region
- A mount target provides an IP address for an NFSv4 endpoint at which you can mount an Amazon EFS file system.
- Mount your file system using its DNS name, which resolves to the IP address of the Amazon EFS mount target in the same Availability Zone as your EC2 instance

### How Amazon EFS Works with AWS Direct Connect

- You can mount your Amazon EFS file systems on your on-premises data center servers when connected to your Amazon VPC with AWS Direct Connect (DX).

## Mount Target

- To access your file system, create mount targets in your Amazon VPC. Each mount target has the following properties:
  - Mount target ID
  - Subnet ID where it is created
  - File system ID for which it is created
  - IP address at which the file system may be mounted
  - Mount target state
  - You can use the IP address or the DNS name in your mount command.

## Tags

- To help organize your file systems, assign your own metadata to each of the file systems that you create. Each tag is a key-value pair.

## Authentication and Access Control

## Data Consistency in Amazon EFS

## Deleting an Amazon EFS File System

- Always unmount a file system before you delete it.

## Managing Access to Encrypted File Systems

## Amazon EFS Performance

## Performance Modes

### General Purpose performance mode

- For the majority of your Amazon EFS file systems
- ideal for latency-sensitive use cases, such as web serving environments, content management systems, home directories, and general file serving

### Max I/O performance mode 

- can scale to higher levels of aggregate throughput and operations per second with a trade-off of slightly higher latencies for file operations

## Throughput Scaling in Amazon EFS

- 