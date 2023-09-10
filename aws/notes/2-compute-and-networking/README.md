Elastic Compute Cloud (EC2)
=============

- #`vCPUs` #`AZ` #`resizable`
- You control `operating system`, `softwares`. `Bare-metal` access also supported.

# EC2 Instance Families

| EC2 Family      | Attributes      | Usage
| --              | --              | --
| General Purpose | `Balance` of CPU,RAM,etc | Web application
| `Compute` Optimized | High `CPU`    | High-perf web server, scientific modelling, video encoding
| `Memory` Optimized | Large `RAM`      | In-Memory DB/Cache
| `Storage` Optimized | Large Storage, I/O | Data Warehouse, Analytics, BigData
| `Accelerated` computing | Dedicated `GPU/FPGA` | 3D rendering, DeepLearning, Genomics, RealTime Video Processing

# EBS Volume

- 1 EBS : 1 Instance
- EBS volume size can be increased while instance running.
- EBS can be detached and attached in same AZ
- Point-in-time snapshot: `durability`, `Multi-AZ auto-replication`.
- Charged even if instance is terminated

# Instance Store

- Local storage with high read-write performance
- Provided only for a few EC2 instance types
- Usage: High-Performance temporary storage

# Amazon Machine Image (AMI)

- Template for the OS and applications on the root volume
- Supports block device mapping that can specify additional volumes to mount
- AMIs are `region based`.
- Define `launch permission` for private AMIs to control which AWS accounts can use it.

# Elastic Network Interface

- 1 Instance : 1 ENI associated with a subnet
- Private IP for intra-VPC and Public IP for internet communication
- Additional ENI can be attached to the instance. Max ENI number depends on instance type. It does not affect the bandwidth.

# Accessing Instances

- Linux - SSH, Windows - RDP
- Default user: Linux - ec2-user, Ubuntu - ubuntu, Windows - Administrator

## EC2 Key Pair

- Regional
- Used for login using SSH.
- Composed of public and private keys
- EC2 instance has public key, user stores private key securely
- For windows, the password is encrypted with public key. Use private key to decrypt password.

## Customization using `User Data`

- Commands supplied to user data execute only at first boot of the instance
- Example
  ```shell
  #!/bin/bash
  yum update -y
  yum install httpd -y
  systemctl start httpd
  systemctl enable httpd
  ```

## Instance Metadata

- Anyone can make HTTP call to instance metadata service exposed on special IP address, 169.254.169.254 to get instance metadata
- `curl 169.254.169.254/latest/meta-data/`
- Also exposes the user data used for bootstrap

## Assigning AWS API Credentials

- IAM role can be assigned to instance using `instance profile (container for IAM role)`.
- 1 Instance Profile : Many Instance
- Instance profile can be attached/detached while instance is running.
- AWS uses STS to generate short-term credentials for instance.

# Instance Lifecycle

- Pending
- Running
  - Charged
- Stopping
- Stopped
- Shutting-down
- Terminated

# Monitoring Instance

