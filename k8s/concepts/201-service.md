Service
---

Creating a service for Pod
---

- `kubectl run nginx --image=nginx:stable`
- `kubectl create svc my-service `

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
  labels:
    app.kubernetes.io/name: proxy
spec:
  containers:
  - name: nginx
    image: nginx:stable
    ports:
      - containerPort: 80
        name: http-web-svc
      - containerPort: 443
        name: https-web-svc

---
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  selector:
    app.kubernetes.io/name: proxy
  ports:
  - name: name-of-service-port
    protocol: TCP
    port: 80
    targetPort: http-web-svc
  - name: https
      protocol: TCP
      port: 443
      targetPort: https-web-svc
```

# Service Types

## ClusterIP

- Default service that exposes the Service on a cluster-internal IP.
- Service `only reachable from within the cluster`.
- You can expose the Service to `public internet using an Ingress or a Gateway`.

## NodePort

- Exposes the Service on each `Node's IP at a static port` (the NodePort).
- To make the node port available, Kubernetes sets up a cluster IP address, the same as if you had requested a Service of type: ClusterIP.

  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: my-service
  spec:
    type: NodePort
    selector:
      app.kubernetes.io/name: MyApp
    ports:
      - port: 80
        # By default and for convenience, the `targetPort` is set to
        # the same value as the `port` field.
        targetPort: 80
        # Optional field
        # By default and for convenience, the Kubernetes control plane
        # will allocate a port from a range (default: 30000-32767)
        nodePort: 30007
  ```

## LoadBalancer

- Exposes the Service `externally using an external load balancer`.
- Kubernetes does not directly offer a load balancing component; you must provide one, or you can integrate your Kubernetes cluster with a cloud provider.

  ```yaml
  apiVersion: v1
  kind: Service
  metadata:
    name: my-service
  spec:
    selector:
      app.kubernetes.io/name: MyApp
    ports:
      - protocol: TCP
        port: 80
        targetPort: 9376
    clusterIP: 10.0.171.239
    type: LoadBalancer
  status:
    loadBalancer:
      ingress:
      - ip: 192.0.2.127
  ```

## ExternalName

- Maps the Service to the contents of the externalName field (for example, to the hostname api.foo.bar.example).
- The mapping configures your cluster's DNS server to return a CNAME record with that external hostname value. No proxying of any kind is set up.

