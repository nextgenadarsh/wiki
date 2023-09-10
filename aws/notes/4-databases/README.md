Databases
============

# AWS Database Service Mapping to Database Type

Product     | Type        | Description
--          | --          | --
Aurora      | Relational  | MySQL, PostgreSQL
RDS         | Relational  | Managed MySQL, PostgreSQL, Oracle, SQL Server, MariaDB
DynamoDB    | NoSQL       | serverless, managed NoSQL, 1-digit ms latency at any scale
Redshift    | Warehouse   | Managed PetaByte, SQL query for data analysis
ElastiCache | In-memory   | Memcached, Redis
Neptune     | Graph DB    | Fully managed
Document DB (MongoDB) | Non-Relational | Fully managed DocumentDB with MongoDB workloads
TimeStream  | Time series DB | Fully managed TimeSeries DB for IoT and operational apps
Quantum Ledger (QL) DB | Ledger database | Fully managed Ledger DB
Database Migration Service (DMS)| Database Migration | Help migrate your databases to AWS

# Relational Databases

- A collection of data items with predefined relationships between them. 

## Characteristics of Relational Databases

### Structured Query Language (SQL)

- Primary interface that you use to communicate with relational databases
- ANSI SQL is supported by all popular relational database engines

### Data Integrity

- Overall completeness, accuracy, and consistency of data
- Set of constraints (Primary/Foreign keys, NotNull, Unique, Default, Check) to enforce data integrity

### Transactions

- One or more SQL statements that execute as a sequence of operations to form a single logical unit of work
- A transaction results in a COMMIT or a ROLLBACK

### ACID Compliance

#### Atomic

- Requires that the transaction as a whole executes successfully, or if a part of the transaction fails, then the entire transaction is invalid.

#### Consistent

- Data written to the database as part of the transaction must adhere to all defined rules and restrictions, including constraints, cascades, and triggers.

#### Isolated

- Makes sure that each transaction is independent unto itself.

#### Durable compliance

- All of the changes made to the database be permanent when a transaction is successfully completed.

## Managed vs. Un-managed Databases

### Managed Databases

- Enable you to offload the administrative burdens
- AWS is responsible for:
  - Hardware provisioning
  - Setup and configuration
  - Throughput capacity planning
  - Replication
  - Software patching
  - Cluster scaling

### Un-managed Databases

- Gives you more flexibility on the types of databases that you can deploy and configure
- You are responsible for the administration of the un-managed databases

## Amazon Relational Database Service (RDS)

- Automatically `patches` the database software and `backs up` your database

### Procurement, configuration, and backup tasks

- You can scale CPU, Memory, Storage, IOPS independently as you need
- RDS manages backups, software patches, automatic failure detection, and recovery.
- You can configure automated backups or manually create your own backup snapshot

### Security and availability

- Can enable the encryption
- Synchronous secondary instance that you can fail over
- Protect your databases by storing them in a virtual private cloud (VPC).
- RDS does not provide shell access to DB instances

### Features

#### Automatic software patching

- You can define a `maintenance window`
- You can enable auto minor version upgrade

#### Easy vertical scaling

- It gives you flexibility over the performance and cost of your Amazon RDS database
- In Multi-AZ configuration, the standby database is upgraded first and then a failover occurs to the newly configured database

#### Easy storage scaling

- General Purpose SSD (gp2)
  - Cost-effective storage 
  - Ideal for a broad range of workloads
  - Ability to burst to 3,000 IOPS for extended periods of time
- Provisioned IOPS (io1)
  - Ideal for input/output-intensive workloads 
  - Low I/O latency and low I/O throughput
- Magnetic Storage
  - Designed for backward compatibility
  - Not recommended by AWS for usage

#### Read Replicas (Horizontal Scaling)

- Replication from the master database to the read replica is asynchronous
- RDS MySQL, PostgreSQL, and MariaDB support up to 5 and Aurora 15 read replicas

#### Backing Up Data with Amazon RDS

#### Automatic backups (Point-in-time)

