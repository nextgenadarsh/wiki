Amazon S3
---

# S3 Bucket Security

- By default, only the `owner` who created an S3 bucket `has access to the objects stored in the bucket`.

Methods for controlling security for an S3 bucket:
---

## ACLs

- Used to control primary `access from other AWS accounts` for list and write objects and read and write bucket permissions, public access, and access to S3 logging information.
- Are available for purposes of `backward compatibility` and are the `weakest type of S3 security` (and therefore `not recommended`).

## IAM Policy

- You can grant access to other AWS users and groups of IAM users by using IAM permission policies in partnership with resource policies.

## S3 Bucket policy

- is a `JSON-formatted document` that defines which actions are allowed or denied on an S3 bucket and its contents.
- is `attached directly to the bucket` it is protecting, and the policy settings list who has access to the bucket and what they can do with the objects in the bucket.
- An S3 bucket policy might allow a specific IAM user to read and write objects in the bucket, while denying access to all other users. Or, the policy might allow any user to read objects in the bucket but allow only authenticated users to write objects.
- are defined using the AWS Policy Language, which provides a set of keywords and operations that you can use to specify the conditions under which a policy takes effect.
- Can also `allow access from multiple AWS accounts` to a single S3 bucket.

## Query String Authentication (Presigned Url)

- is a method to authenticate requests to an Amazon S3 bucket allowing organizations to generate a URL that can be shared with end users.
- When an end user clicks the URL, they are granted access to the specified S3 bucket and its contents.
- If you require public access to objects in an S3 bucket, it’s recommended that you create a separate AWS account specifically for hosting the S3 buckets that will have public S3 object access.

## Blocking S3 public access

- S3 Buckets always start as private, with no default public access. When the Block Public Access (Bucket Settings) setting is enabled, attempts at changing security settings to allow public access to objects in the S3 bucket are denied.
- You can block public access on an individual S3 bucket or on all S3 buckets in your AWS account by editing the public access settings for your account using the S3 console.

Choices for blocking S3 public access include the following:

**Public:** Everyone has access to list objects, write objects, and read and write permissions.

**Objects Can Be Public:** The bucket is not public; however, public access can be granted to individual objects by users with permissions.

**Buckets and Objects Not Public:** No public access is allowed to the bucket or the objects within the bucket.

![Blocking Public Access on an S3 Bucket by Default](../../images/s3-block-public-access.png)
> Fig: Blocking Public Access on an S3 Bucket by Default

# S3 Storage at Rest

## SSE-S3

- With `SSE-S3`, Amazon `S3 manages the encryption and decryption` of the data in the bucket.
- `Organizations don’t manage the encryption keys` but can access the data in the bucket without having to manage the keys.
- uses the Advanced Encryption Standard (`AES`) `algorithm` with a 256-bit key to encrypt the data in the bucket.
- The key is `automatically generated by S3` and is `regularly rotated` to ensure the security of the encrypted data.
- Note that SSE encrypts the object data but the optional tag object metadata remains unencrypted.

![SSE-S3 Encryption Process](../../images/s3-sse-s3-encryption-process.png)
> Fig: SSE-S3 Encryption Process

## SSE-KMS

- Organizations can select AWS KMS to manage their encryption keys.
- Select the default CMK or choose a CMK that was already created in AWS KMS before starting an S3 encryption process.
- `Accessing encrypted objects managed by KMS can be expensive`: If you have an exceptionally large number of encrypted objects, a large volume of decryption requests will be made to KMS.
- You can `configure SSE-KMS to significantly reduce the cost of the encryption and decryption` process.
- When an S3 Bucket Key is configured for SSE-KMS server-side encryption, a short-lived encryption key is created and stored and used to encrypt objects internally inside AWS S3 rather than utilize AWS KMS encryption processes.
- S3 Bucket Key creates unique data keys for encrypting objects in the specific S3 bucket that has enabled the S3 Bucket Key option.
- Encryption process reduces AWS KMS requests for external encryption keys and can reduce encryption costs by 99%.
- S3 Bucket Key is a worker process within the S3 bucket that enables you to perform encryption services without constant communication with KMS.

## SSE-C

- You can use `SSE with a customer-provided encryption key`.
- With each request, the encryption key is provided to AWS, and Amazon S3 manages the encryption and decryption of S3 objects by using the supplied key.
- The same encryption key that was used to encrypt the object must be provided before the object can be decrypted.
- After the encryption process is complete, the supplied encryption key is deleted from memory.
- To upload an object with an organization-provided encryption key (SSE-C), the AWS CLI, AWS SDK, or Amazon S3 REST API must be used.

![SSE-C Encryption Process](../../images/s3-sse-c-encryption-process.png)
> Fig: SSE-C Encryption Process

# Amazon S3 Object Lock Policies

- S3 buckets and S3 Glacier have data policies that can `lock objects so they cannot be deleted or changed`.
- Amazon S3 objects can be locked using a write-once/read-many (`WORM`) policy.
- Object lock policies `enable you to set rules that restrict certain actions on objects, such as deleting or overwriting` them, in order to protect objects and ensure they remain available and unaltered.
- Object lock policies are `set at the S3 bucket level` and apply to all objects in the bucket, `or set on individual objects`.
- Useful for complying with legal or regulatory requirements or protecting important or sensitive data.
- Apply a WORM policy to stop an Amazon S3 object from being overwritten, or deleted for a fixed time period, or indefinitely. - WORM Polices Options:
  - `The retention period`, which refers to a set number of days or years during which an object will remain locked, protected, and unable to be overwritten or deleted.
  - Retention modes:
    - **Governance mode:** An S3 object cannot have its lock settings overwritten and cannot itself be overwritten or deleted unless the user has unique permissions. To override governance mode retention settings, an IAM user must have the s3: BypassGovernanceRetention permission and x-amz-bypass-governance-retention: true applied.
  - **Compliance mode:** A protected object in your AWS account cannot be overwritten or deleted by anyone, including the root user, for the entire retention period.

## Legal Hold

- An object lock allows you to place a legal hold on an S3 object.- Legal hold provides the same protection as a previously discussed retention period but `does not have an expiration date`.
- Once in force, a legal hold `remains in place until it is removed`.
- An object lock `works on S3 buckets` that have `versioning already enabled`.
- Legal hold can be applied to a single S3 object.
- A legal hold can be placed and removed by any user with the s3:PutObjectLegalHold permission applied to their IAM user or group account they are a member of.
- Object lock `can only be enabled for new buckets` when they are being created.
