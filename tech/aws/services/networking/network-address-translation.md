Network Address Translation (NAT)
---

- Provide an indirect path for EC2 instances hosted on private subnets that need `Internet access` to obtain updates, licensing, or other external resources `without exposing their private IP addresses`.
- Services with NAT:
  - Amazon Virtual Private Cloud (VPC) NAT Gateway
    - Enables instances in a private subnet to access the Internet.
  - AWS Transit Gateway NAT
    - Enables instances in a VPC or on-premises network to access the Internet.
  - AWS PrivateLink NAT Gateway
    - Enables instances in a VPC to access resources in another VPC or on-premises network.

# NAT Gateway Service

- `Hosted in a public subnet` configure `with an Elastic IP` address (a static public IP address).


# NAT Instance

- 

# NAT Gateway Service Cheat Sheet

- An AWS NAT gateway must be hosted in a public subnet.
- An AWS NAT gateway uses an Elastic IP address as its static public IP address.
- The AWS NAT gateway service does not support security groups.
- The AWS NAT gateway service does not support port forwarding.
