S3 Glacier Deep Archive
---

- You are charged about $1 per terabyte per month for storage.
- You can `move on-premises magnetic tape` libraries into S3 Glacier Deep Archive and save money.
- Objects archived have a `minimum storage requirement of 180 days`.
- Retrieval processes:
  - Free standard retrieval delivers your data within `12 hours`.
  - Bulk retrieval returns your data within `48 hours`.
  - `Expedited` data retrieval is `not supported`.

<h2 style="background-color:lightgreen">Amazon S3 Glacier Cheat Sheet</h2>

- Data in Amazon S3 Glacier is resilient even if one AZ is unavailable.
- Archived objects are visible upon retrieval request through an Amazon S3 temporary storage location and not directly through Amazon S3 Glacier.
- Amazon S3 Glacier automatically encrypts all stored data at rest using AES 256-bit encryption.
- The Amazon S3 PUT API allows direct uploads to Amazon S3 Glacier.
- Amazon Glacier Deep Archive is lower cost than Amazon S3 Glacier but has longer retrieval times.
- Once an archive has been uploaded, it cannot be modified.
- Amazon Glacier Instant Retrievals can be expedited within milliseconds.
- Amazon Glacier Flexible Retrieval bulk retrievals are free of charge once a year.
- Amazon Glacier Flexible Retrieval bulk retrieval times are typically between 5 and 12 hours.
