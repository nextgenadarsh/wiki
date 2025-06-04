Customer Gateway
---

- VPN concentrator on the `customer side` of a site-to-site `VPN connection`.
- Uses `IPsec to encrypt the data` transmitted between the on-premises network and the VPC.
- Supports routing options:
  - Static routing
    - Enables you to `specify routes` for traffic over a VPN connection.
    - Specify the `IP address ranges and destinations` for your traffic, and the VPN connection will use this information to route traffic.
  - Dynamic routing
    - AWS VPN connection will `automatically add and remove routes as needed`, based on the traffic paths available.
