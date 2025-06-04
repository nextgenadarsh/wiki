Amazon Inspector
---

- Allows you to `test the security levels of instances` you have deployed.
- After you define an assessment target for Amazon Inspector, which is a group of tagged EC2 instances, Amazon Inspector evaluates the state of each instance by using several rule packages.
- Uses two types of rules:
  - **Network accessibility tests**
    - `Don’t` require the Inspector `agent to be installed`
  - **Host assessment rules**
    - `Require` the Inspector `agent to be installed.
- Performs security checks and assessments `against the operating systems` `and applications` hosted on Linux and Windows EC2 instances by using an optional Inspector agent installed on the operating system associated with the EC2 instance.

# Assessment Templates

- Check for any security issues on targeted EC2 instances.
- Choices for rule packages comply with industry standards.
- Include Common Vulnerabilities and Exposure (CVE) checks, Center for Internet Security (CIS) checks, operating system configuration benchmarks, and other security best practices.
- The Amazon Inspector Network Reachability rules package allows you to identify ports and services on your EC2 instances that are reachable from outside the VPC.
- Amazon Inspector gathers the current network configuration, including security groups, network access control lists, and route tables, and analyzes the accessibility of the instance.

- Amazon Inspector rules are assigned severity levels of medium and high based on the defined assessment target’s confidentiality, integrity, and availability.
- Amazon Inspector also integrates with SNS, which sends notifications when failures occur. An AWS SNS notification can, in turn, call an AWS Lambda function, which can carry out any required task; AWS Lambda can call any AWS API.
- Amazon Inspector can alert you when security problems are discovered on web and application servers, including insecure network configurations, missing patches, and potential vulnerabilities in the application’s runtime behavior.
