Load Balancing Algorithms
---

# Round Robin

- Assigns requests `sequentially across servers`
— first to Server 1, then 2, and so on, cycling back after the last

# Least Connections

- Sends new requests to the `server with the fewest active connections`

# Weighted Round Robin

- Distributes requests based on `server capacity using predefined weights`

# Weighted Least Connections

- A hybrid strategy: considers both `server weight and active connections` for smarter load distribution

# IP Hash

- Uses the client's IP address to consistently route their requests to the `same server` — ensuring `session persistence`

# Least Response Time

- Sends traffic to the server with the `fastest response time` and fewest connections

# Random

- Assigns each request to a `random server` — simple but less optimized.

# Least Bandwidth

- Routes requests to the server currently handling the `least network traffic`
