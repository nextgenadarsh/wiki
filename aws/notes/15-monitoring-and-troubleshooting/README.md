Monitoring and Troubleshooting
===

# Introduction to Monitoring and Troubleshooting

- Applications today are spread across multiple systems over large networks that make it difficult to track the health of systems and react to issues
- AWS Cloud provides fully managed services to help you implement monitoring solutions that are reliable, scalable, and secure. AWS offers services to help you monitor, log, and analyze your applications and infrastructure

## Monitoring Basics

### Choosing Metrics

- AWS takes the approach of “working backward” from the customer.

### Performance and Cost

- measure any metric that directly affects customers using your software or system
- measure the performance of your system to determine what is acceptable performance based on the usage at any point in time

### Trends

- Monitoring and measuring customer demand over time allows you to scale your infrastructure predictively to meet changes in customer demand without having to purchase more resources than are necessary.

### Troubleshooting and Remediation

- By gathering potentially relevant information ahead of time, it becomes easier to determine causes for failure

### Learning and Improvement

- By evaluating operational metrics over time, you can reveal patterns and common issues in your systems

# Amazon CloudWatch

- a monitoring and metrics service that provides you with a fully managed system to collect, store, and analyze your metrics and logs. By using CloudWatch, you can create notifications on changes in your environment.
- Typical use cases include the following:
  - Infrastructure monitoring and troubleshooting
  - Resource optimization
  - Application monitoring
  - Logging analytics
  - Error reporting and notification
- enables you to collect and store monitoring and operations data from logs, metrics, and events that run on AWS and on-premises resources

## How Amazon CloudWatch Works

![Amazon CloudWatch](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c15f002.jpg)

## Amazon CloudWatch Metrics

### Built-In Metrics

- A metric is a set of time-series data points that you publish to CloudWatch
- You can also define custom metrics based on data specific to your system.
- A metric is identified uniquely by a namespace, a name, and zero or more dimensions
  - Namespace
    - a collection of metrics or a container of related metrics
  - Name
    - A name for a given metric defines the attribute or property that you are monitoring
  - Dimension
    - a name/value pair used to define a metric uniquely
    - For example, for the namespace AWS/EC2 and name/metric CPUUtilization, the dimension might be InstanceId
- Data Points
  - When data is published to CloudWatch, it is pushed in sets of data points. Each data point contains information such as the timestamp, value, and unit of measurement.
- Timestamp
- Value
- Unit
- Statistics
  - aggregations of data points over specified periods of time for specified metrics
- Aggregations
  - CloudWatch aggregates metrics according to the period of time you specify when retrieving statistics.
- Available Metrics

### Custom Metrics

- CloudWatch also supports custom metrics that you can publish from your systems

#### High-Resolution Metrics

- Use `standard resolution` for data points that have a granularity of `one minute`
- Use `high resolution` for data points that have a granularity of `less than one second`

## Publishing Metrics

- You can publish them as single data points, statistics sets, or zero values

## Amazon CloudWatch Logs

- With CloudWatch Logs, you can set up a central log storage location to ingest and process logs at scale

### Log Aggregation

- install and configure the CloudWatch agent
- configure AWS Identity and Access Management (IAM) roles or users to grant permission for the agent to publish logs into CloudWatch
- CloudWatch organizes your logs into three conceptual levels: groups, streams, and events
  - Log Groups
    - collection of log streams
  - Log Streams
    - A sequence of log events such as a single log file from one of your instances
  - Log Events
    - a record of some activity from an application, process, or service. This is analogous to a single line in a log file

### Log Searches

- you can search for logs through a central location using metric filters.

### Metric Filters

- a text pattern used to parse log data for specific events

### Log Processing

- CloudWatch can process logs that you already generate and provide valuable metrics

## Amazon CloudWatch Alarms

- you can set alarms to monitor your metrics and trigger actions in response to changes in state
- CloudWatch alarms have three possible states: OK, ALARM, and INSUFFICIENT_DATA

### Using Amazon CloudWatch Alarms

- When you create an alarm, specify three settings that determine when the alarm should change states: the threshold, period, and data points on which you want to notify


## Amazon CloudWatch Dashboards

- customizable pages in the CloudWatch console that you can use to monitor resources in a single view

# AWS CloudTrail

- a fully managed service that continuously monitors and records API calls and stores them in Amazon S3
- IT auditors can also use log files as compliance aids.
- CloudTrail helps answer the following five key questions about monitoring access:
  - Who made the API call?
  - When was the API call made?
  - What was the API call?
  - Which resources were acted upon in the API call?
  - Where was the origin of the API call?

## AWS CloudTrail Events

- any single API activity in an AWS account
- CloudTrail tracks two types of events: management events and data events

### Management Events

- give insight into operations performed on AWS resources

### Data Events

- give insight into operations that store data in (or extract data from) AWS resources

### Global Service Events

- Global services are logged as occurring in US East (N. Virginia) Region

## Trails

- If you need long-term storage of events (for example, for compliance purposes), you can configure a trail of events as log files in CloudTrail
- A trail is a configuration that enables delivery of CloudTrail events to an Amazon S3 bucket, Amazon CloudWatch Logs, and Amazon CloudWatch Events

# AWS X-Ray

- a service that collects data about requests served by your application.
- provides tools you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization.
- helps developers build, monitor, and improve applications

## AWS X-Ray Use Cases

- Identifying performance bottlenecks
- Pinpointing specific service issues
- Identifying errors
- Identifying impact to users

## Tracking Application Requests

![Microservice example](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c15f005.jpg)

- X-Ray can track a user request using a trace, segment, and subsegment.
  - Trace
    - End to end path of request from the client—from its entry into your environment to the backend and back to the user
    - A trace ID is passed through the AWS services
  - Segment
    - data from a particular service
    - analogous to links in a chain whereby the chain is the request generated by the user
  - Subsegment
    - identifies the underlying API calls made from a particular service
    - Subsegments are collated into segments
- A `service graph` is a visual representation of the services and resources that make up your application
- provides a convenient way for you to view system performance and to identify problems or bottlenecks in your applications
