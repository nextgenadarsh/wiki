# dig

- Tool used to `query DNS server`
- Can `query multiple DNS servers simultaneously`
- Provides more detailed information about the DNS records
- Example:
    ```
    ; <<>> DiG 9.10.6 <<>> centoreal.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 29422
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 512
    ;; QUESTION SECTION:
    ;centoreal.com.			IN	A

    ;; AUTHORITY SECTION:
    centoreal.com.		900	IN	SOA	ns-1896.awsdns-45.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400

    ;; Query time: 49 msec
    ;; SERVER: 2001:4860:4860::8888#53(2001:4860:4860::8888)
    ;; WHEN: Fri Feb 10 21:53:21 IST 2023
    ;; MSG SIZE  rcvd: 126
    ```
