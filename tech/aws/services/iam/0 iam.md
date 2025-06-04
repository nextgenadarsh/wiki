Identity & Access Management (IAM)
---

# Terms

## Root User

- Tasks carried out only by root user:
  - Changing your AWS support plan
  - Enabling billing for the account or changing your payment options
  - Creating a CloudFront key pair
  - Enabling MFA on an S3 bucket in your AWS account
  - Requesting permission to perform a penetration test

## User

- An IAM security principal
- User ARN: `arn:aws:iam::account ID:user/mark`

## Group

- Collection of IAM users
- Can’t be nested

## Security Policy

- A `set of rules` that define the actions that each AWS entity can perform on specific AWS resources; `who is allowed to do what`.
- Define what actions administrators (users and groups) and AWS cloud services can and can’t carry out.
- Each IAM policy can define a single permission statement or multiple permission statements.

### Identity-Based Policy

- Contains permissions for specific actions an IAM user, group, or role can carry out.

### Resource-based Policy

- Assigned to protect storage resources such as S3 buckets
- Services that support resource-based policies:
  - S3 Glacier vaults
  - Simple Notification Service (SNS)
  - Simple Queue Service (SQS)
  - Lambda functions

### Inline Policy

- Helps you maintain a `strict one-to-one relationship` between the attached policy and the entity the policy is attached to.

## Role

- An IAM identity with specific permissions that define what the identity can and can’t do at AWS.
- Provide `temporary access` to AWS resources once a role is associated with the identity.
