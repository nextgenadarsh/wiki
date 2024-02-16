Storage Service Characteristics
---

Storage   | Durability  | Replication
--  | --  | --  
Amazon EBS  | Multiple storage volumes, snapshots stored in Amazon S3 | Replicated within each AZ across multiple servers
Amazon FSx  | Multiple storage volumes, automatic backup to Amazon S3 | Single or Multi-AZ deployments
Amazon EFS  | Multiple storage volumes, automatic backup to Amazon S3 | Single or Multi-AZ deployments
Amazon S3 Standard  | Eleven 9s durability  | Across three AZs or more depending on AWS Region
Amazon S3 One Zone  | Eleven 9s durability  | Single availability zone
Amazon S3 Glacier Deep Archive  | Eleven 9s durability  | Across three AZs
Amazon DynamoDB | SSD volumes on multiple servers | Across three AZs, or multiple AWS regions
Amazon RDS  | EBS volumes | Across one, two, or three AZs
Amazon Aurora | SSD volumes cluster shared storage  | Across three AZs, or multiple AWS regions
AWS Backup  | Eleven 9s availability  | Across three AZs

