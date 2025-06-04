System Design
---

1. Horizontal vs Vertical Partitioning: https://bit.ly/3zyBRew
Vertical partitioning splits tables by columns, often separating different features. Horizontal partitioning splits tables by rows, distributing data across multiple servers. Vertical organizes data logically, while horizontal improves scalability + performance.

2. Apache Kafka: https://kafka.apache.org/
Kafka is a distributed streaming platform using a publish-subscribe model. It's fast due to sequential disk I/O, zero-copy principle, and efficient batching of messages. 

3. Rate Limiter: https://lnkd.in/dvvNjKue
A rate limiter controls the rate of requests a client can make to a service. It prevents overload and ensures fair resource usage.

4. JWT vs OAuth vs SAML: https://lnkd.in/dPqrcN3u
JWT is a compact, self-contained token for secure information transmission. OAuth is an authorization framework for delegated access. SAML is an XML-based standard for exchanging authentication and authorization data. 

5. Single Sign-On (SSO): https://lnkd.in/diU54_-s
SSO allows users to access multiple applications with one set of credentials. It typically uses a central authentication server and protocols like SAML/OAuth. 

6. Microservices vs Monolithic Architecture: https://bit.ly/4bAt2hv
Microservices architecture breaks an application into small, independent services. Monolithic architecture is a single, tightly-coupled unit. Microservices offer scalability while monoliths are simpler to develop + deploy.

7. Reverse Proxy vs Forward Proxy: https://bit.ly/3xOx6wO
A reverse proxy sits in front of web servers, forwarding client requests to backend servers. A forward proxy sits in front of clients, forwarding their requests to the internet. Reverse proxies are used for load balancing and security, while forward proxies are used for anonymity and filtering.

8. CAP Theorem: https://lnkd.in/dQhhe4jD
The CAP theorem states that a distributed system can only provide two of three guarantees: Consistency, Availability, and Partition tolerance. In practice, partition tolerance is necessary, so systems must choose between consistency and availability during network partitions.

9. Global Scale System Design:https://bit.ly/3RW8DMJ
Key considerations include data replication, CDN usage, distributed caching, efficient load balancing, and handling data consistency across regions. Latency management, regulatory compliance, and disaster recovery are also crucial for global systems.

10. Efficient Caching Strategy: https://lnkd.in/dfnP9keJ
Implement multi-level caching (browser, CDN, application server, database). Use appropriate cache invalidation strategies (TTL, event-based). Consider cache coherence for distributed systems.

Huge thanks to Gaurav Sen for stellar system design content! 🙌 Dive into their amazing insights!