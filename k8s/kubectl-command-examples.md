# KubeCtl Command Examples

`kubectl run hello-minikube`
`kubectl cluster-info`
`kubectl get nodes`


`kubectl create -f deployment-definition.yml`
`kubectl get deployments`
`kubectl apply -f deployment-definition.yml`
`kubectl set image deployment/myapp-deployment nginx=nginx:1.7.3`
`kubectl rollout status deployment/myapp-deployment`
`kubectl rollout history deployment/myapp-deployment`
`kubectl rollout undo deployment/myapp-deployment`
