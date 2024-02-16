IP Address
---

# Private IPv4 Addresses

- When a new EC2 instance is created and launched, by default, AWS assigns a `primary private IP address to the default elastic network interface card (eth0)` from the range of available IP subnet addresses.
- Network interfaces attached to EC2 instances are defined at AWS as elastic network interfaces (ENIs). Private IP addresses only communicate across the private network at AWS. A private DNS hostname that points to the associated private IPv4 address is also assigned to each EC2 instance. Private IP addresses are defined as addresses that are not routable over the Internet, regardless of whether they are used at AWS or on premises. If you choose to manually assign a primary private IP address, the private IP address chosen must be available in the subnet IP address range where the EC2 instance will reside. You can assign any private IP address in the assigned subnet range to an EC2 instance if it is not currently in use or reserved by AWS for its communication needs.


- Once a primary private IP address is assigned, the EC2 instance retains the address for the lifetime of the EC2 instance.

Additional (secondary) private IP addresses can also be assigned to ENIs of an EC2 instance, and these addresses can be unassigned and moved to other EC2 instances that reside on the same subnet at any time.


- Cost is a factor here. Communication between EC2 instances residing on the same subnet using their private IP addresses is free of charge. However, EC2 instances using private IP addresses located on subnets in different AZs are charged an outbound data transfer fee for communicating with each other.

## Private IPv4 Address Summary

- A private IP address is assigned by default to every EC2 instance on `both public and private subnets`.
- Here are some other criteria to remember:
  - EC2 instances don’t need to use public IP addresses; however, an EC2 instance is always assigned a private IP address.
  - A private IP address is assigned for the life of each EC2 instance. The IP address remains attached until the EC2 instance is terminated.

# Public IPv4 Addresses

Public IP addresses are used to access resources that have been placed in a public subnet, which is a subnet that is configured to allow inbound and outbound traffic to and from the Internet. A public IP address is typically assigned from AWS’s pool of public IP addresses, as shown in Figure 11-29. Public IP addresses from AWS’s own pool are managed and controlled by AWS and are therefore not permanently assigned to an EC2 instance. Instances in a public subnet can be assigned a public IP address automatically when they are launched. These public IP addresses are dynamic and are associated with the instance until it is stopped or terminated. Whether or not your EC2 instance receives a public IP address during creation is dependent on how the public IP addressing attribute has been defined on the subnet where the EC2 instance is to be hosted. At the subnet attribute level of any subnet you have created, the IPv4 public addressing attribute is initially set to false, which means no public IPv4 address will be assigned to any EC2 instance at creation.

You can enable the public IP addressing attribute during the creation of an EC2 instance; if you do, an AWS-controlled public IP address is assigned, overruling the default state of the subnet’s public IP address attribute.

## Elastic IP Addresses

- is a `static public IPv4 address` that is created and assigned to your AWS account and can be easily remapped to any EC2 instance or elastic network interface in your AWS account.
- They are useful for EC2 instances or services, such as NAT gateway services that need to be reachable from the Internet and require a consistent, static IP address. Requesting an EIP address is simple: Request an EIP address, as shown in Figure 11-30, and it’s added to your AWS account from the regional pool of available EIP addresses. EIPs are unassigned; you need to first assign an EIP to the desired VPC and then to the desired EC2 instance.

AWS advertises each regional pool of its EIPs across the public Internet and to all other AWS regions. Because of this advertising, EIPs hosted at AWS can be located across the public Internet and within the public AWS address space.

When an EC2 instance has been assigned an EIP address, turning the EC2 instance off and back on is not an issue. The EIP address remains attached because it’s assigned to your AWS account and to the EC2 instance. And there’s no additional charge for ordering and assigning a single EIP address to an EC2 instance. However, if you order but don’t assign an EIP address, AWS charges you because EIPs are in limited supply.

At AWS, there are four public pools of IP addresses to consider:

- Dynamically assigned public IPv4 addresses: Assigned to EC2 instances and returned to the common public pool of AWS addresses when an EC2 instance shuts down, releasing its dynamically assigned public IPv4 address.
- Elastic IP addresses: Elastic IP addresses are static, public IP addresses that are allocated to your AWS account.
- BYOIP public IPv4 and IPv6 addresses: Detailed in the upcoming section “Bring-Your-Own IP (BYOIP).”
- Global unicast IPv6 addresses: These addresses are unique, globally routable addresses that are assigned to VPCs and subnets. They are used to communicate with resources on the Internet and can be assigned to instances, ELBs, and other resources in a VPC.

The public IPv4 address is displayed as an attribute of the network interface when viewed through the AWS EC2 dashboard, but the internal wiring is a little more complicated. On an EC2 instance with a public IP address, this address is internally mapped to the EC2 instance’s primary private IPv4 address using NAT services. When a public IP address is assigned to an EC2 instance, the inbound traffic is directed to your EC2 instance’s private internal IP address.

