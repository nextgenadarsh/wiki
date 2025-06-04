AWS Glue
---

- a fully managed extract, transform, and load (`ETL`) service that `automatically discovers and profiles data, creates and updates metadata`, and `enables users to create and orchestrate ETL jobs` using the AWS Glue console.
- provides several useful features, such as `data classification, data discovery, and data lineage`, to help customers `understand, cleanse, and transform their data`. 
- can also be used to `move data between data stores, transform data, and process data for analysis`.
- often used with Amazon Redshift, Amazon S3, and Amazon EMR, as well as other AWS data storage and analytics services.

# AWS Glue Key Components

## ETL Jobs

- Python or Scala code that defines the ETL logic for extracting data from sources, transforming the data, and loading it into targets.

## ETL Libraries

- Customizable Apache Spark libraries for common ETL tasks such as reading and writing data, data type conversion, and data processing.

## Data Catalog

- A central repository for storing metadata about data sources and targets, as well as ETL jobs and development endpoints. The data catalog is used to access data sources and targets using AWS Glue ETL jobs and development endpoints.

## Development Endpoints

- Apache Spark environments used to develop, test, and run ETL jobs.

## Triggers

- Start ETL jobs on a schedule, in response to an event, or on-demand.

## Crawlers

- Discover data stored in data stores and populate the AWS Glue data catalog with metadata about the discovered data.

## AWS Glue Studio

- A visual interface for creating, debugging, and managing ETL jobs and development endpoints.

## Glue Schema Registry

- Validate and control streaming data using registered schemas for Apache Avro and JSON.

## Glue DataBrew

- Clean and normalize data without having to write code.

## Glue Elastic Views

- Use SQL queries to combine and replicate data to S3 buckets or Amazon Redshift.

# Process of using AWS Glue to create and execute ETL jobs:

- Define source and target data stores
- Connect to the data stores
- Discover data and schema
- Create an ETL job
- Define the ETL process
- Execute the ETL job
- Monitor and maintain the ETL process

