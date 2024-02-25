Route Tables
---

- Used to `control subnet traffic` using a set of rules, called routes, that determine where network traffic is directed within each VPC.
- Each subnet must be associated with a route table. If no specific route table association has been configured, the subnet will use the `main route table`.
- Multiple subnets can be associated and controlled with a single route table that is assigned to multiple subnets.
- You might have multiple private subnets that need routes to the same service, such as a route to the NAT gateway service enabling resources on private subnets to get updates from a public location on the Internet, or a route to the virtual private gateway (VGW) for VPN connections from external locations.

# The Main Route Table

- Each VPC has a default route table called the main route table. 
- Associated with a VPC after it is first created.
- Provides local routing services throughout each VPC and across all defined AZs (AZs)
- Defines the routing for all subnets that are not explicitly associated with any other custom route table.
- Cannot be deleted; however a custom route table can be associated with a subnet, replacing main route table association.

# Custom Route Tables

- A `user-defined` routing table that `enables custom routes to direct traffic` to specific destinations or implement more complex network architectures.

# Route Table Cheat Sheet

- Each VPC has a main route table that provides local routing throughout each VPC.
- Each subnet, when created using the VPC dashboard, is implicitly associated with the main route table.
- Don’t add additional routes to a main route table. Leaving the main route table in its default state ensures that if the main route table remains associated to a subnet by mistake, the worst that can happen is that local routing is enabled.
- The main route table cannot be deleted; however, it can be ignored and will remain unassigned if you do not associate it with any subnets within the VPC.
- Create and assign a custom route table for custom routes required by a subnet.
- Subnet destinations are matched with the most definitive route within the route table that matches the traffic request.
