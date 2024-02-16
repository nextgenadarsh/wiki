Amazon Guard Duty
---

- A `threat detection service` that continuously `monitors and protects` your AWS account, `EC2` instances, `container` applications Amazon `Aurora` databases, and data stored in `S3` buckets.
- Uses `machine learning and anomaly detection` to identify potentially malicious activity in your AWS environment, such as `unauthorized access` or `unusual behavior`.
- Provides `alerts for any suspicious activity` it detects, allowing organizations to take appropriate action to protect AWS resources.
- Also supports AWS Organizations.
- Uses CloudTrail events, VPC flow logs, Amazon Elastic Kubernetes Service audit logs, and DNS query logs.
- Monitors:
  - Reconnaissance: unusual API activity, failed database login attempts
  - Global events
  - Amazon `EC2` instance compromise
  - Amazon `EKS` Protection
  - Amazon `RDS` Protection
  - Amazon `S3` Bucket compromise
  - Amazon `Route 53` DNS logs

<h2 style="background-color:lightgreen"># Amazon GuardDuty Cheat Sheet</h2>

- Can also be deployed with AWS Organizations (AWS recommended deployment).
- When Amazon GuardDuty Malware Protection finds issues with EBS volumes, it creates replica snapshots of the affected EBS volumes.
- Can also be `integrated with` AWS `Security Hub` and Amazon `Detective Services` to perform automated actions.
