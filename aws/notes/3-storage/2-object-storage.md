# Object Storage

- Object is a piece of data like a document, image, or video that is stored with some metadata in a flat structure.

## Amazon Simple Storage Service (S3)

- Provides highly scalable, reliable, and low-latency data storage infrastructure at low cost.
- Virtually no size limit

### Buckets

- Container for objects stored in Amazon S3.

#### Limitations

- Do not use buckets as folders, because there is a `maximum limit of 100 buckets per account`.
- You cannot create a bucket within another bucket.
- A bucket is `owned by the AWS account` that created it, and bucket `ownership is not transferable`.
- A bucket must be `empty before you can delete it`.
- After a bucket is deleted, that name becomes available to reuse, but the name might not be available for you to reuse for various reasons.

#### Universal Namespace

- A bucket name must be `unique across AWS` ie. across all existing bucket names in Amazon S3 across all of AWS.
- Comply with Domain Name System (DNS) naming conventions when choosing a bucket name. DNS-compliant bucket name rules:
  - Names must be between `3 to 63 characters long`.
  - Must contain lowercase letters, numbers, and hyphens.
  - Must consist of a series of one or more labels, with adjacent labels separated by a single period (.)
  - Label must start and end with a lowercase letter or number.
  - Must not be formatted like IP addresses.
  - Recommendation is that do not use periods (.) in bucket names.
  - Valid names: `example.bucket.names`

#### Versioning

- Use versioning to preserve, retrieve, and restore every version of every object stored in your Amazon S3 bucket, including recovering deleted objects.
- Versioning is `turned off by default`.
- S3 versioning tracks the changes over time.
- AWS places a delete marker on top of the deleted object.
- It is easy to set up a lifecycle policy to control the amount of data that’s being retained when you use versioning on a bucket.
- Once you enable versioning on a bucket, it can never return to an un-versioned state. You can, however, suspend versioning on that bucket.

#### Region

- Amazon S3 creates buckets in a region that you specify.

#### Objects

- An object can only be between `1 byte to 5 TB` in size.
- The largest object that can be uploaded in a single PUT is 5 GB.
- S3 URLs can be thought of as a basic data map between “bucket + key + version” and the web service endpoint.

##### Object Facets

- `Key`: name that you assign to an object
- `Version ID`
- `Value`
- `Metadata`
- `Subresources`
- `Access Control Information`


##### Object Tagging

- Enables you to categorize storage.
- You can associate 10 tags with an object with unique tag key.
- A tag key can be up to 128 Unicode characters in length, and tag values can be up to 256 Unicode characters in length.

#### Cross-Origin Resource Sharing

- Defines a way for client web applications that are loaded in one domain to interact with resources in a different domain.

### S3 Standard

- Offers `eventual consistency` for overwrite PUTs and DELETEs in all regions, and updates to a single key are atomic.

#### Presigned URLs

- A way to grant access to an object
- Allow users to upload or download objects without granting them direct access
- Cannot be generated within the AWS Management Console

#### Encryption

- Use Server Side Encryption (SSE) to encrypt the object as they are written to disk and decrypt when accessing object
- Use `client-side encryption` to encrypt the objects before uploading and then decrypt them after downloading. 

#### Envelope Encryption Concepts

- Provides a balance between performance and security.
- Key-encrypting keys used to encrypt data keys are stored and managed separately from the data and the data keys.

#### Server-Side Encryption (SSE)

- SSE-S3 (Amazon S3 managed keys)
  - Set an API flag or check a box in the AWS Management Console to have data encrypted
  - Offered at `no additional cost`
- SSE-C (Customer-provided keys)
  - Encryption key is used to encrypt/decrypt the data
  - Offered at `no additional cost`
- SSE-KMS (AWS KMS managed encryption keys)
  - Encrypt your data in Amazon S3 by defining an AWS KMS master key within your account to encrypt the unique object key (referred to as a data key)
  - Incur an `additional charge`

#### Client-Side Encryption

- Encrypting your data before sending
- Client-Side Master Key
  - Use a client-side master key of your own
  - Client-side master key that you provide can be either a symmetric key or a public/private key pair.
- AWS KMS-Managed Customer Master Key (CMK)
  - Use an AWS KMS managed customer master key (CMK)
  - Used for data at rest instead of data in transit

#### Access Control

- By default, all Amazon S3 resources—buckets, objects, and related sub-resources are private.
- Using Bucket Policies and User Policies
  - Bucket policy
    - Attached only to Amazon S3 buckets
    - Specifies what actions are allowed or denied for whichever principals on the bucket
  - Attached to IAM users
- Managing Access with Access Control Lists
  - Resource-based access policies
  - Can grant permissions only to `other accounts`
  - Use to manage access to your buckets and objects, including granting basic read/write permissions to other accounts
  - Cannot grant conditional permissions, nor can you explicitly deny permissions

#### Hosting a Static Website

##### Steps

- Register your domain
- Create S3 bucket and upload your static website content
- Point your domain to S3 bucket  

