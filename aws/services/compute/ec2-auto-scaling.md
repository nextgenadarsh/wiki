EC2 Auto Scaling
---

- service enables you to `automatically scale your Amazon EC2 resources` in response to changes in demand for your application.
- helps you ensure that you have the right number of Amazon EC2 instances available to meet the needs of your application, without having to manually create or terminate instances.

# EC2 Auto Scaling  Terms

## Policies

- Amazon EC2 Auto Scaling uses scaling policies to `determine when to scale` your Amazon EC2 resources up or down.
- You can create simple scaling policies based on a single metric, such as `CPU utilization`, or you can create more complex policies that `use multiple metrics` based on the size of your Amazon EC2 fleet of instances.

## Scaling actions

- When a scaling policy is triggered, Amazon EC2 Auto Scaling takes a scaling action `to either launch or terminate Amazon EC2` instances.
- The number of instances to launch or terminate can be defined, or you can use a percentage to scale the number of instances relative to the size of your Amazon EC2 fleet.

## Scaling groups

- Amazon EC2 Auto Scaling groups are `logical collections of Amazon EC2 instances that are managed as a single entity`.
- Multiple scaling groups can be created with their own scaling policies and configurations.

## Health checks

- Amazon EC2 Auto Scaling `uses health checks to ensure that only healthy Amazon EC2 instances are used to serve traffic`.
- If an instance fails a health check, it is terminated and replaced with a new instance.

## CloudWatch alarms

- Amazon EC2 Auto Scaling uses CloudWatch alarms and SNS notifications to trigger scaling actions based on metrics with defined thresholds linked to alarms.
- For example, an alarm can send an SNS notification when the CPU utilization of your Amazon EC2 instances exceeds a certain threshold, triggering a scaling action to launch additional instances.

# EC2 Auto Scaling Operation

# EC2 Auto Scaling Components

## Launch Configuration

- is a `simple template used by an ASG to launch EC2 instances`.
- The process of creating a launch configuration is `much like the process to manually launch an EC2 instance` from the AWS Management Console.
- `contains the installation details for the EC2 instances` that will be built by the ASG.
- is `associated with one ASG`.
- includes numerous system components, including the instance ID of the AMI, the instance type to build, the key pair for authentication, the desired security groups, and a block storage device.
- are `slowly being superseded by the launch template`, which `has many additional settings` that can be used when deploying instances.

## Launch Templates

- is `similar to a launch configuration`, `with added features` related to `versioning` an existing template, so you can make changes.
- support all new AWS features related to EC2 instances and Auto Scaling, whereas launch configurations do not.
- A default launch template can be created as a source template; then, other versions of the template can be created and saved.
- AWS recommends that you `use launch templates rather than launch configurations` because a launch template has many deployment options when compared to a launch template.

# Auto Scaling Groups (ASG)

- is `built from a collection of EC2 instances` that have been generated from the associated launch configuration or launch template.
- Each ASG launches instances, following the parameters of the launch template, to meet the defined scaling policy.
- An ASG can `function independently or be associated with a load balancer`.
- `Scaling policies are attached to ASGs`, which automatically increase or decrease the number of EC2 instances.
- The EC2 instance types that can be added to an ASG include on-demand, spot, or reserved instances across multiple AZs.
- You can also define the percentage of on-demand and spot instances to deploy for additional cost savings.
- An ASG `performs health checks` on instances added to the ASG; ELB health checks can also be chosen.
- If instances added to an ASG fail their status checks after boot, they are considered unhealthy, and EC2 Auto Scaling terminates, relaunches, and re-adds them to the ASG.
- `ELB health checks are a little more rigorous` than Auto Scaling health checks, and `ASGs can and should be configured to also use ELB health checks`.

# Scaling Options for Auto Scaling Groups

## Target tracking scaling policy

- You can select the `metric type and target value` to maintain the desired capacity and automatically have any instances that are determined to be unhealthy (by the Auto Scaling health check or the load-balancing health check) replaced.

## Simple scaling

- You can increase and decrease the size of an ASG based on a `single metric` and automatically manage the size of the EC2 instances in the Auto Scaling group.
- An Auto Scaling group has three key parameters that determine the size and capacity of the group:

### Minimum size

- is the `minimum number of Amazon EC2 instances that you want to have running` in your Auto Scaling group at any given time.
- The minimum size cannot be set to a value lower than the current size of the group.

### Maximum size

- is the `maximum number of Amazon EC2 instances that you want to have running` in your Auto Scaling group at any given time.
- The maximum size cannot be set to a value higher than the current size of the group.

### Desired capacity

