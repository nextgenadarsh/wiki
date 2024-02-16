Local EC2 Instance Storage Volumes
---

- There are two main types of storage that EC2 instances can directly use:
  - Persistent EBS block storage volumes
  - Temporary block storage (also called ephemeral storage).
- An ephemeral storage volume is a hard drive (SSD/HDD) physically attached to the bare-metal server where the EC2 instance is hosted.
- The local temporary block storage volume is `shared between the hosted EC2 instances` that support ephemeral storage.
- Depending on the EC2 instance type selected, there could be one or more SSD volumes exposed as ephemeral storage devices. - Ephemeral storage volumes are `numbered from 0 to 23` and are labeled as ephemeral 0 to ephemeral 23.
- could be used to `store cached data or logs` of the hosted web application.
