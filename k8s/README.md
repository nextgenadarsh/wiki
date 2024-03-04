
# kubectl Installation

- Follow [Installation Guide](https://kubernetes.io/docs/tasks/tools/) to install kubectl
- Verify if kubectl is installed with version: `kubectl version --client`
- View K8 Configuration: `kubectl config view`

> K8 configuration file path: `~/.kube/config`

# Cluster

- Get cluster info: `kubectl cluster-info`

# Context

- Get list of contexts: `kubectl config get-contexts`

# Resource Short Names
Resource  | Short Name
--        | --
Namespace | ns
Pods      | po
Services  | svc

# Common Resource Commands

- `kubectl get all --all-namespaces -o wide`
- `kubectl get <resource> --all-namespaces`
- `kubectl get <resource> --namespace=<namespace> | grep <text>`
- `--dry-run`

# Namespace

- Create namespace: `kubectl create ns ckad`
- List namespaces: `kubectl get ns`
- Set current context namespace for future commands: `kubectl config set-context --current --namespace=ckad`
- Verify current namespace: `kubectl config view --minify | grep namespace:`
- Check resources in namespace: `kubectl api-resources --namespaced=true`
- Check resources NOT in namespace: `kubectl api-resources --namespaced=false`

# Field Selectors

- Get pods with status as Running `kubectl get pods --field-selector status.phase=Running`
- Get services in all namespace: `kubectl get services --all-namespaces --field-selector`
- Get multiple resource types: `kubectl get pods,services --all-namespaces`

# Node

- Get node description: `kubectl describe node <node-name>`

# Pod

- Example Commands:
  - `kubectl get pods --field-selector status.phase=Running`
  - `kubectl run nginx-app --image=nginx --restart=Never`
  - `kubectl exec -it nginx -- /bin/bash`
  - `kubectl run nginx --image=nginx --restart=Never --dry-run=client -o yaml > nginx-pod.yaml`
- 