Designing Secure Workloads and Applications
---

# Domain 1: Design Secure Architectures

- Workload and application security at AWS refers to the `measures and controls that are implemented to protect the data and associated cloud services used to process, store, and transmit data`.

- Design and deploy subnets and route tables, security groups (SG), and network access control lists (ACLs) to protect workload infrastructure hosted on subnets in each virtual private cloud (VPC).
- Use AWS Web Application Firewall (WAF), AWS Shield Standard, and AWS Shield Advanced, to help protect workloads that are exposed to the internet.


## Securing Network Infrastructure

- **Internet connections (HTTPS/HTTP) to public-facing workloads:** An Internet gateway must be attached to the VPC hosting the workload, and the VPC’s security groups and network ACLs must be configured to allow the appropriate traffic to flow through the subnets, load balancer, and web servers.

- **AWS Direct Connect:** Establish a dedicated network connection from your on-premises data center to your VPC (Virtual Private Cloud) at AWS.

- **An AWS VPN (Virtual Private Network) connection:** Provide a secure encrypted connection between an on-premises network and VPC at AWS. VPN connections allow access to your AWS resources and workloads as if they were on your on-premises network.

- **Edge locations for accessing cached data records using Amazon CloudFront, Amazon’s content delivery network (CDN):** Edge locations are located at the edge of the AWS cloud and serve content to users more quickly and efficiently.

- **AWS Global Accelerator network:** Use Amazon’s global network of edge locations to improve the performance of Internet applications routing traffic from users to the optimal AWS endpoint.



# Domain 2: 

