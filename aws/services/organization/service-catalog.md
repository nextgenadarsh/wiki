AWS Service Catalog
---

- enables organizations to `create, manage, and distribute a catalog of approved IT services installed with CloudFormation templates`.
- can help organizations `maintain control over their IT environments` by providing a `central repository` for approved cloud services and ensuring that `only authorized services are deployed`.
- Administrators can create and manage catalogs of AWS and third-party services, making them available to users within the organization.
- Users can access the catalog and launch services while AWS Service Catalog ensures that they are launched in the correct AWS accounts and with the appropriate permissions.
- To control who gets to deploy specific CloudFormation templates, AWS Service Catalog can be used to manage the distribution of CloudFormation templates portfolios to a single AWS account ID or an organizational unit contained within an AWS organization.
- When an approved product is selected, Service Catalog delivers a confirmation to CloudFormation, which executes the template and creates the product.
- Use CloudFormation and Service Catalog together to create a self-serve portal of portfolios and products.