- RDS performs a full daily snapshot of your data that is taken during your preferred backup window
- Default retention period is 7 days, but it can be a maximum of up to 35 days.
- To perform a restore, you must choose the Latest Restorable Time, which is typically within the last 5 minutes.
- Backups are kept until the source database is deleted

#### Database Snapshots (Manual)

- Backups are kept until you explicitly delete them
- Take backup from standby database of Multi-AZ deployment to avoid latency during backup

#### Multi-AZ deployments

- You have a primary and a standby DB instance
- RDS automatically fails over to the standby in case of any failure or scheduled maintenance

#### Encryption

- RDS uses KMS for `encryption at rest`
- Encryption can only be enabled/disabled when creating
- RDS supports using the Transparent Data Encryption (TDE) for Oracle and SQL Server
- For `encryption in transit`, RDS generates an SSL certificate for each database instance that can be used to connect

#### IAM DB Authentication

- You can manage access to your database centrally instead of storing the user credentials in each database
- Supported only for MySQL and PostgreSQL
- You can enable this feature during the maintenance window due to downtime

#### Monitoring with Amazon CloudWatch

- Use Amazon CloudWatch to monitor your database tier and raise alarms for any failure
- CloudWatch provides some built-in metrics for Amazon RDS with a granularity of 5 mins
- Use enable enhanced monitoring for 1 min granularity
- Amazon RDS integrates with CloudWatch to send it the following database logs:
  - Audit log
  - Error log
  - General log
  - Slow query log

### Amazon Aurora

- A `MySQL` and `PostgreSQL`-compatible relational database engine
- Drop-in replacement for MySQL and PostgreSQL relational databases
- Time-consuming administration tasks, such as hardware provisioning, database setup, patching, and backups, are automated
- Aurora features a distributed, fault-tolerant, self-healing storage system that automatically scales up to 64 TiB per database instance compared to 32 TiB for other RDS services.
- Up to `15 low-latency read replicas`, point-in-time recovery, continuous backup to Amazon Simple Storage Service (Amazon S3), and replication across 3 AZ

#### Amazon Aurora DB Clusters

![Amazon Aurora DB cluster](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f008.jpg)
- A DB cluster `consists of one or more DB instances and a cluster volume` that manages the data for those instances.
- An Aurora cluster volume is `a virtual database storage volume` that `spans multiple AZ`, and each Availability Zone has a copy of the DB cluster data.
- An Aurora DB cluster has two types of DB instances:
  - Primary Instance
    - Supports read and write operations and `performs all of the data modifications` to the cluster volume. Each Aurora DB cluster has one primary instance.
  - Amazon Aurora Replica
    - Supports `read-only operations`.
    - Each Aurora DB cluster can have `up to 15 Replicas` in addition to the primary instance.
    - Multiple Aurora Replicas distribute the read workload, and if you locate Aurora Replicas in separate Availability Zones, you can also increase database availability.
- It has separate storage layer, called the `cluster volume`, which is `spread across multiple AZ` increasing durability
- It has one primary instance that writes across the cluster volume

### Amazon Aurora Global Databases

- You can also create a `multi-regional deployment` for your database tier
- Application must write to the primary AWS Region
- Secondary AWS Region is used for reading data only
- Available only for MySQL 5.6

### Amazon Aurora Serverless

- An on-demand, automatic scaling configuration for Aurora
- Available only for MySQL
- Database will automatically start up, shut down, and scale capacity up or down

### Best Practices for Running Databases on AWS

- Follow Amazon RDS basic operational guidelines
- Allocate sufficient RAM to the DB instance
- Implement Amazon RDS security
- Use enhanced monitoring to identify OS issues
- Use metrics to identify performance issues
- Tune queries
- Use DB parameter groups
- Use read replicas

# Nonrelational Databases

- Commonly used for `internet-scale applications` that do not require any complex queries

## NoSQL Database

- `Nonrelational` databases optimized for `scalable performance` and `schema-less` data models.
- Recognized for their ease of development, low latency, and resilience.
- Optimized for applications that require large data volume, low latency, and flexible data models

### When to Use a NoSQL Database

- Big data, mobile, and web applications that require greater scale and higher responsiveness

