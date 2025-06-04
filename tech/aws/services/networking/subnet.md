Subnet
---

- is a `range of IPv4 or IPv6 addresses within a VPC` that is `associated with a specific AZ`.
- When you create a subnet, `you specify the CIDR block for the subnet`, which determines the range of IPv4 and IPv6 addresses that are available for use in the subnet.
- You can create `multiple subnets within a VPC`, and `each subnet can span one or more AZs`. You can also specify a different CIDR block for each subnet.
- Each subnet that you create resides within its assigned AZ
- When creating an `IPv6 subnet`, you will need to specify the IPv6 network range for the subnet and the number of IPv6 addresses that the subnet will contain.
- You can also create route tables and security groups to control inbound and outbound traffic for the IPv6 subnet.

There are several benefits to creating subnets within a VPC:

- Network security
  - Subnets can help you segment your network and isolate resources from each other, which can improve security and reduce the risk of unauthorized access.
- Network management
  - Subnets can help you organize and manage your network more efficiently, by allowing you to group resources based on their purpose or location.
- Control traffic flow
  - Subnets can help you control the flow of traffic between resources within the VPC and between the VPC and the Internet, by allowing you to specify different routing rules for different subnets.

# Public subnet

- If a subnet’s associated route table `forwards traffic to the Internet through an Internet gateway`, the subnet is defined as a public subnet.

# Private subnet

- If a subnet’s associated route table has no gateway or endpoint to direct traffic to, it is a private subnet, as traffic remains on the local subnet with no external connectivity.
- A subnet with no external gateway connectivity is a private subnet.

# Protected subnet

- Protected subnets are often used to host resources that need to be `isolated from the public Internet` for security or compliance reasons, such as database servers or application servers.
- The subnet’s route table `allows inbound and outbound traffic only to and from resources within the subnet`.

# <h2 style="background-color:lightgreen">Subnet Cheat Sheet</h2>

- Subnets are contained within an AZ.
- IPv4 or IPv6 subnets can be created.
- IPv6-only subnets can be created.
- Subnets host EC2 instances.
- Public subnets have access to the Internet.
- Public subnets are for hosting infrastructure resources such as load balancers or NAT services.
- Private subnets are private, with no direct Internet access, although NAT services can provide indirect Internet access.
- A subnet cannot span multiple AZs.
- If a subnet’s traffic is routed to an Internet gateway, the subnet is a public subnet because there is a defined path to the Internet.
- If a subnet does not have a route to the Internet gateway, the subnet is a private subnet with no external destination defined.
- If a subnet has a route table entry that routes traffic to a virtual private gateway, the subnet is known as a VPN-only subnet, and it can be connected by using an external VPN connection.

