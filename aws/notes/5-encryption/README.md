Encryption on AWS
===========

# AWS Key Management Service (KMS)

- a managed AWS service that makes it easy to create and manage encryption keys to encrypt your data across a wide range of AWS services and in your applications
- Uses hardware security module (HSM), to protect your master keys
- Uses an Advanced Encryption Standard (AES) in 256-bit mode to encrypt and secure your data.
- AWS KMS offers the following features:
  - Centralized key management
  - Integration with other AWS services
  - Audit capabilities and high availability
  - Custom key store
  - Compliance

## AWS CloudHSM

- Offers third-party, validated FIPS 140-2, level-three hardware security modules in the AWS Cloud
- Use CloudHSM to support encryption for your application while running in your own Amazon Virtual Private Cloud (Amazon VPC)
- Provides both asymmetric and symmetric encryption

## Controlling the Access Keys

- Managing the security of encryption keys is often performed using a key management infrastructure (KMI)
- A common way to protect keys in a KMI is to use a hardware security module
![Encryption options in AWS](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c05f002.jpg)

### Option 1: You Control the Encryption Method and the Entire KMI

- You use your own KMI to generate, store, and manage access to keys in addition to controlling all the encryption methods in your applications. 
- You are responsible for the proper storage, management, and use of keys to ensure the confidentiality, integrity, and availability of your data

#### Amazon Simple Storage Service

![Amazon S3 client-side encryption](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c05f003.jpg)

#### Amazon Elastic Block Store

![Encryption in Amazon EBS using SafeNet ProtectV or Trend Micro SecureCloud](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c05f004.jpg)

##### System-level or block-level encryption

##### File-system encryption

#### AWS Storage Gateway

You can encrypt source data on the disk volumes by using any of the file encryption methods described previously, such as Bouncy Castle or OpenSSL, before it is written to the disk. To encrypt all the data on the disk volume, you can also use a block-level encryption tool, such as BitLocker or dm-crypt/LUKS, on the iSCSI endpoint exposed by Storage Gateway.

#### Amazon Relational Database Service

you can encrypt database fields in your application selectively by using any of the standard encryption libraries mentioned previously, such as Bouncy Castle and OpenSSL, before the data passes to your Amazon RDS instance.

### Option 2: You Control the Encryption Method, AWS Provides the KMI Storage Component, and You Provide the KMI Management Layer

- Similar to option 1 but the keys are stored in an AWS CloudHSM appliance rather than in a key storage system that you manage on-premises
- The CloudHSM appliance is a FIPS 140-2, level 3 HSM that has both physical and logical tamper detection and response mechanisms that trigger zeroization of the appliance. Zeroization erases the HSM’s volatile memory where any decrypted keys were stored. Zeroization destroys the key that encrypts stored objects, effectively causing all keys on the HSM to be inaccessible and unrecoverable.

#### CloudHSM

You can use an HSM to generate and store key material and perform encryption and decryption operations. However, an HSM does not perform any key lifecycle management functions (such as access control policy, key rotation). This means you might need a compatible KMI, in addition to the CloudHSM appliance, before deploying your application. You can deploy the KMI either on-premises or within Amazon EC2. To help protect data and encryption keys, the KMI can communicate to the CloudHSM instance securely over SSL.

#### Amazon Virtual Private Cloud

![Deploying AWS CloudHSM in an Amazon VPC](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c05f005.jpg)

### Option 3: AWS Controls the Encryption Method and the Entire KMI

- AWS provides server-side encryption of your data, transparently managing the encryption method and keys.

#### AWS Key Management Service

- A managed encryption service that lets you provision and use keys to encrypt your data in AWS services and your applications. Master keys in AWS KMS are used in a similar way to how master keys in an HSM are used. Master keys are designed never to be exported from the service. You can send data to the service to be encrypted or decrypted using a specific master key under your account. This design gives you centralized control over who can access your master keys to encrypt and decrypt data, and it gives you the ability to audit this access.
- AWS KMS and other services that encrypt your data directly use a method called `envelope encryption` to balance performance and security.
![Flow of envelope encryption](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c05f006.jpg)

#### Amazon S3

##### Server-side encryption

##### Server-side encryption using customer-provided keys

##### Server-side encryption using AWS KMS

#### Amazon EBS

#### Amazon EMR

#### Amazon Redshift

##### 256-bit AES keys

##### CloudHSM cluster master key

##### AWS KMS cluster master key