### Comparison of SQL and NoSQL Databases

Type            | SQL               | NoSQL
--              | --                | --
Data Storage    | Rows and columns  | Key-value, document, wide-column, graph
Schemas         | Fixed             | Dynamic
Querying        | Using SQL         | Focused on collection of documents
Scalability     | Vertical          | Horizontal
Transactions    | Supported         | Support varies
Consistency     | Strong            | Eventual and strong

### NoSQL Database Types

- Columnar
  - Optimized for reading and writing columns of data as opposed to rows of data
- Document
  - Designed to store semi-structured data as documents, typically in JSON or XML format
  - Schema for each NoSQL document can vary
- Graph
  - Store vertices and directed links called edges
  - Can be built on both SQL and NoSQL databases
- In-memory key-value
  - NoSQL databases optimized for read-heavy application or compute-intensive workloads

## Amazon DynamoDB

- Fully managed cloud DB 
- Supports both document and key-value store models
- Great fit for:
  - Mobile
  - Gaming
  - AdTech
  - Internet of Things (IoT)
  - Applications that do not require complex queries
- `Scale up or scale down` your table throughput capacity `without downtime`
- Automatically replicated across `multiple AZ`
- Use `global tables` to keep DynamoDB tables in sync across AWS Regions.

### Core Components of Amazon DynamoDB

- Tables, items, and attributes are the core components
- A table is a collection of items, and each item is a collection of attributes.
- Uses `partition keys` to identify uniquely each item in a table
- `Secondary indexes` can be used to provide more querying flexibility
- Use DynamoDB Streams to capture data modification events in DynamoDB tables
![Amazon DynamoDB tables and partitions](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f010.jpg)
- DynamoDB supports `nested attributes` up to `32 levels` deep

#### Primary Key

- Uniquely identifies each item in the table
- Required to specify the table name and primary key


#### Partition key (hash key/attribute)

- Composed of one attribute

#### Partition key and sort key (range attribute)

- aka composite primary key; composed of partition key and the sort key
- DynamoDB stores items with the same partition key physically close together, in sorted order, by the sort key value.
- Possible for two items to have either partition key or sort key as different value for uniqueness
- Composite primary key gives you additional flexibility when querying data
- All your data for partition key is stored in same physical location

#### Secondary Indexes

- Used to perform queries on attributes that are not part of the table’s primary key
- Contains primary key, alternate key attributes and optionally subset of base table attributes

##### Local Secondary Index

- An index that has the same partition key as the base table, but a different sort key
- Every partition of a local secondary index is scoped to a base table partition that has the same partition key value
![Local secondary index](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f013.jpg)

##### Global Secondary Index

- An index with a partition key and a sort key that can be different from those on the base table
- `Queries` on the index can span all of the data in the base table `across all partitions`
![Global secondary index](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f014.jpg)
- You can create a global secondary index, `not a local secondary index`, `after table creation`

#### Comparison of Local Secondary Indexes and Global Secondary Indexes

Characteristic	| Global Secondary Index  | Local Secondary Index
--              | --                      | --
Query Scope	    | Entire table, across all partitions. | Single partition, as specified by the partition key value in the query.
Key Attributes	| Partition key, or partition and sort key. Can be any scalar attribute in the table. | Partition and sort key. Partition key of index must be the same attribute as base table.
Projected Attributes | Only projected attributes can be queried. | Can query attributes that are not projected. Attributes are retrieved from the base table.
Read Consistency | Eventual consistency only | Eventual consistency or strong consistency.
Provisioned Throughput | Separate throughput settings from base table. Consumes separate capacity units. | Same throughput settings as base table. Consumes base table capacity units.
Lifecycle Considerations | Can be created or deleted at any time.	| Must be created when the table is created. Can be deleted only when the table is deleted.

### Amazon DynamoDB Streams

- Captures data modification events in DynamoDB tables
- Stream records have a `lifetime` of `24 hours`; after that, they are automatically removed from the stream.
![Example of Amazon DynamoDB Streams and AWS Lambda](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f016.jpg)
- DynamoDB Streams enables other powerful solutions like:
  - `Data replication` within and `across AWS regions`
  - `Materialized views` of data in DynamoDB tables
  - `Data analysis` by using Amazon Kinesis materialized views