If your EC2 instance is directly accessible from the Internet, when someone wants to directly reach your EC2 instance, the inbound destination is the public IP address. When the EC2 instance needs to communicate outbound across the Internet, the source address is its public IP address. Queries on the private network of the EC2 instance always use the private address of the EC2 instance. The takeaway from this example is that AWS attempts to use the private IP address, whenever possible, for network communication with an EC2 instance.

Each EC2 instance that receives a public IP address at AWS is also provided with an external DNS hostname. As a result, the external DNS hostname is resolved to the public IP address of the EC2 instance when queries are external to AWS, as shown in Figure 11-31.

## Public IPv4 Address Cheat Sheet

- You can use EIP addresses for NAT EC2 instances or custom public-facing appliances.
- You can use EIP addresses for public-facing load balancers.
- You can use EIP addresses for public-facing EC2 instances.
- You must use EIP addresses for the NAT gateway services.
- Public IP addresses are not necessary for EC2 instances.

## Inbound and Outbound Traffic Charges

It’s important to realize that you are billed differently for public traffic and private traffic at AWS. Your AWS outbound traffic costs can become extremely high if you don’t pay attention. For example, you will be charged more for public traffic sent to a public IP address traveling across the Internet than for private IP address traffic. Private traffic traveling within AWS data centers is always cheaper than traffic on a public subnet (see Figure 11-32); therefore, whenever possible, AWS uses the private network for communication.

Private traffic that stays within a single subnet incurs no additional charges, whereas private traffic that travels across multiple private subnets that are hosted by different AZs incurs an egress charge of $.01 per gigabyte. However, RDS database replication across separate availability zones is free for the synchronous replication of your data from the primary database EC2 instance to the secondary database EC2 instance. One task to carry out is a detailed cost optimization of your production workload traffic patterns, including the costs for replication across AZs, load balancer traffic, and outbound traffic flow.

All inbound communication traffic that an EC2 instance receives is free, regardless of whether it comes from inside AWS or from the public Internet. However, EC2 instance replication traffic across multiple AZs, with the exception of RDS deployments, is charged a data transfer fee.

## Bring-Your-Own IP

Bring-Your-Own IP (BYOIP) is a feature offered by AWS that enables you to bring your own public IPv4 or IPv6 addresses to AWS and use them with your AWS resources. This can be useful if you want to use a specific range of IP addresses for your resources or if you want to migrate your existing IP addresses to AWS. If you own a publicly routable public IPv4 or IPv6 address range, you can move part or all of a public IP address from your on-premises network to AWS. Each organization still owns their public IP range; however, AWS hosts and advertises the public IP address range hosted at AWS across the Internet and AWS regions for you. The public address range must be registered with your Regional Internet Registry (RIR)—for example, the American Registry for Internet Numbers (ARIN)—and must also be registered to a business or institution, not to an individual person. Bringing your own public IPv4 or IPv6 address space to AWS allows you to accomplish the following:

- Maintain your public IP address reputation.
- Avoid any changes to public IP addresses that have been whitelisted.
- Avoid changing IP addresses that legacy applications still use.
- Use a public IP address as a hot standby failover for on-premises resources.

The following are some examples of situations in which you might want to control your own public address space in the AWS cloud:

- You want to keep a recognizable public IP address but have the service assigned to that address hosted on AWS.
- You have 10,000 hard-coded lottery machines, and you want to change the hardware devices to virtual ones at AWS with your public IP addresses.
- You have 2,000 hard-coded public IP addresses within your data center, and you want to change the physical location of your data center to AWS but keep the same public IP addresses.
- You have legacy workloads—or older applications that rely on specific fixed public IP addresses—and want to move these addresses to AWS.

The specific prefix supported by BYOIP at AWS for IPv4 public addresses is /24. The specific prefix for IPv6 addresses is /48 for CIDRs that are publicly advertised, and /56 for CIDRs that are not publicly advertised.

# IPv6 Addresses

Even though IPv6 addresses are fully supported within a VPC, an IPv4 CIDR block must be created first. The allowable format for IPv6 addresses is 128 bits, with a fixed CIDR block size of /56. Amazon is in control of IPv6 addressing at AWS; you cannot select your own IPv6 CIDR range. At AWS, IPv6 addresses are globally unique addresses and can be configured to remain private or reachable across the Internet.

Amazon VPC has built-in support for address assignment via DHCP for both IPv4 and IPv6 addresses. If your EC2 instance is configured to receive an IPv6 address at launch, the address will be associated with the primary network interface (eth0). Assigned IPv6 addresses are also persistent; you can stop and start your EC2 instance, and the IPv6 addresses remain assigned. Access to the Internet using an IPv6 address can be controlled by using the egress-only Internet gateway (EOIG), route tables, and, optionally, network access controls. Here is a short summary of the steps for providing IPv6 Internet access:

