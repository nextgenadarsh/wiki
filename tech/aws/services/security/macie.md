Amazon Macie
---

- Uses `machine learning` to automatically discover, classify, and `protect sensitive data stored in S3 buckets`.
- Helps you secure your data and prevent `unauthorized access` or accidental `data leaks`.

<h2 style="background-color:lightgreen"># Amazon Macie Cheat Sheet</h2>

- AWS Organizations uses multiple Amazon Macie accounts: an Administrator account that manages the Amazon Macie accounts for the organization and member accounts.
- Sensitive data can be identified using a custom data identifier or keyword.
- Can publish sensitive data policy findings automatically to Amazon `EventBridge as events`.
- A policy finding provides a detailed report of a potential policy violation (for example, unexpected access to S3 bucket), including a severity rating, detailed information, and when the issue was found.
- Publishes near-real-time logging data to CloudWatch logs.
- Can `analyze encrypted objects` with the exception of objects encrypted with customer-provided keys (SSE-C).