### Read Consistency

- DynamoDB replicates data among multiple AZ
- DynamoDB supports both `eventually consistent` and `strongly consistent reads`
- 1 RCU ~ 1 strongly consistent read per second ~ 2 eventually consistent reads per second for an item up to `4 KB`
- 1 WCU ~ 1 write per second for an item up to `1 KB` in size
- When a request is throttled, it fails with an HTTP 400 code with `ProvisionedThroughputExceededException`

### Mechanism for managing throughput

- Amazon DynamoDB Auto Scaling
- Provisioned throughput
- Reserved capacity
- On demand

### Partitions and Data Distribution

- When you allocate RCUs and WCUs to a table, those RCUs and WCUs are split evenly among all partitions for your table.
- Burst Capacity
  - Whenever your partition is not using all of its total capacity, DynamoDB reserves a portion of that unused capacity for later bursts of throughput to handle any spike your partition may experience
- Adaptive Capacity
  - Enables your application to continue reading and writing to hot partitions without being throttled, provided that the total provisioned capacity for the table is not exceeded
  - When it is not always possible to distribute read and write activity to a partition evenly

### Retrieving Data from DynamoDB

- Query
  - You need to specify Primary key for querying table; TableName and IndexName for querying index
- Scan
  - Returns one or more items and item attributes by accessing every item in a table or a secondary index
  - If the total number of scanned items exceeds the maximum dataset `size limit of 1 MB`, the scan stops
  - Uses eventually consistent reads by default

### Global Tables

- Fully managed, multi-region, and multi-master database that provides fast, local, read-and-write performance for massively scaled, global applications
![Global Tables](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f017.jpg)
- A collection of one or more DynamoDB tables, all owned by a single AWS account, identified as replica tables
- A `replica table` (or replica, for short) is a single DynamoDB table that functions as a part of a global table.
- Only one replica table per region, and every replica has the same table name and the same primary key schema
- DynamoDB does not support strongly consistent reads across AWS Regions.

### IAM and Fine-Grained Access Control

- You can use AWS IAM to grant or restrict access to DynamoDB resources and API actions.

### Backup and Restore

- `On-demand backups` create full backups of your tables or restore them on-demand at any time.
- `Point-in-time recovery` helps protect your DynamoDB tables from accidental write or delete operations.

### Encryption with Amazon DynamoDB

### Amazon DynamoDB Best Practices

- Distribute Workload Evenly

### Comparison of Query and Scan Operations

The `Query` operation finds items in a table based on `primary key values`. You can provide a `sort key attribute` name and value `to refine the search results`. By default, Query `returns all of the data attributes` for those items with specified primary keys. The results are `sorted by the sort key` in ascending order, which can be reversed. Additionally, queries are set to be Eventually Consistent, with an option to change to Strongly Consistent, if necessary.

The `Scan` operation `returns all of the item attributes` by accessing every item in the table. It is for this reason that Query is more efficient than the Scan operation.

# Data Warehouse

- a central repository of information that you can analyze to make better-informed decisions.

## Data Warehouse Architecture

- consists of three tiers:
  - top-tier: front-end client
  - middle tier: analytics engine
  - bottom tier: database server

## Data Warehouse Benefits

- Better decision-making
- Consolidation of data from many sources
- Data quality, consistency, and accuracy
- Historical intelligence
- Analytics processing that is separate from transactional databases, improving the performance of both systems

## Comparison of Data Warehouses and Databases

Characteristics     | Data Warehouse	          | Transactional Database
--                  | --                        | --
Suitable Workloads	| Analytics, reporting, big data | Transaction processing
Data Source	        | Data collected and normalized from many sources | Data captured as-is from a single source, such as a transactional system
Data Capture	      | Bulk write operations typically on a predetermined batch schedule | Optimized for continuous write operations as new data is available to maximize transaction throughput
Data Normalization  | De-normalized schemas, such as the star schema or snowflake schema | Highly normalized, static schemas
Data Storage        | Optimized for simplicity of access and high-speed query performance by using columnar storage	| Optimized for high-throughout write operations to a single row-oriented physical block
Data Access	        | Optimized to minimize I/O and maximize data throughput | High volumes of small read operations

