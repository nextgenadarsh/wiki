Refactor to Microservices
===

# Introduction to Refactor to Microservices

- Microservices architecture is a method to design and build software applications as a suite of modular services, each performing a specific functional task, which deploy and access application components via well-defined standard application programming interfaces (APIs). Where possible, you automate the provisioning, termination, and configuration of resources.
![Microservices in action](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f001.jpg)
- To refactor to microservices is to separate the application components into separate microservices so that each microservice has its own data store, scales independently, and deploys on its own infrastructure. Refactoring includes rewriting and decoupling applications, re-architecting a solution, and determining whether you will perform a complete refactor (lift and shift—all in) or only a partial refactor (lift and shift—hybrid).
- To refactor to microservices requires a message infrastructure so that the microservices can communicate with each other. Message queues communicate between applications. AWS provides the message infrastructure that enables you to build microservice architectures without the need to spend the time and effort for a connective infrastructure.

# Amazon Simple Queue Service

- Message-oriented middleware (MoM) supports messaging types in which the messages that are produced (producers) can broadcast and publish to multiple message consumers, also known as message subscribers.
- Amazon Simple Queue Service (Amazon SQS) is a fully managed message queuing service that makes it easy to decouple and scale microservices, distributed systems, and serverless applications to assist in event-driven solutions. Amazon SQS both moves data between distributed application components and helps you to decouple these components. Amazon SQS is the best option for cloud-designed applications that need unlimited scalability, capacity, throughput, and high availability. Amazon SQS temporarily stores messages from a message producer while they wait for a message consumer to process the message.
- The producer is the component that sends the message. 
- The consumer is the component that pulls the message off the queue
- One of the consumers processes each message, and when a consumer processes a message, they remove it from the queue

## Amazon SQS Parameters

An Amazon SQS message has three basic states:
  - Sent to a queue by a producer
  - Received from the queue by a consumer
  - Deleted from the queue
- For most standard queues there can be a maximum of approximately 120,000 in-flight messages
- For first-in, first-out (FIFO) queues, there can be a maximum of 20,000 in-flight messages

## ReceiveMessage

- The ReceiveMessage action waits for a message to arrive. Valid values are integers from 0 to 20 seconds, with the default value of 0.

## Long Polling

- Long polling helps reduce the cost of Amazon SQS by eliminating the number of empty responses (when there are no messages available for a ReceiveMessage request) and false empty responses (when messages are available but are not included in a response).

## VisibilityTimeout

- the duration (in seconds) that the received messages are hidden from subsequent retrieve requests after being retrieved by a ReceiveMessage request. The default VisibilityTimeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours.

## WaitTimeSeconds

- duration (in seconds) for which the call waits for a message to arrive in the queue before returning. If a message is available, the call returns sooner than WaitTimeSeconds. If no messages are available and the wait time expires, the call returns successfully with an empty list of messages.

## ReceiveMessageWaitTimeSeconds

- ReceiveMessageWaitTimeSeconds is the length of time, in seconds, for which a ReceiveMessage action waits for a message to arrive. Valid values are integers from 0 to 20 (seconds), with the default value equal to 0.

## ChangeMessageVisibility

- ChangeMessageVisibility changes the visibility timeout of a message in a queue to a new value. The default VisibilityTimeout setting for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours.

## DelaySeconds

DelaySeconds is the length of time, in seconds, that a specific message will be delayed. Valid values are 0–900, with a maximum of 15 minutes. Messages with a positive DelaySeconds value become available for processing after the delay period is finished. If you do not specify a value, the default value for the queue applies.

## MessageRetentionPeriod

MessageRetentionPeriod is the length of time, in seconds, that Amazon SQS retains a message. It is an integer representing seconds, from 60 (1 minute) to 1,209,600 (14 days). Changes made to the MessageRetentionPeriod attribute can take up to 15 minutes to take effect.

## DeleteMessage

DeleteMessage deletes the specified message from the specified queue. To select the message to delete, use the ReceiptHandle value of the message (not the MessageId that you receive when you send the message). Amazon SQS can delete a message from a queue even if a VisibilityTimeout setting causes the message to be locked by another consumer. Amazon SQS automatically deletes messages kept in a queue longer than the retention period configured for the queue.

