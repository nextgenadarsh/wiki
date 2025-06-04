AWS Web Application Firewall (WAF)
---

- Protect web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources.
- Enables you to create rules that `block, allow, or monitor web requests` based on conditions.
- Provides `custom filtering` of incoming (ingress) public traffic requests for IPv4 and IPv6 HTTP and HTTPS requests at each edge location.
- WAF Rules:
  - are created using `conditions` combined into a web ACL.
  - can be applied to public-facing application load balancers, Amazon CloudFront distributions, Amazon API gateway hosted APIs, and AWS AppSync.
  - can be applied to either Allow or Deny the request
- WAF supports the following behaviors:
  - IP addresses
  - HTTP methods
  - Cookies
  - Headers
  - Query strings
- WAF supported rule types:
  - Regular rules (condition based)
  - Rate-based rules
  - Group rules
