CloudTrail
---

- `Records all AWS API calls` carried out `within each AWS account` related to actions across your AWS infrastructure.
- Also `logs all account authentications and event history` for your AWS account, including actions taken through the AWS Management Console, AWS SDKs, the AWS CLI command prompt, and other AWS service activity.
- `Enabled by default` for all AWS accounts, and events in the default CloudTrail trail are available for the `last 90 days free of charge`.
- Organizations can also create custom trails storing all activity indefinitely in an Amazon S3 bucket or Amazon CloudWatch log group.
- CloudWatch events are logged in CloudTrail within 15 minutes of each API request.
- A `regional service` with a `global reporting reach` because the default trail automatically creates separate trails in each active AWS region.

<h2 style="background-color:lightgreen"># CloudTrail Cheat Sheet</h2>

- Records all activity on an AWS account, including API calls and authentications.
- Custom AWS CloudWatch trails can deliver events to an S3 bucket or a CloudWatch log group.
- CloudTrail events can be used for `auditing AWS account activity`.
- CloudTrail reports activity for each AWS account.
- CloudTrail can be integrated with an AWS Organization.
- CloudTrail tracks both data and management events.
- CloudTrail records can be encrypted using S3 server-side encryption.
