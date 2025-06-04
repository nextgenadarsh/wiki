AWS Elastic Beanstalk
---

- enables developers to `upload their application code` and Elastic Beanstalk will automatically `handle the deployment, scaling, and management of the underlying infrastructure`.
- allows you to deploy different runtime environments across multiple technology stacks running on EC2 instances or Docker containers.
- automates both `application deployment` and the `infrastructure components` required by the application, including single and multiple EC2 instances, load balancers, and EC2 Auto Scaling.
- Monitoring is carried out with CloudWatch metrics for monitoring the health of your application infrastructure.
- also integrates with [AWS X-Ray](../monitoring/x-ray.md), which can `monitor and debug` the internal operations of your hosted application.

Updating Elastic Beanstalk Applications
---

# All at once

- The new application version is `deployed to all EC2 instances simultaneously`.
- The `current application is unavailable` while the deployment process is underway.
- To keep an older version of your application functioning until the new version is deployed, choose the immutable method or the blue/green update method.

# Rolling

- The application is `deployed in batches` to a select number of EC2 instances defined in each batch configuration.
- As the batches of EC2 instances are being updated, they are `deregistered from the load balancer queue`.
- When the update is successful and the instances pass load-balancing health checks, the `instances are registered to the load-balancing target group` again.

# Immutable

- The application update is only installed on new EC2 instances contained in a `second Auto Scaling group` launched in your environment.
- Only after the new environment passes health checks is the old application version removed.
- The new application servers are made available `all at once`.
- Because new EC2 instances and Auto Scaling groups are being deployed, the `immutable update process takes longer`.

# Blue/Green

- The new version of the application is `deployed to a separate environment`.
- When the new environment is healthy, the `CNAMEs of the two environments are swapped`, so traffic is redirected to the new application version.
- In this scenario, if a production database is to be used in the application design to maintain connectivity, the database must be installed separately from the Elastic Beanstalk deployment.
- Externally installed databases remain operational when the new Elastic Beanstalk application version is installed and swapped on the application’s EC2 instances.

# Traffic-Splitting Deployments

- `Canary testing` can also be included in your application deployment. 
- Elastic Beanstalk can launch a set of new instances with a new version of the application; however, `only a specific percentage of incoming traffic will initially be forwarded to the new application instances` for a defined time.
- If the new application instances remain healthy during the evaluation period, Elastic Beanstalk then forwards traffic to the new instances and terminates the old instances.
- If the new instances don’t pass their health checks, traffic is moved back to the current instances, and the new instances that were under evaluation are terminated, leaving the existing instances online with `no service interruption`.

