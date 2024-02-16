AWS Global Accelerator
---

- `routes traffic over the AWS private network to the closest available edge location endpoint that is closest to the end user`.
- End user traffic enters the closest edge location and the Global Accelerator routes traffic to the closest application endpoint.
- The application outbound traffic returns over the AW private network back to the end user using the optimal endpoint (edge location).
- Application endpoints can be created in single or multiple AWS regions. Global Accelerator uses accelerators to improve the performance of applications for local and global users.
- uses listeners to process inbound connection requests from end users based on the TCP port or port range specified for a single or multiple listeners.
- Each listener has one or more endpoint groups associated with it. Endpoint groups use endpoints in the defined AWS region and traffic is forwarded to the available endpoints in one of the groups.
- Both listener and endpoint ports can also be remapped to custom ports using port overrides.

# Standard accelerator

- automatically `routes traffic to the optimal AWS region with the lowest latency, using static Anycast IP addresses` that are globally unique and do not change.
- For a standard accelerator with IPv4 addresses, `endpoints can be Network Load Balancers, Application Load Balancers, EC2 instances, or Elastic IP addresses`.
- With `dual-stack addresses` (IPv4/IPv6), `only Application Load Balancer endpoints` that have been configured to support dual-stack are supported.
- Use case:
  - Applications that require a `consistent, low-latency connection, such as web applications, mobile applications, and gaming applications`.
  - Each listener created in a standard accelerator can include one or more endpoint groups; each listener has a Traffic dial that can be used to increase or decrease traffic to each endpoint in the selected AWS region.

# Custom accelerator

- maps listener port ranges to a specific Amazon EC2 private IP address and port destination in an AWS VPC and subnet.
- can logically map one or more end users to a specific destination, such as a gaming application with multiple players or a training application that needs to assign multiple end users to a specific server for video training sessions.
- is `mapped to an AWS VPC endpoint` with a destination port range that maps the incoming client connections.
- Use cases:
  - Single-region applications
    - End users’ traffic is sent over 90 global edge locations onto Amazon’s private network and sent to your application origin.
  - Multi-region applications
    - Static IPs can be mapped to multiple application endpoints across AWS regions.
  - Multi-region storage
    - S3 Multi-Region Access Points rely on the AWS Global Accelerator for accessing data sets stored in S3 buckets across multiple AWS regions.

![Multi-Region Global Accelerator Operation](../../images/global-accelerator-operation-multi-region.png)
> Fig: Multi-Region Global Accelerator Operation