## Dead-Letter Queue

- Amazon SQS supports dead-letter queues, which other queues (source queues) can target for messages that cannot process (be consumed) successfully

## Standard Queue Message Failures

- Standard queues continue to process messages until the expiration of the retention period. This ensures continuous processing of messages, which minimizes the chances of your queue being blocked by messages that cannot process. It also ensures fast recovery for your queue.

### Dead-Letter Queue First-In, First-Out Message Queues

- The dead-letter queue of a FIFO queue must also be a FIFO queue. Similarly, the dead-letter queue of a standard queue must also be a standard queue.

Amazon SQS uses FIFO message queues that place the messages in the queue in the order that you receive them. The first messages that you receive display first in the queue. Message groups also follow this order so that when you publish messages to different message groups, each message group preserves the messages’ internal order.

Amazon SQS FIFO queues provide order within message groups, and they delete any duplicate messages that occur within 5-minute intervals.

FIFO queues ensure single processing by consuming messages in sequence from a message group. Thus, although the consumer can continue to retrieve ordered messages from another message group, the first message group remains unavailable until the message that is blocking the queue processes successfully.

## Monitoring Amazon SQS Queues Using Amazon CloudWatch

# Amazon Simple Notification Service

- a flexible, fully managed producer/consumer (publisher/subscriber) messaging and mobile notifications web service that coordinates the delivery of messages to subscribing endpoints and clients. Amazon SNS coordinates and manages the delivery or sending of messages to subscriber endpoints or clients to assist in event-driven solutions.
- The message is delivered to multiple subscribers, which can then consume the message to trigger subsequent processes. A topic allows multiple receivers of the message to subscribe dynamically for identical copies of the same notification.
- By default, Amazon SNS offers 10 million subscriptions per topic and 100,000 topics per account. 
![Amazon SNS workflow](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f009.jpg)

## Features and Functionality

- SNS topic names have a limit of 256 characters

## Amazon SNS APIs

### Owner Operations

### Subscriber Operations

## Clean Up

- You cannot delete a pending subscription, but if it remains pending for 3 days, Amazon SNS automatically deletes it.

## Transport Protocols

### HTTP, HTTPS

### Email, Email-JSON

### Amazon SQS

### SMS

## Amazon SNS Mobile Push Notifications

- You can send push notification messages directly to apps on mobile devices
- Push notification services, such as APNS and GCM, maintain a connection with each app and mobile device registered to use their service. When an app and mobile device are registered, the push notification service returns a device token. Amazon SNS uses the device token to create a mobile endpoint to which it can send direct push notification messages. For Amazon SNS to communicate with the different push notification services, you submit your push notification service credentials to Amazon SNS.
![Amazon SNS mobile endpoint subscriber](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f010.jpg)

## Add Device Tokens or Registration IDs

## Create Amazon SNS Endpoints

## Billing, Limits, and Restrictions

- By default, Amazon SNS offers 10 million subscriptions per topic and 100,000 topics per account

# Amazon Kinesis Data Streams

- a service that ingests large amounts of data in real time and performs real-time analytics on the data. Producers write data into Amazon Kinesis Data Streams, and consumers read data from it.
![Amazon Kinesis Data Streams](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f011.jpg)
- The messages are not deleted when they are consumed
- The consumers save a reference to the last message they view, and messages iterate based on sequence IDs to fetch the latest messages.
- The number of partition keys should typically be much greater than the number of shards, and if you have enough partition keys, the data can be evenly distributed across the shards in a stream.

## Multiple Applications

- It is the application’s responsibility to track its checkpoint within the data stream.
- Records automatically delete after their retention interval expires, which you configure. The default retention interval is 1 day, but you can extend it up to 7 days

## High Throughput


## Real-Time Analytics

- Amazon Kinesis Data Streams enable real-time analytics, which produces metrics from incoming data as it arrives

## Open Source Tools

- Open source tools, such as Fluentd and Flume, support Amazon Kinesis Data Streams as a destination, and you can use them to publish messages into an Amazon Kinesis data stream.

## Producer Options

- After you create the stream in Amazon Kinesis data stream, you need two applications to build your pipeline: a collection of producers that write data into the stream and consumers to read the data from the stream.

### Amazon Kinesis Agent

