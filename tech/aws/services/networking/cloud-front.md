Amazon CloudFront
---

- AWS’s `global CDN service`.
- is `located at each edge location data center` that optimizes the `delivery of both static and dynamic web content`, such as website images, videos, media files, and updates.
- When the viewer (which is the end user in CloudFront terminology) requests content that is served by `CloudFront cache`, the viewer’s `request is sent to the closest edge location with the lowest latency`, ensuring the requested content is delivered to the viewer with the best performance possible.
- `Persistent connections` to each origin service location are `kept open by CloudFront to fetch requested objects from the origin locations` as quickly as possible.
- Deploying a CloudFront distribution also `provides increased resiliency` for your applications, as multiple edge locations are available for accessing the requested content.
- Route 53 records are stored redundantly in each region to ensure the reliability of the AWS global DNS service.

![CloudFront Operation](../../images//cloud-front-operation.png)
> Fig: CloudFront Operation

# Regional Edge Caches

- is an `additional caching location within select AWS regions` with a large amount of additional cache resources to ensure that more objects remain cached.
- is `located between the origin (Amazon S3 bucket or web server) and the edge location` and helps speed up access to frequently accessed content by keeping cached content as close as possible to the end user.
- A simple request for content that is available is served by the regional edge cache; RESTful API methods such as PUT, POST, and DELETE are sent directly to the edge location and do not proxy through regional edge cache locations.
- Requests served from the regional edge cache don’t go back to the edge cache or to the origin location.

![Regional Edge Location Placement](../../images/regional-edge-location-placement.png)
> Fig: Regional Edge Location Placement

# CloudFront Use Cases

## Speeding up static website content delivery

- Static content includes images, videos, CSS style sheets, and JavaScript files.

## Providing video-on-demand or live streaming video

- Video-on-demand options can stream formats such as MPEG DASH, Apple HLS, Microsoft Smooth Streaming, and CMAF to any network-enabled device.
- Live streaming supports the caching of media fragments at the edge location; the proper order to stream the media fragments is documented in the associated manifest file.

## Encrypting content

- You can add field-level encryption to protect specific data fields against tampering during system processing.
- This ensures that only select applications can view the encrypted data fields.

## Customized requests

- Using CloudFront functions or `Lambda@Edge` functions allows for customization of both ingress and egress requests with custom functions.

# HTTPS Access

- CloudFront can be configured to require the use of the HTTPS protocol to request content, ensuring that all connections remain encrypted.
- CloudFront is configured from the properties of each distribution.
- Selecting HTTPS ensures that communication remains encrypted for both ingress and egress data transfer.

# Serving Private Content

- Use `signed URLs or signed cookies`.
- You can create a signed URL or signed cookie that grants temporary access to a private file.
- Use an `origin access identifier (OAI)` to grant CloudFront permission to access your Amazon S3 bucket or custom origin and serve your private content.

## Using Signed URLs and/or signed cookies

- helps you `distribute private content across the Internet to a select pool of viewers`.
- The `content is signed using the private key from the associated public/private key pair`.
- CloudFront compares the signed and unsigned portions of the signed URL or cookie.
- If the public/private keys match, the content is served; if the keys don’t match, the content is not served.
- To use signed URLs with CloudFront, you must `set up a trusted signer`, which is an AWS account or an IAM user in your AWS account that has permission to create signed URLs and signed cookies.
- You also must `configure your CloudFront distribution to use signed URLs` as an additional layer of security.
- When creating signed URLs and/or signed cookies, conditions for accessing the URL are dictated by a JSON policy statement which mandates which of the following restrictions are to be enforced:
  - The date and time after which the URL is accessible.
  - The date and time after which the URL is no longer accessible.
  - The IP address range of devices that can access content.

## Using an Origin Access Identifier

- Direct access to the S3 bucket can be restricted using a special CloudFront user called an origin access identity (OAI) that is associated with your CloudFront distribution.
- Configuring S3 bucket permissions allows the OAI to access the requested objects from the S3 bucket for CloudFront serving the objects to the viewer.
- The OAI is a special AWS Identity and Access Management (IAM) user associated with your CloudFront distribution.
- Once the OAI is created, only the OAI user can directly access objects in the S3 bucket origin; permissions need to be configured to allow only the OAI to access the bucket.

# Restricting Distribution of Content

- When an end user requests content from CloudFront, the content is served regardless of the physical location of the end user.
- To allow users only from approved countries to access cached content, `geo-restrictions` can be enabled by defining CloudFront access lists.

![CloudFront Geographic Restrictions](../../images/cloud-front-geographic-restrictions.png)
> Fig: CloudFront Geographic Restrictions

# CloudFront Origin Failover

- CloudFront also has an additional option to assist with `data reliability and resiliency called origin failover`.
- To set up origin failover, create a CloudFront distribution with at least `two origins in place` and define cache behavior to use the primary origin group for content requests.
- In the CloudFront distribution origin group, define the HTTP status codes to be used as failover criteria to the secondary origin; for example, 500, 502, 503, or 504 codes.
- With origin failover enabled, CloudFront operates normally and relies on the primary origin.
- When one of the specified HTTP status codes is received, failover to the secondary origin occurs if present.
- The speed of failover can be controlled by adjusting the `Origin Connection Timeout and the Origin Connection Attempts default values` for the respective CloudFront distribution.

# Video-on-Demand and Live Streaming Support

- CloudFront can deliver video on demand (VOD) or live streaming video from any HTTP origin.
- Video content must be packaged together with a supported encoder (MPEG DASH, Apple HLS, CMAF) before CloudFront can distribute the streaming content.
- `CloudFront and AWS Media Services` can be used together to deliver live streaming video.

## Video on demand

- Content is stored on a server and can be watched at any time.
- Content can be formatted and packaged using AWS Elemental MediaConvert.
- After content is packaged, it can be stored in Amazon S3 and delivered upon request using CloudFront.

## Live streaming video

-  AWS Elemental MediaConvert can be used to compress and format the live streaming video delivered by CloudFront to end users.

# Edge Functions

- Serverless custom functions called edge functions can be written to `customize how a CloudFront distribution processes HTTP viewer requests and responses`.
- Edge functions can be written using CloudFront functions and `Lambda@Edge` functions.

## CloudFront Functions

- JavaScript can be used to create what are called `“lightweight” functions to monitor viewer requests and responses for customizations`.
- CloudFront Functions must finish executing within sub-milliseconds. 
- Use cases:
  - Modifying the HTTP request from the viewer
    - Return the modified request to CloudFront for processing. Headers, query strings, and URL paths can be modified.
  - Header manipulation
    - Insert, modify, or delete HTTP headers for the viewer request or response.
  - URL redirects
    - Redirect viewers to other pages based on information contained in the request.

## Lambda@Edge Functions

- is a managed AWS service that `allows you to craft custom functions` to carry out any task written in a variety of programming languages, including Python, Go, C#, Node.js, or Java.
- `sits in the middle of the ingress and egress communication paths`.
- could send specific content to users sending requests from a smartphone and send different specific content to users sending requests from a traditional computer.
- Lambda functions can be executed when the following requests occur:
  - When CloudFront receives a request for content from a viewer
  - When CloudFront forwards a request to the origin server (S3 bucket or web server)
  - When CloudFront receives a response from the origin server (S3 bucket or web server)
  - When CloudFront sends back a response to the viewer
- Lambda@Edge Use Cases:
  - You could return different objects to viewers based on the devices they’re using. In this case, the Lambda@Edge function could read the User-Agent header, which provides information about a viewer’s device.
  - Perhaps you’re selling clothing in different sizes. You could use cookies to indicate which size the end user selected when looking at clothing choices. The Lambda@Edge function could show the image of the clothing in the selected color and size.
  - A Lambda@Edge function could inspect and confirm the validity of authorization tokens to help control access to your content.
  - A Lambda@Edge function could be used to confirm viewer credentials to external sources.

<h2 style="background-color:lightgreen"># CloudFront Cheat Sheet</h2>

- Control access to your public-facing content by mandating access via HTTPS endpoints using TLS 1.3.
- Origins include S3 buckets, AWS Elemental MediaStore container, an Application Load Balancer, a Lambda function URL, or a custom origin web server.
- Securing content access by using signed URLs and cookies.
- Use origin access identity (OAI) to restrict direct access to S3 bucket access, making it only accessible from CloudFront.
- Origin failover automatically serves content from the secondary origin when the primary origin is not available.
- Lambda@Edge functions support customizations that take from milliseconds to seconds to execute.
- CloudFront functions are lightweight functions that take less than one millisecond to execute.

# AWS CloudFront Pricing

Amazon CloudFront delivers web and media content stored in S3 buckets to clients worldwide using one of the hundreds of edge locations. If the requested content is already cached at the edge location, it is delivered to the viewer (end user) quickly. Delivery costs are billed per GiB transferred from an edge location server to the viewer; customers are charged per 10,000 HTTP requests. The billing rate for serving data ranges from $0.085 per GiB to $0.170 per GiB and is determined by where the viewer request originates from. Any data transferred out to an edge location from an EC2 instance, S3 bucket, or an Elastic Load Balancer has no additional data transfer charges from each AWS service, just CloudFront charges (see Figure 15-3). Customers can save up to 30% in delivery costs and 10% off AWS WAF service charges by subscribing to a CloudFront Security Savings Bundle. Amazon CloudFront costs increase (see Table 15-2) as additional features are enabled:

- Encryption: Although there is a charge for encryption, less data will be sent; therefore, data transfer costs will be reduced.
- Logging: Enabling real-time logs costs $0.01 per million log lines written.
- CloudFront Origin Shield: Improves the cache hit ratio by using CloudFront regional edge caches, which are hosted across three AZs. Enabling Origin Shield is charged per 10,000 requests.
- CloudFront functions and Lambda@Edge functions: Charged per request and duration.
- Custom SSL/TLS certificates and domain names: Charged monthly.

![Data Transfer Charges Minimized](../../images/cloudfront-data-transfer-charges-minimized.png)
> Fig: Data Transfer Charges Minimized

## Cost Comparison for CloudFront Costs

Data Type | Pricing | Details
--  | --  | --
CloudFront to the Internet/viewer | $0.085–$0.120 per GiB (first 10 TB) | Data transferred from edge location to viewer location
CloudFront to data or server origin | $0.020–$0.160 per GiB | Data requests to origin (POST and PUT)
HTTP/HTTPS requests | $0.0075–$0.0120 per 10,000 requests | Charges for HTTP and HTTPS requests
Origin shield requests  | $0.0075–$0.0090 per 10,000 requests | Requests to origin shield cache layer
File invalidation requests  | $0–$0.005 per path requested  | Remove files from edge location before TTL expires
Lambda Functions requests | $0.60 per million requests/$0.00005001 per GiBps execution time | Charged per request and execution time
Field-Level Encryption requests | $0.02 per 10,000 requests | Encrypt specific fields in HTTP form
Real-time log requests  | $0.01–$0.01 for every 1 million log lines written | Log requests to distribution
Custom SSL Certificate  | $600 per month per certificate  | Used when content is delivered to browsers that don’t support Server Name Indication (SNI)

## CloudFront Pricing Cheat Sheet

S3 transfers under 1 GiB are free per month; however, Amazon CloudFront delivery could be faster depending on the location of the end user.
Transfers of data over 50 GiB per month from Amazon S3 or EC2 instances will be cheaper using an Amazon CloudFront distribution.
If applications exclusively serve GET requests, direct requests to the S3 bucket are cheaper.
Applications using both GET and POST requests will be cheaper to access using an Amazon CloudFront distribution.
HTTP requests for data are cheaper than HTTPS requests.
By default, all files cached at an Amazon CloudFront edge location expire after 24 hours.
Change the minimum, maximum, and default time to live (TTL) values on all cached objects in the distribution to extend the cache storage time. Each object in the CloudFront cache is identified by a unique cache key. When a viewer requests an object that is stored in the edge location cache, this is defined as a cache “hit,” which reduces the load on the origin server and reduces the latency of the object delivery to the viewer. To improve the cache hit ratio, include only the minimum values in the cache key (see Figure 15-4) for each object. The default cache key includes the domain name of the CloudFront distribution and the URL path of the requested object. Other cache values, HTTP headers, and cookies can be defined with a cache policy.
- For cache content that will rarely or never change, setting the Cache-Control HTTP headers on the origin server will set the cache rate at the client’s browser and at the edge location.
- Enabling compression will reduce data transfer costs.
- Reserve capacity a year in advance.
- Opt out of more expensive regions/edge locations to reduce data transfer costs.

