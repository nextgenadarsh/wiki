Amazon Simple Notification Service
---

- enables applications, end users, and devices to `send, store, and receive notifications` from different applications, services, and servers.
- is `integrated with Amazon CloudWatch`.
- lets you `decouple your application communications` and react when changes occur to workloads or associated AWS services; for example, changes in a DynamoDB table being monitored by CloudWatch can trigger an alarm when data values increase or decrease.
- SNS messages are `redundantly stored across multiple servers` in `each region`.
- Many AWS cloud services can communicate with SNS topics as a publisher, sending messages and notifications to SNS topics using CloudWatch alarms, Amazon EventBridge, or Amazon Pinpoint.
- To `receive notifications` from Amazon SNS, the appropriate service or end user `subscribes to the desired SNS topic`.
- Each SNS topic can have multiple subscribers:
  - AWS Lambda
    - An SNS notification can be linked to a function to carry out one or more tasks at AWS
  - Amazon SQS
    - Queues can notify SNS topics that messages have been delivered
  - Amazon Kinesis Data Firehose
    - `Capture and upload data` into Amazon S3, Amazon Redshift, or Elasticsearch data stores for further analysis
  - HTTP/S endpoints
    - Deliver SNS notifications `to a specific URL`
  - Email
    - Email subscribers using `push notifications`
- To use Amazon SNS, first create a topic and then associate the topic to a specific event type.

## SNS Integrated Components:

- Publishers
  - applications, or AWS services `send messages` to access points called `topics`.
- Messages
  - can be application-to-application messaging for the following subscribers:
    - Kinesis Data Firehose delivery streams
    - Lambda functions
    - SQS queues
    - HTTP/S endpoints.
  - Messages can also be `application-to-person push notifications` for mobile applications, phone numbers, and email addresses.
- Topics
  - are the `access points to which publishers send messages` asynchronously.
- Clients
  - `subscribe to SNS topics to receive published messages`.

![SNS Publisher and Subscriber Options](../../images/sns-publisher-subscriber.png)
> Fig: SNS Publisher and Subscriber Options

![Creating a Notification Topic](../../images/sns-notification-topic.png)
> Fig: Creating a Notification Topic

<h2 style="background-color:lightgreen"># Amazon SNS Cheat Sheet</h2>

- Amazon SNS provides `push-based` deliveries of messages.
- Messages are application-to-application or application-to-person.
- Application-to-application message delivery choices are `HTTP/HTTPS via email, SQS` queue endpoints, Kinesis Data `Firehose`, and AWS `Lambda`.
- Application-to-person message delivery choices are `SMS, email, and push` notifications.
- `JSON` is the `supported data type for messages`.
- Amazon SNS `messages are stored redundantly` across `multiple AZs`.