## Comparison of Data Warehouses and Data Lakes

- `Data lake` is a centralized repository for all data, including `structured and unstructured`
- A `data warehouse` uses a `predefined schema` that is optimized for `analytics`

Characteristics	        | Data Warehouse            | Data Lake
--                      | --                        | --
Data	                  | Relational data from transactional systems, operational databases, and line-of-business applications | Nonrelational and relational data from IoT devices, websites, mobile apps, social media, and corporate applications
Schema                  | Designed before the data warehouse implementation (schema-on-write)	| Written at the time of analysis (schema-on-read)
Price/Performance | Fastest query results by using higher-cost storage | Query results getting faster by using low-cost storage
Data Quality  | Highly curated data that serves as the central version of the truth | Any data that may or may not be curated (in other words, raw data)
Users   | Business analysts, data scientists, and data developers	| Data scientists, data developers, and business analysts (using curated data)
Analytics	    | Batch reporting, BI, and visualizations	| Machine learning, predictive analytics, data discovery, and profiling

## Comparison of Data Warehouses and Data Marts

- A `data mart` is `a data warehouse` that serves the needs of a specific team or business unit, such as finance, marketing, or sales. It is `smaller, is more focused`, and may contain summaries of data that best serve its community of users.

Characteristics	    | Data Warehouse      | Transactional Database
--                  | --                  | --
Scope	              | Centralized, multiple subject areas integrated together | Decentralized, specific subject area
Users	              | Organization-wide   |	A single community or department
Data Source	        | Many sources	      | A single or a few sources, or a portion of data already collected in a data warehouse
Size	              | Large—can be 100s of gigabytes to petabytes	| Small, generally up to 10s of gigabytes
Design	            | Top-down	          | Bottom-up
Data Detail	        | Complete, detailed data	| May hold summarized data

## Amazon Redshift

- A fast, fully managed, `petabyte-scale`, `data warehouse`
- Makes it simple and cost-effective to analyze all your data by using standard SQL and your existing BI tools

### Architecture

![Amazon Redshift architecture](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f020.jpg)
- Redshift data warehouse is a `collection of` computing resources called `nodes`, which are organized into a group called a `cluster`.
- Each cluster `runs an Amazon Redshift engine` and contains `one or more databases`.
- After you provision your cluster, you can upload your dataset and then perform data analysis queries.
- Each `cluster has a leader node` and one or more compute nodes, and you have a choice of a hardware platform for your cluster.

### Client Applications

- Amazon Redshift `integrates with various data loading and extract, transform, and load (ETL) tools` and BI reporting, data mining, and analytics tools.
- It is based on `open standard PostgreSQL`, so most existing SQL client applications will integrate with Amazon Redshift with only minimal changes.

### Leader Node

- acts as the SQL endpoint and receives queries from client applications, parses the queries, and develops query execution plans
- stores metadata about the cluster

### Compute Nodes

- execute the query execution plan and transmit data among themselves to serve these queries and sends result to leader node for aggregation

### Node Slices

- A compute `node is partitioned into slices`.
- Each slice is allocated a portion of the node’s memory and disk space, where it processes a portion of the workload assigned to the node.

### Databases

- A cluster contains one or more databases. User data is stored on the compute nodes.

### Hardware Platform Options

- dense storage (DS) node types are storage-optimized
- dense compute (DC) node types are compute-optimized

### Distribution Strategy

- EVEN distribution
  - Rows are distributed across the slices in a round-robin fashion, regardless of the values in any particular column
- KEY distribution
  - Rows are distributed according to the values in one column
- ALL distribution
  - A copy of the entire table is distributed to every node

### Sort Keys

- Amazon Redshift stores your data on disk in sorted order according to the sort key, and the query optimizer uses sort order when it determines the optimal query plans

### Snapshots

- Amazon Redshift supports snapshots, similar to Amazon RDS

