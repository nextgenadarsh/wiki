Authentication and Authorization
===

# Introduction to Authentication and Authorization

- Authentication is the process or action that verifies the identity of a user or process.
- Authorization is a security mechanism that determines access levels or permissions related to system resources including files, services, computer programs, data, and application features

AWS Identity and Access Management (IAM) allows you to create identities (users, groups, or roles) and control access to various AWS services through the use of policies. IAM serves as an identity provider (IdP).

## Different Planes of Control

The control plane permits access to perform operations on a particular AWS instance. AWS can control access to this plane through various AWS application programming interface (AWS API) operations. The data plane permits access to the application running on AWS. The data plane permits access to sign in to the compute instance using Secure Shell (SSH) or Remote Desktop Protocol (RDP) and to make changes to the guest operating system or to the application itself.

The control and data planes use different paths, different protocols, and different credentials; however, for several AWS services, the control and data planes are identical. Amazon DynamoDB allows you to stop and start the compute instances (control plane) and stop and start the database (data plane) using an AWS API.

## Identity and Authorization

A discussion of federation requires a review of the concept’s identity and authorization. Each of these concepts asks and answers two different questions. Identity asks and answers “Who are you?”; and authorization asks and answers “What can you do?”

AWS establishes authorization by user-executed APIs. AWS controls operations and tasks through APIs. Policies are JavaScript Object Notation (JSON) documents that show attribute-value pairs. Every policy document requires a minimum of three attribute-value pairs: effect, action, and resource.

Effect has the API value of either ALLOW or DENY. The entity (whether a user, group, or role) is either granted the permission to execute that API or denied the permission to execute that API.

Action determines whether the API is allowed or denied. Actions can be determined by an individual API, a grouping of APIs for the same service using a wildcard (for example, S3:* includes all Amazon Simple Storage Service (Amazon S3 APIs), or APIs for different services.

Resource determines where the API is being allowed or denied. For example, with Amazon S3, you can allow the execution of an API in a particular bucket, object, or particular group of objects (using the wildcard *).

## Federation Defined

A federation consists of two components: identity provider and identity consumer.

- An identity provider stores identities, provides a mechanism for authentication, and provides a course level of authorization. 
- An identity consumer stores a reference to the identity, providing authorization at a greater granularity than the identity provider.

## Federation with AWS

- allows you to use AWS as an IdP to gain access to both AWS and non-AWS resources. Amazon Cognito is an AWS service that acts as an IdP
- you can use non-AWS resources like Security Assertion Markup Language (SAML) 2.0, OpenID Connect (OIDC), or Microsoft Active Directory as the IdP to facilitate single sign-on (SSO).

## Cross-Account Access

When you need to access resources across multiple AWS accounts, cross-account access enables you to do so by using only one set of credentials

## Security Assertion Markup Language

provides federation between an IdP and a service provider (SP) when you are in an AWS account and a trust relationship has been established between the IdP and the SP. The IdP and the SP exchange metadata in an .xml file that contains both the certificates and attributes that form the basis of the trust relationship between the IdP and the SP.

## OpenID Connect

OpenID Connect (OIDC) is the successor to SAML. OIDC is easier to configure than SAML and uses tokens rather than assertions to provide access. Most use cases for OIDC involve external versus internal users.

With OIDC, OpenID provider (OP) uses a relying party (RP) trust to track the service provider. OP and RP exchange metadata by focusing on the OP providing information to the RP about the location of its endpoints. The RP must register with the OP and then receive a client ID and a client secret. This exchange establishes a trust relationship between the OP and the RP.

## Microsoft Active Directory

You use the Active Directory forest trusts to establish trust between an Active Directory domain controller and AWS Directory Service for Microsoft Active Directory (AWS Managed Microsoft AD). For Microsoft Active Directory, the domain controller is on-premises or in the AWS Cloud.

## AWS Single Sign-On

an AWS service that manages SSO access. AWS SSO allows users to sign in to a user portal with their existing corporate credentials and access both AWS accounts and business accounts. You can have multiple permission sets, allowing for greater granularity and control over access.

## AWS Security Token Service

creates temporary security credentials and provides trusted users with those temporary security credentials. The trusted users then access AWS resources with those credentials

## Amazon Cognito

a service that allows you to manage sign-in and permissions for mobile and web applications through two services: Amazon Cognito Sync store and Amazon Cognito Sync.

With Amazon Cognito Sync store, you can authenticate users using third-party social identity providers or create your own identity store. With Amazon Cognito Sync, you can synchronize identities across multiple devices and the web.

## AWS Managed AD

![AWS Directory Service chart](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781119508199/files/images/c10f002.jpg)

