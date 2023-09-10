# Lambda

`#serverless #compute-service #auto-scale #stateless #monitoring-logging `

## Invocation

- Synchronous
  - No built-in retries
- Asynchronous
  - events are queued in event queue
  - send response to destination service
- Polling
  - Synchronous
  - retries depends on source configuration