Network Load Balancer (NLB)
---

 - is a load balancing service that `distributes incoming traffic across multiple targets`, such as Amazon EC2 instances, containers, and IP addresses, in `one or more AZ`.
 - provides `TCP and UDP load balancing at Layer 4` of the OSI stack.
 - uses a `flow-based algorithm to distribute traffic` to the targets in a target group.
 - distributes traffic `based on the number of connections` rather than on the amount of data transferred. The NLB can scale to handle millions of requests per second at very low latencies.
 - It can also `integrate with EC2 Auto Scaling`, Amazon ECS, and AWS ACM. NLB supports end-to-end encryption using TLS.

# Features of NLB

- TLS offloading
  - Client TLS session termination is supported, allowing TLS termination tasks to be carried out by the load balancer.
- Server Name Indication (SNI)
  - Serves multiple websites using a single TLS listener.
- AWS Certificate Manager: Manages server certificates.
- Sticky sessions
  - Can be defined per target session.
- Preserve client-side source IP address
  - Backend servers can see the IP address of the client.
- Static IP address
  - A static IP address is provided per AZ.
- EIP support
  - An Elastic IP address can be assigned for each AZ.
- DNS fail-over
  - If there are no healthy targets available, Route 53 directs traffic to load balancer nodes in other AZs.
- Route 53 integration
  - Route 53 can route traffic to an alternate NLB in another AWS region.
- Zonal isolation
  - The NLB can be enabled in a single AZ, supporting applications that require zonal isolation.

<h2 style="background-color:lightgreen"># NLB Cheat Sheet</h2>

- The NLB can load balance applications hosted at AWS and on premises using IPv4/IPv6 addresses.
- The NLB supports connections across peered VPCs in different AWS regions.
- The NLB supports long-running connections, which are ideal for WebSocket applications.
- The NLB supports failover across AWS regions, using Route 53 health checks.
- With the NLB, the source IP addresses of the clients that are connecting are preserved.
- Each NLB allows for extremely high throughput; an NLB can scale and handle millions of requests per second.
- The NLB flow-based algorithm is ideal for latency-sensitive TCP/UDP applications.
- The NLB provides “end-to-end security” with TLS termination performed by the NLB.

# Multi-Region Failover

- An NLB supports failover across AWS regions using Route 53 health checks, allowing organizations to create a highly available, globally distributed load balancing solution that can route traffic to the optimal region based on the health of the targets in each region.

- An NLB must be created in each AWS region where traffic will be load balanced. Then create a target group in each region that contains the regional targets to which to route traffic. Enable cross-zone load balancing for each NLB so traffic is distributed across the targets in each AZ.

- Next, create an Route 53 health check for each target group. You can use the default health check configuration or customize the health check settings to meet your specific requirements.

- Finally, create a Route 53 record set that points to the NLB in each AWS region. Choices are a weighted record set, or a latency-based record set to specify the routing policy for the record set. With a weighted record set the proportion of traffic that should be routed to each region is controlled based on the weights assigned to the record set. With a latency-based record set, Route 53 routes traffic to the region that provides the lowest latency for the end user.

# CloudWatch Metrics

CloudWatch metrics for ELB can be used to monitor and ensure that a workload is performing as expected.

ELB Metric  | Description
--  | --  
ActiveConnectionCount | The number of concurrent TCP frontend and backend connections
ConsumedLCUs  | The number of Load Balancer Capacity Units used
NewConnectionCount  | The total number of TCP connections from clients to the load balancer to targets
ProcessedBytes  | The total number of bytes processed by the load balancer
RequestCount  | The number of requests processed with responses from a target
HealthyHostCount  | The number of targets that are healthy
UnhealthyHostCount  | The number of targets that are unhealthy
RequestCountPerTarget | The average number of requests received by each target in a group

