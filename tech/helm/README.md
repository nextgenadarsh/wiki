# Helm

> A package/release manager for [kubernetes](../k8s/README.md).

## Common Commands

| Command                                       | Purpose
| --                                            | --
| `helm install <release-name> <chart-name> ...`| Install the helm release
| `helm upgrade <release-name> ...`     | Upgrade the release
| `helm rollback <release-name> ...`    | Rollback the release
| `helm uninstall <release-name> ...`   | Uninstall the release
| `helm repo add <repo-name> <repo-url>`
| `helm repo list`
| `helm list`                           | List the releases



> References:

- [Helm Quickstart Guide](https://helm.sh/docs/intro/quickstart/)