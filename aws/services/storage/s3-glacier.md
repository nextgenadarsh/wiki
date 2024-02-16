Amazon S3 Glacier
---

- offers the `lowest cost` of any AWS storage services.
- costs on average $0.004 per gigabyte per month, and S3 Glacier Deep Archive costs just $0.00099 per gigabyte per month.
- Customers `don’t require regular access` to the content stored in S3 Glacier vaults and archives.
- Minimum storage time is `90 days`; accessing the S3 Glacier content sooner results in a financial penalty.
- `storage pricing` is based on `monthly storage capacity` and the `total number of lifecycle transition` requests for moving data into S3 Glacier.
- Objects archived into S3 Glacier must remain a minimum of 90 days, or additional charges apply.
- S3 Glacier has the same eleven 9s durability as S3 Standard storage. 
- S3 Glacier data is `stored in vaults and archives`, set up through S3 management console or using the AWS CLI.
- S3 Glacier `automatically encrypts all stored objects`.
- Content can be delivered to S3 Glacier by using the following methods:
  - Amazon S3 Lifecycle or Intelligent-Tiering rules
  - CLI commands
  - Direct use of the REST API or AWS SDK
  - AWS Storage Gateway: Tape Gateway, which integrates with S3 Glacier
  - AWS Snowball, AWS Snowcone, and AWS Snowmobile devices, which can directly migrate data records into S3 storage
  - A direct PUT stores objects directly in S3 Glacier using the S3 API
  - Cross-Region Replication or Single-Region Replication can replicate objects into S3 Glacier storage

# Vaults and Archives

- Amazon S3 Glacier archives can be from `1 byte up to 40 TiB`; archives up to 4 GiB can be uploaded in a single operation.
- Archives from 100 MiB up to 40 TiB use the `multipart upload API` and are synchronously uploaded and stored in an Amazon S3 Glacier vault stored in your chosen AWS region.
- Each AWS customer can have up to 1,000 vaults per region.

# S3 Glacier Retrieval Policies

- To retrieve objects from S3 Glacier, create `an archive retrieval job`.
- The archive retrieval job is a separate temporary copy of your data placed in either Amazon S3 Reduced Redundancy Storage or Amazon Standard-IA storage, leaving the actual archived data in its original location in Amazon S3 Glacier.
- Temporary archived data is accessed using an Amazon S3 GET request.
- To retrieve an archive from S3 Glacier, use the AWS CLI to get the ID of the archive to retrieve. Next, initiate a job requesting Amazon S3 to prepare the archive request.

## Retrieval Options

### Expedited

- `Retrieval is within 1 to 5 minutes` for archives less than 250 MiB.
- Provisioned capacity can be purchased to ensure that expedited retrieval requests under all circumstances will be carried out.

### Standard

- Retrieve any archive within several hours, typically 3 to 5 hours. This is the default option when retrieval options are not specified.

### Bulk

- Retrieve any archive within 5 to 12 hours. Bulk retrievals are the lowest-cost S3 Glacier retrieval option.