This is an application that reads data, appends to a log file, and writes to the stream. The benefit of the Amazon Kinesis Agent is that it does not require you to write application code.

### Amazon Kinesis Data Steams API 

You write an application to use the Amazon Kinesis Data Streams API to put data on the stream.

### Amazon Kinesis Producer Library (KPL)

The KPL gives you a higher-level interface over the low-level Amazon Kinesis Data Streams API. It has the logic to retry failures and to buffer and batch-send multiple messages together. The KPL makes it easier to write messages into a stream than if you use the low-level API.

## Consumer Options

### Amazon Kinesis Data Streams API 

### Amazon Kinesis Client Library

### AWS Lambda

# Amazon Kinesis Data Firehose

- Amazon Kinesis Data Firehose can replace the CoDA service to ingest data. In many business applications, you require a real-time pipeline, but you do not require latency of a few seconds. You can afford to have latency that can run anywhere from 1–15 minutes.
- Amazon Kinesis Data Firehose is easier to use than Amazon Kinesis Data Streams, as it does not require you to write a consumer application. Data that arrives at the Amazon Kinesis Data Firehose is automatically delivered to both Amazon S3 and the other destinations. From Amazon S3, you can deliver the data to Amazon Redshift, Amazon Elasticsearch Service, and Splunk.
- Amazon Kinesis Data Firehose also handles dynamically scaling the underlying shards of the stream based on the amount of traffic.
- You can also configure Amazon Kinesis Data Firehose to transform your data before you deliver it.


# Amazon Kinesis Data Analytics

- enables you to process and analyze streaming data with standard structured query language (SQL). It also enables you to run SQL code against streaming sources to perform time-series analytics, feed real-time dashboards, and create real-time metrics
- supports ingesting from either Amazon Kinesis Data Streams or Amazon Kinesis Data Firehose, and it continuously reads and processes streaming data
![Amazon Kinesis Data Analytics flow](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f012.jpg)
- Use Cases:
  - Generate time series analytics You can calculate metrics over time windows and stream values to Amazon S3 or Amazon Redshift through a Firehose delivery stream.
  - Feed real-time dashboards You can send aggregated and processed streaming data results downstream to feed real-time dashboards.
  - Create real-time metrics You can create custom metrics and triggers for use in real-time monitoring, notifications, and alarms.


# Amazon Kinesis Video Streams

- Use the Amazon Kinesis Video Streams service to push device video content into AWS and then onto the cloud to process that content and detect patterns in it.

You can use Amazon Kinesis Video Streams to build computer vision and machine learning applications.

A single stream can support one producer connection and three consumer connections at a time.

# Amazon DynamoDB Streams

- integrates with Amazon DynamoDB to publish a message every time a change is made in a table. When you insert, delete, or update an item, Amazon DynamoDB produces an event, which publishes it to the Amazon DynamoDB Streams
![Amazon DynamoDB Stream](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f013.jpg)

## Use Case

- continuously poll the database to indicate if a variable changes

## Amazon DynamoDB Streams Consumers

- Amazon DynamoDB integrates with AWS Lambda so that you can create triggers, which are pieces of code that automatically respond to events in DynamoDB Streams. With triggers, you can build applications that react to data modifications in DynamoDB tables.

## Amazon DynamoDB Streams Concurrency and Shards

- Amazon DynamoDB Streams publishes the changes in your table into multiple shards.
- If you create a consumer application using AWS Lambda, each AWS Lambda instance processes the messages in a particular shard. This enables concurrent processing and allows Amazon DynamoDB Streams to scale to handle a high volume of concurrent changes

# AWS IoT Device Management

- A cloud-based service that makes it easy for customers to manage IoT devices securely throughout their lifecycle
- This remote management includes over-the-air (OTA) updates to device software.
- manages devices associated with the Internet of Things, collects data from them, and sends out commands with updates to their state
![AWS IoT Device Management](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f014.jpg)

## Rules Engine

- When messages enter the AWS IoT Device Management service, the service dispatches them to different AWS endpoints. AWS IoT rule actions specify what to do when a rule is triggered. AWS IoT can dispatch the messages to AWS Lambda, an Amazon Kinesis data stream, a DynamoDB database, and other services. This dispatch is done through the AWS IoT rules engine. Rules give your devices the ability to interact with AWS products and services. Rules are analyzed, and actions occur based on the MQTT topic stream.

