AWS Auto Scaling
---

# AWS Services managed by AWS Auto Scaling

## Amazon Aurora

- Increase or decrease the number of read replicas that have been provisioned for an Aurora DB cluster.

## EC2 Auto Scaling

- Increase or decrease the number of EC2 instances in an Auto Scaling group.

## Elastic Container Service

- Increase or decrease the desired task count in ECS.

## DynamoDB

- Increase or decrease the provisioned read and write capacity of a DynamoDB table or global secondary index.

## Spot fleet

- Increase or decrease the target capacity of a spot fleet.
- A spot fleet `enables you to launch a desired number of instances`, called a fleet of instances, `based on the desired price` and number of spot instance types.

# Scaling Plan

- tells AWS Auto Scaling `how to optimize the utilization` of supported AWS resources defined in your scaling plan.
- You can optimize for availability, for cost, or a balance of both options.
- AWS Auto Scaling can also be used to create predictive scaling for EC2 instances that are members of a target tracking EC2 auto scaling group.
- Predictive scaling looks at historic traffic patterns and forecasts and schedules changes in the number of EC2 instances running at the appropriate time.
