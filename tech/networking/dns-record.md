# DNS Record

- DNS, is a global system responsible for `mapping` human-readable `hostnames to` their corresponding `IP Addresses`
- DNS records are `stored in text files (zone files)` on the authoritative DNS server

## Types of DNS Record

### A record

- "A" in A record stands for `"address"`
- `Shows the IP address` for a specific hostname or domain
- Supports `only IPV4 addresses`
- Uses:
  - For `IP address lookup`
  - For domain name system-based blackhole list (DNSBL) to `block email from known source`

### AAAA record

- Like A record, point to the IP address for a domain
- It points to `IPV6 addresses`
- Uses:
  - To resolve a domain name to the newer IPV6 protocol address

### Canonical Name (CNAME) record

- Points a domain name (an `alias`) to another domain
- It's also possible to `point a CNAME to another CNAME`. However, doing so is `inefficient` and can lead to `slow load speed` and poor user experience.
- Uses:
  - For running `multiple subdomains` for different purposes on the same server.
  - 

### Nameserver (NS) record

- Specifies the `authoritative DNS server for a domain`
- Helps point to where internet applications like a web browser can find the IP address for a domain name
- Usually, `multiple nameservers` are specified for a domain
- These nameservers `connect your domain name to the actual server` your site is hosted on

### Mail exchange (MX) record

- Shows where `emails` for a domain `should be routed to`
- You can have `multiple MX records` for a single domain name
- It is possible to hand off emails to a dedicated email server using MX record.
- Example Record:

| Name   | Type | RDATA         |
| ------ | ---- | ------------- |
| @      | MX   | mx.zoho.com   |
| @      | MX   | mx2.zoho.com  |

> Additional DNS record types

### Start of Authority (SOA) record

- Stores `admin information about a domain`. It includes the email address of the admin and when the domain was last updated.

### Text (TXT) record

- Lets the owner of a domain store text values in the DNS. Several services use this record to `verify ownership` of a domain.

### PTR record

- Provides a domain name for reverse lookup. 
- `Opposite of an A record` as it provides the domain name linked to an IP address instead of the IP address for a domain.

### SRV record

- Stores the IP address and port for specific services.

### CERT record

- Stores public keys certificates.

### DCHID record

- Stores information related to dynamic host configuration protocol (DHCP).

### Delegation Name (DNAME) record

- Works very similarly to CNAME
- It points all the subdomains for the alias to the canonical domain name. That is, pointing the DNAME for secondsite.com to example.com will also apply to staff.secondsite.com and any other subdomain.