#### Defense in Depth—Amazon S3 Security

- Data must be `encrypted at rest` and `during transit`.
- Data must be accessible only by a `limited set of public IP addresses`.
- Data must `not be publicly accessible` directly from an Amazon S3 URL.
- A `domain name is required` to consume the content.

#### MFA Delete

- A way to control deletes on your objects.
- `Requires a unique code` from a token or an authentication device

#### Cross-Region Replication

- `Bucket-level configuration` that enables `automatic`, asynchronous copying of objects across buckets in `different AWS Regions`
- Source and Destination buckets can be owned by different accounts
- Can replicate objects from a source bucket to `only one destination` bucket.
- Requirements for CRR:
  - `Versioning is enabled` for both the `source and destination` buckets.
  - Source and destination buckets must be in `different Regions`.
  - Amazon S3 must be granted `appropriate permissions` to replicate files.

#### VPC Endpoints

- Enables you to `connect your VPC privately` to Amazon S3 without requiring an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.
- Use bucket policy to indicate which VPCs and which VPC endpoints have access to your Amazon S3 buckets.

#### Data Lake

- Allows you to `store massive amounts of data` in a `central location` for consumption by multiple applications.
- S3 is a common component of a data lake solution on the cloud

#### Performance

- Automatically scales to thousands of requests per second per prefix

#### Consideration for Workloads

- Mixed requests
  - Appropriate key names for your objects ensures better performance
- GET-intensive
  - Use Amazon CloudFront

#### Tips for Object Key Naming

- Consider using a three- or four-character hash in your key names.
- A random hash should come before patterns, such as dates and sequential IDs.
- Using a naming hash can improve the performance of heavy-traffic applications. 

#### Amazon S3 Transfer Acceleration

- Optimizes throughput when transferring larger objects across larger geographic distances.
- Uses Amazon CloudFront edge locations

#### Multipart Uploads

- API enables you to upload large objects in parts to speed up your upload by doing so in parallel.
- Can be used for objects ranging from 5 MB to 5 TB in size.

#### Range GETs

- Similar to multipart uploads, but in reverse

#### Amazon CloudFront

#### TCP Window Scaling

- Improve network throughput performance between your operating system, application layer, and Amazon S3

#### Pricing

- You pay for the following:
  - Storage that you use
  - API calls that you make (PUT, COPY, POST, LIST, GET)
  - Data transfer `out of S3`

#### Object Lifecycle Management

- Used to manage your objects so that they are stored cost effectively
- Transition actions
  - Define when objects transition to another storage class. 
- Expiration actions
  - Define when objects expire. Amazon S3 deletes expired objects on your behalf.



### S3 Glacier

- Retrieval times run from a few minutes to several hours.
- Need CLI/SDK to perform any operation other than Create/Delete vault.
- Does not support any additional metadata for the archives
- Cannot assign a key name, like "filename.txt", to the archives you upload.
- Archives
  - Any object, such as a photo, video, or document that you store in a vault.
  - Base unit of storage in Amazon S3 Glacier.
- Vaults
  - Containers to store archives.
  - Up to 1,000 vaults per AWS account.
- Vault Lock
  - Allows you to deploy and enforce compliance controls easily on individual Amazon S3 Glacier vaults via a lockable policy.
  - After 24 hours, the Vault Lock is permanent, and you will not be able to change it.
- Encryption
  - All data in Amazon S3 Glacier will be encrypted on the server side.
- Restoring Objects from Amazon S3 Glacier
  - Not immediately accessible and cannot be retrieved via copy/paste
  - S3 Glacier charges a retrieval fee for retrieving objects.
- Archive Retrieval Options

  | Retrieval Option  | Retrieval Time  | Note
  | --                | --              | --
  | Expedited         | 1-5 minutes
  | On-Demand         |                 | Processed `immediately mostly`. May fail sometimes.
  | Provisioned       |                 | Processed `immediately guaranteed `.
  | Standard          | 3-5 hours       | 
  | Bulk              | 5-12 hours      | `Lowest-cost` option

### Storage Classes Comparison

|            | Standard       | Reduced redundancy | Standard IA   | One-Zone IA | Glacier
| --         | --             | --      | --            | --          | --
| Durability | 99.999999999%* | 99.99%  |               |             |
| Availability | 99.99%       | 99.99%  | 99.9%         | 99.9%       | NA
| SLAs        | 99.9%         |         | 99%           |             | NA
| AZ          | >= 3          |         |               | 1           | >= 3
| Min Capacity Charge/Object | NA | 128 KB*   |         | NA
| Min Storage Duration Charge | NA | 30 days  |         | 90 days
| Retrieval fee | NA | Per GB retrieved | | Supports multiple retrieval tiers
| First byte latency | milliseconds |   |           | Minutes or hours
| Storage Type  | Object
| Lifecycle transitions | Yes
| Use cases | Cloud App, Website, CDN, Big Data Analytics | Thumbnails, Transcoded media | Long term, Backup, Disaster recovery | 

