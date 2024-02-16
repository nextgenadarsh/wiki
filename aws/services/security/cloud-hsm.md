AWS CloudHSM
---

- Instead of using the default AWS KMS store, you can `create a custom key store using a VPC-hosted AWS CloudHSM cluster and authorize KMS to use it as its dedicated key store`.
- CloudHSM clusters are created using `multiple single-tenant hardware devices`.
- Amazon maintains the AWS CloudHSM hardware and backs up its contents but never enters an AWS CloudHSM device.
- Organizations might use an AWS CloudHSM deployment if `compliance rules explicitly require that encryption keys are protected in a single-tenant hardware device`.
- AWS CloudHSM can operate as a complete stand-alone hardware device for your synchronous and asynchronous keys and provide you with Federal Information Processing Standard (FIPS) 140-2 Level 3 compliance.