- EC2 performs automated status checks of the software/hardware `of host machine` every minute and `stores it in CloudWatch``
- For each instance, AWS collects metrics for CPU, disk reads/writes, network utilization and stores it in CloudWatch.
- `CloudWatch agent` can be installed on instance to generate logs for memory utilization, application etc.
- You can automate actions based on metric through `CloudWatch Alarms`.

# Network Customization

## Virtual Private Cloud (VPC)

- Provides logically isolated networks within your AWS account.
- Spans across AZ inside Region.

## Connecting to Other Networks

Instances within an Amazon VPC cannot communicate with the internet or other networks until you explicitly create connections.

### Amazon VPC Connection Types

| Connect Type  | Description 
| --            | --
| Internet Gateway (IG) | `Outbound` and `Inbound` requests to the `Internet` from VPC.
| Egress Only IG | `IPv6`. `Outbound` traffic and but `blocks inbound` connection.
| Virtual Private Gateway (VPG) | Corporate network connection by using `VPN` connection or through `Direct Connect` (DX)
| VPC Endpoints | VPC to AWS services or 3rd-party SaaS services connection without traversing an internet gateway
| VPC Peering | Private traffic from `VPC to VPC`. Peer relationship.
| Transit Gateway | Centrally manage connectivity between many VPCs and an on-premises using a single gateway

## IP Addresses

- Private IP Address
  - Unique within a VPC
  - Inter/Intra VPC
- Public IP Address
  - Reachable from Internet
  - AWS manages the association b/w instance and IP
- Elastic IP Address
  - Customer manage the association b/w instance and IP
- IPv6 Address
  - Supports `dual-stack mode` meaning instance can communicate over IPv4 and IPv6 independently

## Subnets

- 1 VPC : Many Subnets
- Associated with specific AZ
- VPC reserves first 4 and last IP of the CIDR block of subnet
- `Public subnet` allows the instance inside it to be reachable from internet
  - Contains web servers etc
- `Private subnet` restricts the access of its instance from internet
  - Contains RDS, ElastiCache, DB Server etc

## Route Tables

- `Local Route` allows inter-subnet traffic inside VPC
- `Main Route Table` contains local route by default
- Route table rules are evaluated in order of specificity.
- Example route table

  | Destination   | Target
  | --            | --
  | 10.0.0.0/16   | `local`
  | 0.0.0.0/0     | internet-gateway

# Security Group

- Protects the traffic entering and existing ENI
- `Stateful` firewall for EC2 instance
- Includes a `default outbound rule` that `allows all outbound requests` on all protocols and ports to all destinations
- Only support rules to `allow traffic`
- Multiple security groups combine in most `permissive way`
- Example rule for Inbound

  | Protocol    | Port    | Source
  | --          | --      | --
  | TCP         | 80      | 0.0.0.0/0
  | TCP         | 443     | 0.0.0.0/0
  | TCP         | 22      | 10.10.0.6/32

- Example rule for Outbound

  | Protocol    | Port    | Destination
  | --          | --      | --
  | TCP         | All      | 0.0.0.0/0

# Network Access Control List (NACL)

- `Stateless` firewall
- Control inbound/outbound traffic for subnet
- Consists of `inbound and outbound` rules can be associated to `multiple subnets`
- Supports rule to `allow/deny` traffic
- Rules are evaluated from largest to lowest number
- Default NACL associated with VPC allows all inbound/outbound traffic by default
- Default NACL Inboud Rules

  | Rule Number | Type  | Protocol  | Port Range  | Source    | Allow/Deny
  | --          | --    | --        | --          | --        | --
  | 100         | All   | All       | All         | 0.0.0.0/0 | Allow
  | *           | All   | All       | All         | 0.0.0.0/0 | Deny

- Default NACL Outbound Rules

  | Rule Number | Type  | Protocol  | Port Range  | Source    | Allow/Deny
  | --          | --    | --        | --          | --        | --
  | 100         | All   | All       | All         | 0.0.0.0/0 | Allow
  | *           | All   | All       | All         | 0.0.0.0/0 | Deny

# Security Group vs Network ACL (NACL)

| Feature     | Security Group    | NACL
| --          | --                | --
| Applies to  | EC2, ENI          | Subnet
| Firewall Type | Stateful        | Stateless
| Rules       | Only Allow        | Allow or Deny traffic

# Network Address Translation (NAT)

- Allows for `instances` in a `private subnet` to make `outbound requests` to the `internet`
- Use an Amazon EC2 instance configured to perform NAT or a NAT gateway
- Place `NAT instance` or `NAT gateway` in a correctly configured public subnet to forward traffic to the internet
- Update route table to direct internet traffic to NAT gateway
- Using an Amazon EC2 instance for NAT instead of a NAT gateway requires you to disable the source/destination check setting for the NAT instance.

# Dynamic Host Configuration Protocol (DHCP) Option Sets

- Provides a standard for passing configuration information to hosts on a TCP/IP network.

# Monitoring Amazon VPC Network Traffic

- `VPC Flow Logs` enable you to monitor the network flows within VPC
- You can enable VPC Flow Logs on VPC/Subnet/ENI

# Managing Your Resources

## Shared Responsibility Security Model

- AWS `Systems Manager` to `automate the patching` of instances on your behalf.

## Developer Tools

### Cloud9 IDE

- Allows you to create developer environment
- A web interface for editing code, debugging, and running commands
