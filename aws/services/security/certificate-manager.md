AWS Certificate Manager
---

- allows you to `provision, manage, and deploy public and private SSL/TLS certificates` that can be used with your AWS services and AWS-hosted websites and applications.
- Certificates can also be deployed on ELB load balancers, CloudFront distributions, Elastic Beanstalk, and APIs hosted on Amazon API Gateway.
- `No additional charge for provisioning public or private SSL/TLS certificates for use with AWS services`.
- Organizations will `pay a fee for creating and operating a private certificate authority (CA)` `and for the private certificates that are issued by the private CA` that is used by your internally hosted resources, such as application servers or appliances.

# Supported Certificate Types:

## Public certificates

- ELB port `443` traffic, CloudFront distributions, and public-facing APIs hosted by Amazon API Gateway all use public certificates.
- Request a public certificate for a domain name for your site. AWS Certificate Manager validates that you own or control the domain name in your certificate request. Validation options include DNS validation and email validation.

## Private certificates

- Delegated private certificates are managed by an AWS Certificate Manager–hosted private CA, which can automatically renew and deploy certificates for private-facing Amazon ELB and Amazon API Gateway deployments.
- Private certificates can also secure Amazon EC2 instances, Amazon ECS containers, and IoT devices.

## Imported certificates

- Third-party certificates can be imported into AWS Certificate Manager.

## CA certificates

- Certificates can be issued for creating a private CA up to five levels deep, including a root CA, three levels of subordinate CAs, and a single issuing CA.

