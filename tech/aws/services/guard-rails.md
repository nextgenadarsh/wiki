Guardrails
---

- Used to provide ongoing governance of the AWS environment by preventing deployment of resources that don’t follow prescribed policies.
- Prevents deployment of resources that don’t match your rules.
- Can also be detective in nature by continually monitoring the resources that are deployed for nonconformance.
- Deployed using an AWS CloudFormation script that establishes the configuration baseline.
- SCPs create preventive guardrails that prevent unwanted infrastructure changes.
- Detective guardrails are created and enforced using AWS Config rules.
- There are also mandatory and optional guardrails that can be leveraged.