# In-Memory Data Stores

- used for caching and real-time workloads.

## Caching Strategies

- A `cache hit` occurs when the cache contains the information requested.
- A `cache miss` occurs when the cache does not contain the information requested.

### Lazy loading

- a caching strategy that loads data into the cache only when necessary.

### Write through

- Adds data or updates in the cache whenever data is written to the database
- if your data is updated frequently, the cache may be updating often, causing `cache churn`

## In-Memory Key-Value Store

- a NoSQL database optimized for read-heavy application workloads or compute-intensive workloads

### Benefits of In-Memory Data Stores

### Benefits of Distributed Cache

## Amazon ElastiCache

- A web service that makes it easy to deploy, operate, and scale an in-memory cache in the AWS Cloud
- Automatically detects and replaces failed nodes
- Supports engines: Redis and Memcached

 ### Redis

- Key-value store that supports more advanced data structures, such as sorted sets, hashes, and lists
- Has disk persistence built in, meaning that you can use it for long-lived data
- Supports replication to achieve Multi-AZ redundancy
- Use Redis if you require one or more of the following:
  - More advanced data types, such as lists, hashes, and sets.
  - Sorting and ranking datasets in memory help you, such as with leader-boards.
  - Your application requires publish and subscribe (pub/sub) capabilities.
  - Persistence of your key store is important.
  - You want to run in multiple Availability Zones (Multi-AZ) with failover.
  - You want transactional support, which lets you execute a group of commands as an isolated and atomic operation.
 
 ### Memcached

- In-memory key store
- ElastiCache is protocol-compliant with Memcached
- It is also multithreaded, meaning that it makes good use of larger Amazon EC2 instance sizes with multiple cores.
- Use Memcached if you require one or more of the following:
  - Object caching is your primary goal, for example, to offload your database.
  - Simple a caching model as possible.
  - To run large cache nodes and require multithreaded performance with the use of multiple cores.
  - You want to scale your cache horizontally as you grow.

### Comparison of Memcached and Redis

## Amazon DynamoDB Accelerator

- A fully managed, highly available, `in-memory cache for DynamoDB` that `delivers up to 10 times` the performance improvement—from milliseconds to microseconds—even at millions of requests per second
- You `pay only for` the capacity you `provision`

# Graph Databases

- A graph is a data structure that consists of `vertices` and `directed links` called `edges`. Vertices and edges can each have properties associated with them.
- A graph database is `optimized to store and process graph data`.

## Amazon Neptune

- `Fully managed` graph database service that makes it easy to build and run applications that work with highly connected datasets.
- The core of Neptune is a purpose-built, high-performance graph database engine `optimized for storing billions of relationships` and querying the graph with milliseconds latency.
- Features:
  - Read replicas
  - Point-in-time recovery
  - Continuous backup to Amazon S3
  - Replication across Availability Zones
  - Encryption at rest and in transit
- Use cases:
  - Recommendation engines
  - Fraud detection
  - Knowledge graphs
  - Drug discovery
  - Network security

# Cloud Database Migration

## AWS Database Migration Service (DMS)

- Helps you migrate databases to AWS quickly and securely
- Supports both `homogenous database migrations` and `heterogeneous migrations`
- You can also stream data to Amazon Redshift, Amazon DynamoDB, and Amazon S3
![Homogenous database migrations using AWS DMS](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c04f023.jpg)

## AWS Schema Conversion Tool

- For `heterogeneous database migrations`, AWS DMS uses the AWS Schema Conversion Tool (AWS SCT).
- AWS SCT makes heterogeneous database migrations predictable by automatically converting the source database schema and a majority of the database code objects, including views, stored procedures, and functions, to a format compatible with the target database.
- Any objects that cannot be automatically converted are clearly marked so that they can be manually converted to complete the migration.
- AWS SCT can also scan your application source code for embedded SQL statements and convert them as part of a database schema conversion project. During this process, AWS SCT performs cloud-native code optimization by converting legacy Oracle and SQL Server functions to their equivalent AWS service, thus helping you modernize the applications at the same time as database migration

