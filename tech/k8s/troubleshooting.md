# Troubleshooting

## Configuration Issues

### When I execute `kubectl get pods` I am getting error as `error: You must be logged in to the server (Unauthorized)`

#### Checklist:
- Your `~/.kube/config` file
    - contains valid cluster detail like `certificate-authority-data`
    - contains valid user and `token`. mostly token might have expired.

### Other issue