Amazon CloudWatch
---

- is a monitoring service provided by AWS that enables you to `monitor and manage various resources` and more than 70 cloud services in the AWS cloud.
- You can `monitor metrics, set alarms, and automatically react` to changes in your resources.
- `provides data and operational insights` for various AWS resources, such as Amazon EC2 instances and Amazon RDS instances.
- `collect and track metrics` which are variables you can measure for your resources and applications.
- `set metric alarms`, which enable you to receive notifications or automatically make changes to the resources you are monitoring when a threshold is breached.

# CloudWatch Features

## Auto Scaling and CloudWatch metrics and alarms

- You can `automatically adjust your application’s compute power` as needed with EC2 Auto Scaling and EC2 metrics linked to Amazon CloudWatch alarms.

## Log filtering with metric filters and alerts

- You can `arrange to be notified` when specific data patterns occur in your logs and act accordingly using Amazon CloudWatch alarms and Amazon SNS notifications that `call AWS Lambda to run custom functions providing automated solutions`.

## Billing Alerts

- You can `monitor and control AWS cloud costs` by using `Billing Alerts` and `SNS notifications`.

## Logging of CloudTrail API calls to CloudWatch logs

- Log all the API calls made to your AWS resources and send the logs to CloudWatch Logs `for storage and monitoring`.
- This can be useful for a variety of purposes, such as `auditing and compliance, debugging, and security analysis`.

# CloudWatch Basic Monitoring

- is `free of charge and, depending on the AWS service`, a select number of basic metrics are available for monitoring the operation of the service.
- Metrics, once enabled, report to Amazon CloudWatch on a set schedule.
- For EC2 instances and containers (ECS), metric data is sent to CloudWatch `every 5 minutes`.
- For RDS and ELB (ELB), a selection of metric data is sent to CloudWatch every `60 seconds`.
- EC2 instances can also enable `detailed monitoring`, which `increases the reporting period to every 60 seconds`; however, `detailed monitoring is not free`.
- Make sure to check what basic metrics are available for each service in the AWS documentation; new metrics are being added to CloudWatch all the time to further enhance its monitoring ability.
- With every AWS service, there are additional metrics you can choose to enable to assist in monitoring.

![CloudWatch Metrics](../../images/cloud-watch-metrics.png)
> Fig: CloudWatch Metrics

# CloudWatch Logs

- Amazon CloudWatch allows you to send your event data from AWS CloudTrail custom trails to CloudWatch `log groups`.
- Stored CloudWatch log data can be reviewed by creating a `metric filter` that looks for `specific events or patterns`.
- Network traffic across a VPC, subnet, or elastic network adapter can be captured and stored in a CloudWatch log group for analysis.
- Collected data stored in a CloudWatch log can also be analyzed by one of the following options:
  - Export Data to Amazon S3
    -Log information for a defined date range can be exported to an S3 bucket for `analysis by any third-party monitoring application`.
  - Create an AWS Lambda subscription filter
    - When a log event matches a specific filter, AWS Lambda functions can `execute a custom task based on the event type generated`.
- `Retention time` for CloudWatch logs is `forever`; however, you can choose a retention time frame of `up to 10 years`.
- Retention of records stored in S3 buckets can be managed with lifecycle rules.

# Collecting Data with the CloudWatch Agent

- Amazon CloudWatch receives and stores metrics or log data from the `CloudWatch agent installed on each EC2 instance` or, optionally, on servers located on premises.
- `AMIs have the CloudWatch agent installed by default`.

# Amazon CloudWatch Integration

## Amazon SNS

- SNS is used to `send alerts when CloudWatch metric alarms are triggered`.

## ELB (ELB)

- Load-balancing metrics available include active connection count, request count, healthy host count, Transport Layer Security (TLS) connection errors, HTTP responses, and errors.

## Amazon S3

- Storage metrics detail the number of objects and bucket size; request metrics include all requests, GET requests, bytes uploaded and downloaded, and 4xx and 5xx errors.

## Amazon EC2

- Once an instance has been launched, from the Monitoring tab, 14 metrics are displayed, including options for CPU utilization, disk read and write operations, network traffic and packet flow, and status checks.

## EC2 Auto Scaling

- Launch or terminate instances using CloudWatch metrics and alarms that trigger EC2 Auto Scale Groups.

## AWS CloudTrail

-  After a custom trail has been created, CloudWatch can be configured to write all API calls and authentications in your AWS account to a CloudWatch log file.

## AWS Config

- Rules that discover resources that are out of compliance can invoke a custom AWS Lambda function to perform remediation.

## Amazon RDS

- Metrics include database connections, disk queue length, free storage space, read and write throughput, SSD burst balance, and CPU credit usage.