- is the `number of Amazon EC2 instances that you want to have running` in your Auto Scaling group at a given time.
- can be any integer value `between the minimum size and the maximum size, inclusive`.

## Step scaling

- enables you to `define a series of steps, or thresholds, for a metric, and specify a different number of Amazon EC2 instances or capacity units to launch or terminate for each step`.
- Step scaling enables you to `define lower and upper boundaries` for the metric being used and to define the amount by which to scale in or scale out the instances with incremental steps in or out:
  - A first instance is added when CPU utilization is between 40% and 50%.
  - The next step adds two instances when CPU utilization is between 50% and 70%.
  - In the third step, three instances are added when CPU utilization is between 70% and 90%.
  - When CPU utilization is greater than 90%, a further four instances are added.
- policy also defines a `warmup period` which is a period of time that you can specify during which Amazon EC2 Auto Scaling will not take any scaling actions in response to a trigger to add additional instances.

## Scale based on a schedule

- Scaling can be defined based on time and date values that instruct Auto Scaling to scale up or down at a specific time. The start time and the minimum, maximum, and desired sizes can be set for recurring actions.

# Management Options for Auto Scaling Groups

## Predictive scaling

- `uses machine learning` models to analyze the deployed application and traffic pattern history to `forecast recommended scaling`.
- In the case of a workload that has high usage during normal business hours and lower usage overnight, predictive scaling can add capacity before an increase in daily traffic occurs.

## Warm pools

- allow you to `reduce scale-out latency by maintaining a pool of pre-warmed EC2 instances ready to be immediately placed into service` when a scale-out event is issued.

## Instance refresh

- can be used to `update the instances currently in an ASG instead of replacing the instances one at a time`.
- can be useful to `deploy a new AMI or new user data script`.
- Instances can also be replaced by specifying the maximum amount of time an instance can be in service before it is terminated and replaced.
- A minimum instance refresh value of at least 1 day must be initially set.

# Cooldown Period

- Simple scaling policies are bound to a cooldown period.
- When a cooldown period is in force, even after the ASG is directed to launch an EC2 instance on a scale-out request, all scaling requests are ignored until the cooldown period finishes.
- The default cooldown period is `300 seconds`; you can change this value when creating an ASG or at a later point if you wish to make modifications.

# Termination Policy

- When a scale-in event occurs, defined default termination policies `control which EC2 instances are first terminated`.
- The default termination policy is designed to ensure that your instances are evenly spaced across the availability zones to maintain high availability.
- Termination of unhealthy instances occurs first; then Auto Scaling attempts to launch new instances to replace the terminated instances.
- Other termination options that can be chosen for a custom termination policy include the following:
  - Oldest launch template
    - Remove instances that are using an older launch template.
  - Oldest launch configuration
    - Remove instances that are using an older launch configuration.
  - Closest to next instance hour
    - Terminate instances that are closest to the next billing hour.
  - Newest Instance
    - Terminate the newest instance in the ASG.
  - Oldest Instance
    - Terminate the oldest instance in the ASG.
  - Allocation strategy
    - Terminate instances based on on-demand or spot instance strategies.

# Lifecycle Hooks

- Custom actions that are carried out on instances that an ASG launches or terminates.
- With such an action, an instance is placed into a wait state and held from becoming registered in the ASG or from being terminated for a period of time.
- While it is being held in the wait state, custom actions can be performed on the instance.
- Think of a wait state as an opportunity to perform any task you want on an EC2 instance before it is added to or removed from the ASG.
- An instance can be held in a `wait state for a maximum of 48 hours`. During the wait time, the following custom actions are allowed:
  - Call an AWS Lambda function to perform a specific task.
  - Send a message to a defined SNS notification.
  - Execute a script as the instance starts and remains in the defined wait state.
  - Add a lifecycle hook to an ASG by using AWS CLI commands that populate the user data location in a launch template.

<h2 style="background-color:lightgreen"># EC2 Auto Scaling Cheat Sheet</h2>

- EC2 Auto Scaling ensures that you have the correct amount of compute power required by an application at all times.
- An Auto Scaling group is a collection of EC2 instances that can provide horizontal scaling across multiple AZs.
- An Auto Scaling group requires an attached Auto Scaling policy.
- EC2 Auto Scaling can be integrated with ELB target groups and Amazon CloudWatch metrics and alarms.
- A launch template is a template used by Auto Scaling to create additional EC2 instances as required.
- Application Load Balancers, Network Load Balancers, and Gateway Load Balancers can be attached to an Auto Scaling group.
- Load balancers must be deployed in the same region as the Auto Scaling deployment.

