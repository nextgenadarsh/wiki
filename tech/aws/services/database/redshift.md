Amazon Redshift
---

- is a `SQL-based data warehouse` service that allows you to analyze your data by using `standard SQL` and business intelligence `(BI) tools` and standard Microsoft Open Database Connectivity (`ODBC`) and Java Database Connectivity (JDBC) connections.
- is designed as an `online analytical processing (OLAP)` database service that `allows you to run complex analytical queries against petabytes of data`.
- An organization might use Redshift when you need to pull data sets together from many `different sources`, such as inventory, financial, and retail systems.
- In comparison, Amazon EMR is designed for the processing of extremely large data sets, such as for machine learning or streaming data, using data processing frameworks such as Spark or Hadoop.
-  uses `columnar data storage`, where data records are stored sequentially in columns instead of rows; this makes it ideal for data warehousing storage and analytics.
- This format of data storage allows a very high level of `parallel processing across all data stores`, resulting in enhanced query performance.
- `Less storage space is required` due to the high level of `compression` of the data stores.
- Data storage and queries are distributed across all nodes, which are high-performance local disks attached to the supported EC2 instance nodes.
- Each Redshift `node` is a `minimum of 128 TB` of managed storage across a two-node cluster.
- Depending on the instance size chosen, clusters range from 160 GB up to 5 PB.
- Choices for instances include the following options:
  - RA3 nodes
    - Data is stored in a separate storage layer that can be scaled independently of compute. The data warehouse is sized based on the query performance required.
  - Dense Compute (DC)
    - High-performance requirements for less than 500 GB of data can utilize fast CPUs, large amounts of RAM, and SSD drives.
  - Dense Storage (DS2)
    - Create large data warehouses with a lower price point using HDDs with three-year-term reserved instances (RIs).
- The `multimode` design of a Redshift cluster includes both leader and compute nodes:
  - Leader nodes
    - These nodes `manage client connections` and receive and coordinate the execution of queries.
    - However, the queries themselves are performed by the compute nodes.
  - Compute nodes
    - These nodes `store all data records and perform all queries under the direction of the leader nodes`.
    - All compute work is performed in `parallel, including queries, data ingestion, backups, and restores`.
- The size of a cluster can be automated using a feature called `Concurrency Scaling`, where Redshift adds additional cluster capacity as required to support an unlimited number of concurrent users and queries.
- supports `identity federation and SAML single sign-on`, multifactor authentication, and additional security by hosting the Redshift cluster in an AWS VPC.
- `Data encryption` is supported using AWS Key Management Service (`KMS`).
- To ensure data `availability`, Redshift replicates your data within your defined data warehouse cluster and continually `backs up` your data to Amazon `S3 using snapshots`.
- Redshift maintains three copies of your data:
  - The original copy of data
  - A replica copy that is stored on compute nodes in the cluster
  - A backup copy that is stored in Amazon S3 and can be retained for 1 to 35 days
- Redshift also supports `SSL/TLS encryption in transit` from the client application to the Redshift warehouse cluster.

<h2 style="background-color:lightgreen"># Amazon Redshift Cheat Sheet</h2>

- Redshift ML can use SQL statements to train Amazon SageMaker models on data stored in Redshift.
- Advanced Query Accelerator (AQUA) allows Redshift to run up to ten times faster.
- RedShift Spectrum can be used to run queries against petabytes of stored Redshift data in S3.
- Redshift supports end-to-end encryption.
- Redshift can be hosted inside a VPC to isolate your data warehouse cluster in your own virtual network.
- Redshift can be integrated with AWS Lake Formation, which allows you to set up a secure data lake to store your data both in its original form and prepared for analysis.