## AWS IAM

- All authentication attempts, both successful and unsuccessful, can be monitored with Amazon CloudWatch.
- SNS notifications can notify humans and automated subscribers.

# Amazon CloudWatch Terminology

## Namespace

- Each `AWS service` stores its CloudWatch metrics and associated data in its `own container`.

## Metrics

- Each metric is a `variable within an AWS service`.
- Each monitored variable produces a data set that is collected over a time period, resulting in a graph defined by data points.
- The `data points represent the metric data` received from the variable being monitored at an exact point in time, based on the range of times selected.
- For example, with EC2 instances, you can monitor the `metric CPU usage`.

## Statistics

- Each metric that you select for analysis collects data based on a `defined time period`.
- Graphed data is categorized statistically using some of the following terms:
  - Minimum: The lowest value seen during the specified time period
  - Maximum: The highest value seen during the specified time period
  - Sum: All values added together, based on a specific time period
  - SampleCount: The number of data points over a specific time period
  - Average: Calculated from Sum divided by SampleCount, based on the time period

## Dimensions

- A dimension describes the metric and what data it stores. Multiple dimensions can be multiple instances assigned to the metric CPU utilization.

## Units of measurement

- Statistics are defined by bytes, seconds, counts, or percentages.

## Timestamp

- Each metric is stamped with a timestamp that references the exact time when data was received. Each timestamp includes the date, hours, minutes, and seconds based on the current time in UTC format.
## Time range (period)

-  This is the length of time data is collected based on a metric calculated on the defined statistical value. Periods of time can be set from 1 minute up to 15 months. The number of periods determines the number of data points presented on the graph.

## Alarms

- An alarm starts an action based on the state of the metric’s data over the defined time period. Alarms can trigger notifications using SNS topics, an EC2 action, or an Auto Scaling action. You can also analyze the data output for each of the CloudWatch metrics against a custom baseline of defined measurement; if the data is below a defined threshold, all is well. However, once the metric’s results cross or exceed the baseline for a defined time period, the CloudWatch alarm fires, notifying you of potential issues. CloudWatch can also alert an AWS Lambda function and the problem can be fixed—automatically. Once an alarm has been enabled, there are three possible states:
  - OK
    - This means that the data collected and evaluated by CloudWatch still fits within the defined alarm threshold. For example, you may have defined the CPU utilization at 60%. CloudWatch’s analysis of the metric’s data points over a defined evaluation period indicates that CPU utilization is currently at 52%; therefore, everything is still okay.
  - ALARM
    - The metric’s data indicates that the established baseline of acceptable CPU utilization has been breached.
  - INSUFFICIENT DATA
    - There is not enough evaluated data to make a definitive analysis.

## Events

- CloudWatch provides a `near-real-time stream of system events` for most AWS services based on a defined pattern, such as API calls indicating root account usage within the AWS account or any IAM API calls.
- `Events can be stored in a CloudTrail log group` and tracked using a metric filter.
- CloudTrail typically delivers events to the configured log group within `15 minutes of the API call`.
- The target that is notified when the event rule fires can be one of several AWS services, including an SNS topic, a Lambda function, or an SQS queue.

# Additional Alarm and Action Settings

There are some complicated settings that can define how the stream of metric data is handled when it is stored in CloudWatch. Say that an instance runs into problems and doesn’t send data; in this case, the default setting “Missing” means that the alarm doesn’t worry about any missing data points in its evaluation of whether to change the state from OK to ALARM. In other words, the missing data isn’t considered critical.

You could also choose to treat the missing data points as being within the defined threshold; in this case, you would choose Not Breaching. Or you could choose to treat the missing data points as reaching the threshold, in which case you would choose Breaching. Our example uses Breaching under the assumption that if data points are not being delivered to CloudWatch, there’s a problem with the EC2 instance; as a result, the missing data points are critical.

Amazon SNS actions define the type of notification used when an alarm fires. For EC2 instance metrics, you have several choices:
- Send an SNS notification via email or text.
- Choose an Auto Scaling action that adds additional instances to be added, reducing the CPU utilization.

<h2 style="background-color:lightgreen"># Amazon CloudWatch Cheat Sheet</h2>

- Amazon CloudWatch monitors resources such as EC2 instances, EBS volumes, and RDS instances.
- Amazon CloudWatch monitors custom metrics and log files generated by hosted applications.
- Amazon CloudWatch monitors application performance and operational health.
- Amazon CloudWatch logs allow you to monitor and troubleshoot systems and applications.
- Amazon CloudWatch logs allow you to store log files from EC2, AWS CloudTrail, ELB, and Route 53 and other third-party logs.

