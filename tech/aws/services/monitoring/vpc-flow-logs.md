VPC Flow Logs
---

- Enable you to capture information about the IP traffic going to and from a VPC.
- Flow logs can be used to monitor, troubleshoot, and analyze the network traffic in your VPC.
- Can be `enabled at the VPC, subnet, or ENI level`, capturing traffic flowing in and out of the specified resource.
- `No charge for creating a flow log` but `charges for log data storage`.
- `store network traffic log data` in CloudWatch log groups. 
- Network traffic across a VPC, subnet, or elastic network adapter can be captured and stored in a CloudWatch log group for analysis.

Network traffic can be captured for analysis or to diagnose communication problems at the level of the elastic network interface, subnet, or entire VPC. AWS does not charge you for creating a flow log, but it will impose charges for data storage. When each flow log is created, you define the type of traffic that will be captured—either accepted traffic only, rejected traffic only, or all traffic, as shown in Figure 11-33.

Flow logs can be stored either in a CloudWatch log group or directly in an Amazon S3 bucket for storage, also shown in Figure 11-33. If VPC flow logs are stored as a CloudWatch log group, IAM roles must be created that define the permissions for the CloudWatch monitoring service to publish the flow log data to the CloudWatch log group. Once the log group has been created, you can publish multiple flow logs to the same log group.

Creating a flow log for a subnet or a VPC, each network interface present in the VPC, or subnet is then monitored. Launching additional EC2 instances into a subnet with an attached flow log results in new log streams for each new network interface and any network traffic flows.

Not all network traffic is logged in a flow log. Examples of traffic that is not logged in flow logs include AWS DNS server traffic, Windows license activation traffic, instant metadata requests, Amazon Time Sync Service traffic, reserved IP address traffic, DHCP traffic, and traffic across a PrivateLink interface.

Any AWS service that uses EC2 instances with network interfaces can take advantage of flow logs. Supporting services also include ELB, Amazon RDS, Amazon ElastiCache, Amazon Redshift, Amazon EMR, and Amazon WorkSpaces. Each of these services is hosted on an EC2 instance with network interfaces.

