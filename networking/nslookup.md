# nslookup

- Tool used to `query DNS server`
- Can only be used to `query one DNS server at a time`
- Displays `only A and AAAA records`
- Support both `interactive and non-interactive` modes
- Example:
    ```
    adarsh$ nslookup google.com
    Server:		2001:4860:4860::8888
    Address:	2001:4860:4860::8888#53

    Non-authoritative answer:
    Name:	google.com
    Address: 142.250.192.142
    ```