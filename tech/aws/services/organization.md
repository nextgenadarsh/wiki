AWS Organizations
---

- Enables `centralized policy-based management for multiple AWS accounts` that are grouped together in a tree structure.

# AWS Organization Cheat Sheet

- A `collection of AWS accounts` organized into a hierarchy that can be managed centrally.
- Each AWS account in an organization is designated as a member account located in a container. There is no technical difference between the master account and a member account other than its location.
- Supports `consolidated billing`.
- AWS Resource Access Manager can be used to share resources within the organization tree.
- Service control policies (SCPs) can be applied to AWS accounts or OUs contained within the AWS organization controlling access to AWS resources and services.
- AWS CloudTrail can be activated across all AWS accounts in the organization and cannot be turned off by member accounts.
- An organizational unit contains one or more AWS accounts within the AWS organizational tree.
- Security tools (AWS IAM, AWS Config, AWS Control Tower) can manage the needs and requirements of the AWS accounts that are members of the same AWS organization.
- AWS Cost Explorer can be used to track costs across accounts.
