Network Access Control List (NACL)
---

- `Software firewall` that `controls inbound and outbound` traffic for each `subnet` within a VPC.
- `Stateless`
- a set of rules that allows or denies traffic based on the source and destination IP addresses, ports, and protocols.
- Both TCP and UDP are supported
- Each `VPC` is associated with a `default NACL` allowing all traffic
- 1 NACL <--> M Subnet in VPC

# NACL Cheat Sheet

- A NACL is an optional security control for subnets.
- Each VPC is assigned a default NACL that allows all inbound and outbound traffic across all subnets.
- NACLs are stateless in design; inbound and outbound rules are enforced independently.
- Each NACL is a collection of deny or allow rules for both inbound and outbound traffic.
- The default NACL can be modified.
- A NACL has both allow and deny rules.
- A NACL applies to both ingress and egress subnet traffic; it does not apply to traffic within the subnet.
- You can create custom NACLs and associate them to any subnet in a VPC.
- A custom NACL can be associated with more than one subnet.
- A subnet can be associated with only one NACL.
- A NACL is a first line of defense at the subnet level; a security group is a second line of defense at the instance.

