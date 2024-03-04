K8 Commands
---

# Getting Started

## kubectl Installation

- Follow [Installation Guide](https://kubernetes.io/docs/tasks/tools/) to install kubectl
- Verify if kubectl is installed with version: `kubectl version --client`
- View K8 Configuration: `kubectl config view`

> K8 configuration file path: `~/.kube/config`

## Aliases

- `alias k='kubectl'`
- `alias kgp='kubectl get po -o wide'`
- `alias kgd='kubectl get deploy -o wide'`
- `alias kgs='kubectl get svc -o wide'`
- `alias kgc='kubectl config get-contexts'`
- `alias kgn='kubectl get ns'`

## Configuration

> Use `--insecure-skip-tls-verify` to ignore certificate error

- `cat ~/.kube/config`
- `kubectl config view`
- `kubectl config get-clusters`
- `kubectl config get-contexts`
- `kubectl config current-context`
- `kubectl config get-contexts my-context`
- `kubectl config set-context my-context --user=cluster-admin`

## Resource Short Names

> `kubectl api-resources`

Resource          | Short Name
--                | --
Namespace         | ns
Pod               | po
Service           | svc
Service Account   | sa

## Cluster

- Get cluster info: `kubectl cluster-info`

## Context

- Get list of contexts: `kubectl config get-contexts`

## Namespace

- Create namespace: `kubectl create ns ckad`
- List namespaces: `kubectl get ns`
- Set current context namespace for future commands:
  - `kubectl config set-context --current --namespace=ckad`
- Verify current namespace:
  - `kubectl config view --minify | grep namespace:`
- Check resources in namespace:
  - `kubectl api-resources --namespaced=true`
- Check resources NOT in namespace:
  - `kubectl api-resources --namespaced=false`
- Get all resource from namespace 'ckad': `kubectl get all -n ckad`
- Get all resource from all namespaces:
  - `kubectl get all -A`

## Explain

- `kubectl explain po`
- `kubectl explain pods.spec.containers`

## Field Selectors

- Get pods with status as Running `kubectl get pods --field-selector status.phase=Running`
- Get services in all namespace: `kubectl get services --all-namespaces --field-selector`
- Get multiple resource types: `kubectl get pods,services --all-namespaces`

## Labels

- Apply label to all pods: `kubectl label po --all status=green`
- Apply label to pod, overwrite if exists already:
  - `kubectl label po nginx-app status=blue --overwrite`
- Update a pod identified by type and name in yaml file:
  `kubectl label -f pod.yaml env=prod`
- Update the label only if resource is unchanged form version 1
  - `kubectl label po nginx-app type=test --resource-version=1`
- Remove label 'status' from pod: `kubectl label po nginx-app status-`

## Describe

- Describe pod 'nginx-app': `kubectl describe po nginx-app`
- Describe pod with label 'env=prod': `kubectl describe po -l env=prod`
- Describe all pods: `kubectl describe po`
- Describe a pod identified by file: `kubectl describe -f pod.yaml`

## Execute commands

- Execute command on pod: `kubectl exec pod-name -- date`
- Open sh terminal on pod container: `kubectl exec nginx-app -it -- sh`
- Execute command on deployment's 1st pod's 1st container:
  - `kubectl exec deployment.apps/my-deploy -- date`
- Execute command on pod's container: `kubectl exec nginx-app -c nginx-app-container -- date`
- Open bash terminal on pod: `kubectl exec nginx-app -it -- bash -il`

# Application Design & Build

## Node

- Get node description: `kubectl describe node <node-name>`

## Pod

- Example Commands:
  - `kubectl get pods --field-selector status.phase=Running`
  - `kubectl run nginx-app --image=nginx --restart=Never --port=5700 --labels="app=demo,env=test"`
  - `kubectl exec -it nginx -- /bin/bash`
  - `kubectl run nginx --image=nginx --restart=Never --dry-run=client -o yaml > nginx-pod.yaml`

## Job

- Create job: `kubectl create job my-job --image=busybox`
- Create job with command: `kubectl create job my-job --image=busybox -- date`
- Create job from cron job: `kubectl create job my-job --from=cronjob/my-cronjob`

## CronJob

- Create cron job:
  - `kubectl create cronjob my=cronjob --image=busybox --schedule="*/1 * * * *"`
- Create cron job with command:
  - `kubectl create cronjob my=cronjob --image=busybox --schedule="*/1 * * * *" -- date`

# Application Deployment

## Deployment

- Create deployment: `kubectl create deployment my-deploy --image=nginx`
- Create deployment with command: `kubectl create deployment my-deploy --image=nginx -- date`
- Create deployment with replicas:
  - `kubectl create deployment my-deploy --image=nginx --replicas=3 --port=5577`
- Delete deployment: `kubectl delete deployment my-deploy`

## Scaling

- Scale deployment to 2 pods: `kubectl scale deployment my-deploy --replicas=2`
- Scale deployment to 2 pods: `kubectl scale --replicas=2 rs replica-set`
- Scale deployment to 4 pods ONLY IF current pods count is 3:
  - `kubectl scale --current-replicas=3 --replicas=4 deployment my-deploy`
- Scale resource identified by file to 3 pods:
  `kubectl scale --replicas=3 -f deployment.yaml`
- Auto scale: `kubectl autoscale deployment my-deploy --min=2 --max=5 --cpu-percent=60`

## Set

- Update image of a deployment:
  - `kubectl set image deployment my-deploy nginx=nginx:1.9.1`
- Update all deployments' and rcs' containers' image:
  - `kubectl set image deployment,rc nginx=nginx:1.9.1 --all`

## Rollback

- Rollback to previous deployment:
  - `kubectl rollout undo deployment my-deploy`
- Rollback to previous deployment with dry-run:
  - `kubectl rollout undo deployment my-deploy --dry-run=server`
- Rollback to previous deployment to revision 3:
  - `kubectl rollout undo deployment my-deploy --to-revision=3`
- Rollback status: `kubectl rollout status deployment my-deploy`
- Rollback history: `kubectl rollout history deployment my-deploy`
- Rollback details of revision:
  - `kubectl rollout history deployment my-deploy --revision=3`

# Application Observability & Maintenance

## Logs

- Get pod's logs: `kubectl logs nginx-app | more`
- Get most recent 10 logs: `kubectl logs nginx-app --tail=10`
- Get last 1hr logs: `kubectl logs nginx-app --since=1h`
- Get pod's container's logs: `kubectl logs nginx-app -c container-name`
- Get pod's all containers' logs: `kubectl logs nginx-app --all-containers=true`
- Get deployment's logs: `kubectl logs deployment.apps/my-deploy`
- Get logs of 1st container of a job: `kubectl logs job my-job`

## Metrics

> [Install metrics server on K8 cluster](https://github.com/kubernetes-sigs/metrics-server)

- Get metrics of all nodes: `kubectl top node`
- Get metrics of all pods from all namespaces: `kubectl top po -A`
- Get metrics of particular nodes: `kubectl top node node-name`
- Get metrics of all pods: `kubectl top po`
- Get metrics of all nodes in namespace: `kubectl top node -ns=kube-public`
- Get metrics of pod and its containers: `kubectl top pod --containers`
- Get metrics of all pods with label 'env=prod': `kubectl top pod -l env=prod`

## Cordon

- Mark node as unschedulable: `kubectl cordon my-node`

## UnCordon

- Mark node as schedulable:
  - `kubectl uncordon my-node`

## Drain

- Drain node, even if there are pods not managed by RC, RS, Job, DaemonSet, or StatefulSet on it
  - `kubectl drain my-node --force`
  - `kubectl drain my-node --grace-period=900`

## Taint

- Update node with a taint key 'dedicated' and value 'special-user' and effect 'NoSchedule'. If a taint with that key and effect already exists, its value is replaced as specified:
  - `kubectl taint node my-node dedicated=special-user:NoSchedule`
- Add a taint with key 'dedicated' on node having label env=prod
  - `kubectl taint node -l env=prod dedicated=special-user:PreferNoSchedule`
- Ad a taint with key 'mytaint' and no value:
  - `kubectl taint node my-node mytaint:NoSchedule`
- Remove taint with key 'dedicated' and effect 'NoSchedule' if exists:
  - `kubectl taint node my-node dedicated:NoSchedule-`
- Remove all taints with key 'dedicated':
  - `kubectl taint node my-node dedicated:NoSchedule-`

# Application Environment, Configuration and Security

## ConfigMap

- `kubectl create cm my-cm --from-file=path/to/folder`
- `kubectl create cm my-cm --from-file=path/to/file.txt`
- `kubectl create cm my-cm --from-file=key1=/path/to/file1.txt --from-file=key2=/path/to/file2.txt`
- `kubectl create cm my-cm --from-literal=key1=value1 --from-literal=key2=value2`
- `kubectl create cm my-cm --from-env-file=path/to/file.env`

## Secret (Generic)

- `kubectl create secret generic my-secret --from-file=path/to/folder`
- `kubectl create secret generic my-secret --from-literal=key1=secret1 --from-literal=key2=secret2`
- `kubectl create secret generic my-secret --from-env-file=path/to/secret.env`

## Role

- `kubectl create role pod-reader --verb=get --verb=list --verb=watch --resource=pods`
- `kubectl create role pod-reader --verb=get --resource=pods --resource-name=readable-pod --resource`

## RoleBinding

- `kubectl create rolebinding admin --clusterrole=admin --user=user1 --user=user2 --group=group1`

## ClusterRole

- Create a ClusterRole 'pod-reader' that allows users to perform get/watch/list on pods:
  - `kubectl create clusterrole pod-reader --verb=get,list,watch --resource=pods`
- Create a ClusterRole with ResourceName specified:
  - `kubectl create clusterrole pod-reader --verb=get --resource=pods --resource-name=readable-pod`

## ClusterRoleBinding

- `kubectl create clusterrolebinding cluster-admin --clusterrole=cluster-admin --user=user1 --user`

# Service & Networking

## Service

- Create new ClusterIp service:
  `kubectl create svc clusterip my-svc --tcp=5678:8080`
- Create new ClusterIp service in headless mode:
  `kubectl create svc clusterip my-svc --clusterip="None"`
- Create new NodePort service:
  `kubectl create svc nodeport my-svc --tcp=5678:8080`

## Exposing Resources

- `kubectl expose rc nginx --port=80 --target-port=8080`
- `kubectl expose -f deployment.yaml --port=80 --target-port=8080`
- `kubectl expose po nginx-app --port=8080 --target-port=80 --name=frontend`
- `kubectl expose svc my-svc --port=443 --target-port=8443 --name=my-svc-https`
- `kubectl expose rc my-rc --port=4100 --protocol=UDP --name=video-stream`



## Service Account

- Get service accounts: `kubectl get sa`
- Create service account: `kubectl create sa ckad-svc-act`
- Set service account for deployment:
  - `kubectl set sa deployment my-deploy ckad-svc-act`
- Dry run attaching service account with deployment:
  `kubectl set sa -f my-deploy.yaml ckad-svc-act --local --dry-run=client -o yaml`


# Others

## Create the resources

- 

## Applying the resources

- Apply resource from yaml file: `kubectl apply -f my-resource.yaml`
- Apply json passed to stdin: `cat resources/pod.yaml | kubectl apply -f -`
- Apply kustomization.yaml in directory: `kubectl apply -k my-directory/`

## Edit the resources

- Edit the resource in yaml and save modified config in its annotation:
  - `kubectl edit po nginx -o yaml --save-config`

## Delete the resources

- Delete with minimum delay and forcefully:
  - `kubectl delete po pod-name --now --force`
- Delete ALL pods: `kubectl delete po --all`
- Delete pod and services with same name "nginx":
  - `kubectl delete po,service nginx`
- Delete pod and services with names "nginx-app" and "nginx-pod":
  - `kubectl delete po,service nginx-app nginx-pod`
- Delete pod and services with label as "env=test":
  - `kubectl delete po,service -l env=test`
- Delete resources from directory containing kustomization.yaml
  - `kubectl delete -k my-directory/`

## Common Resource Commands

- `kubectl get all --all-namespaces -o wide`
- `kubectl get <resource> --all-namespaces`
- `kubectl get <resource> --namespace=<namespace> | grep <text>`
- Validate command: `--dry-run=client`
