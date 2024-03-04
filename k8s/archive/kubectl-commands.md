# kubectl Cheat Sheet

## Tips

- You need to update the cluster/context/user details in config file for kubectl configuration
- `cluster` represents the kubernetes cluster created generally for your environment
- `context` is used to alias cluster parameters with human-readable name
- `--insecure-skip-tls-verify` is used to ignore the certificate errors

## Configuration

| Command                           | Purpose
| --                                | --
| `kubectl config get-contexts`     | get all available contexts
| `kubectl config set-context <context-name>`   | create/modify current context
| `kubectl config view`             | view kubectl configurations
| `kubectl config set-context <context-name> --namespace=<namepsace>`   | create/modify context
| `kubectl config use-context <context-name>`                   | use the particular context
| `kubectl config --help`                                       | view command options
| `alias k=kubectl`                                             | create alias for kubectl
| `kubectl api-resources`                                       | lists all available commands plus their short names
| ``

## Describe

| Command                                                       | Purpose
| --                                                            | --
| `kubectl describe pod <pod-name>`                             | 
| `kubectl describe pvc <pvc-name>`                             | 
| `kubectl delete pod <pod-name> --force`                       | 
| `kubectl explain pods.spec`                                   | list all fields of pod spec

kubectl describe pods | grep -C 10 "author=John Doe"
kubectl get pods -o yaml | grep -C 5 labels:

| `kubectl create serviceaccount <account-name>`                | create new service account
| `kubectl get serviceaccounts`                                 | get all service accounts
| `kubectl describe serviceaccount <account-name>`              | get service account details
| `kubectl get secrets`                                         | 
| `kubectl create role read-only --verb=list,get,watch --resource=pods,deployments,services`
| `kubectl get roles`                                           | 

## Cluster

| Command                                                       | Purpose
| --                                                            | --
| `kubectl cluster-info`


## Nodes

| Command                                                       | Purpose
| --                                                            | --
| `kubectl get nodes`

# Pods

| Command                                                       | Purpose
| --                                                            | --
| `kubectl get pods -n default`                                 | view the pods in default namespace
| `kubectl get pods --selector key1:value1,key2:value2 --no-headers`    | view pods without header and with matching labels
| `kubectl get pod,svc -n kube-system`                          | view the pod and services in kube-system namespace
| `kubectl get pod,svc -n kube-system`                          | view the pod and services created in default namespace

## Working with Deployment

| Command                                                       | Purpose
| --                                                            | --
| `kubectl get deploy`                                          | 
| `kubectl set image <deployment-name> nginx=nginx:1.9.1`       | 
| `kubectl rollout status deployment <deployment-name>`         | 
| `kubectl rollout undo <deployment-name>`                      | 
| `kubectl rollout history deploy <deploy-name> --revision=1`   | 

## Container

| Command                                                       | Purpose
| --                                                            | --
| `kubectl run <name> --image=<image> --replicas=1000`


| Command                                                       | Purpose
| --                                                            | --
| `kubectl [command] [TYPE] [NAME] [flags]`                     | command syntax
| `kubectl create deployment <deployment> --image=<image-name>` | create a deployment that manages a pod
| `kubectl get deployments`                                     | view the deployment
| `kubectl delete deployment <deployment> -n default`           | delete deployment in default namespace
| `kubectl get events -n default`                               | view cluster events
| `kubectl expose deployment <deployment> --type=LoadBalancer --port` | expose the pod to public internet
| `kubectl get services`                                        | view the services
| `kubectl delete service <service> -n default`                 | delete service in default namespace
| `kubectl run --replicas=1000 <image>`                         | runs 1000 replicas of the image in cluster
| `kubectl rolling-update <image> --image=web-server:2`
| `kubectl rolling-update <image> --rollback`

## Working with Secret

| Command                                       | Purpose
| --                                            | --
| `kubectl get secret <secret-name> -o yaml`    | show secret data

## Working with commands

| Command                                       | Purpose
| --                                            | --
| `kubectl exec -it <pod-name> <command> <args>`| execute command on pod

## Working with Taint

| Command                                       | Purpose
| --                                            | --
| `kubectl taint nodes <node-name> key=val:<taint-effect>`

## Working with logs

| Command                                       | Purpose
| --                                            | --
| `kubectl logs -f <pod-name>`                  | stream logs live(-f)
| `kubectl top node`