## Message Broker

- a publish/subscribe broker service that enables you to send messages to and receive messages from IoT
- AWS IoT does not send and receive messages across AWS accounts and regions.

## Device Shadow

- an always-available representation of the device, which allows communications back from cloud applications to the IoT devices
- Cloud applications can update the device shadow even when the underlying IoT device is offline. Then when the device is brought back online, it synchronizes its final state with a query to the AWS IoT service for the current state of the instances.
- A device’s shadow is a JavaScript Object Notation (JSON) document that stores and retrieves current state information for a device

# Amazon MQ

-  a managed message broker service for Apache ActiveMQ that makes it easy to migrate to a message broker on the cloud. Amazon MQ is a managed Apache Active MQ that runs on Amazon EC2 instances that you select. AWS manages the instances, the operating system, and the Apache Active MQ software stack. You place these instances in your Amazon Virtual Private Cloud (Amazon VPC) and control access to them through security groups.



# AWS Step Functions

- enables you to launch and develop workflows that can run for up to several months, and it allows you to monitor the progress of these workflows. You can coordinate the components of distributed applications and microservices by using visual workflows to build applications quickly, scale and recover reliably, and evolve application easily
- enables the compute to be stateless
![AWS Step Functions](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c11f015.jpg)

## State Machine

- workflow template that is made up of a collection of states. Each time you launch a workflow, you provide it with an input. Each state that is part of the state machine receives the input, modifies it, and passes it to the next state.
- You can use AWS Step Functions as event sources to trigger AWS Lambda
- Use AWS Step Functions to build visual workflows that enable fast translation of business requirements into technical requirements. You can build applications in a matter of minutes. When your needs change, you can swap or reorganize components without customizing any code.

## Task State

- A task state involves a form of compute. A task executes on an AWS Lambda function or on an Amazon EC2 instance. An activity is a task that executes on an Amazon EC2 instance.

## Choice State

- The Choice state enables control flow between several different paths based on the input you select. In a choice state, you place a condition on the input. The state machine evaluates the condition, and it follows the path of the first condition that is true about the input.
- A Choice state may have more than one Next, but only one within each Choice Rule. A Choice state cannot use End.

## Choice Rules

A Choice state must have a Choices field whose value is a nonempty array and whose every element is an object called a Choice Rule. A Choice Rule contains the following:
- omparison Two fields that specify an input variable to compare, the type of comparison, and the value to which to compare the variable.
- Next field The value of this field must match a state name in the state machine.

## Parallel State

- The Parallel state enables control flow to execute several different execution paths at the same time in parallel. This is useful if you have activities or tasks that do not depend on each other, can execute in parallel, and can help your workflow complete faster.

## Parallel State Output

A Parallel state provides each branch with a copy of its own input data (InputPath). It generates output, which is an array with one element for each branch that contains the output from that branch. There is no requirement that all elements be of the same type. You can insert the output array into the input data (and the whole sent as the Parallel state’s output) with a ResultPath field

## Error Handling

- If any branch fails, because of an unhandled error or by a transition to a Fail state, the entire Parallel state fails, and all of its branches stop. If the error is not handled by the Parallel state itself, Step Functions stops the execution with an error.

- When a Parallel state fails, invoked AWS Lambda functions continue to run, and activity workers that process a task token do not stop.

## End State

A state machine completes its execution when it reaches an end state. Each state defines either a next state or an end state, and the end state terminates the execution of the step function.

## Input and Output

Each execution of the state machine requires an input as a JSON object and passes that input to the first state in the workflow. The state machine receives the initial input by the process initiating the execution. Each state modifies the input JSON object that it receives and injects its output into this object. The final state produces the output of the state machine.

## Paths and Reference Paths

Paths In Amazon States Language, a path is a string that begins with $ that you can use to identify components within JSON text. Paths follow the JsonPath syntax.

Reference paths A reference path is a path whose syntax can identify only a single node in a JSON structure.

You can access object fields with only a dot (.) and square brackets ([ ]) notation.
Paths and reference paths do not support the operators @ .. , : ? * and functions such as length().

## AWS Step Functions Use Case

- process long-running workflows