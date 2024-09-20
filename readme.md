- [🌟 Certified Kubernetes Application Developer (CKAD) 🌟](#-certified-kubernetes-application-developer-ckad-)
  - [📚 Resources](#-resources)
  - [🎁 Special Offer](#-special-offer)
- [Important links](#important-links)
- [Cosign](#cosign)
- [regctl](#regctl)
- [Kubernetes Commands and Explanations](#kubernetes-commands-and-explanations)
  - [Node Workers](#node-workers)
- [Command docker](#command-docker)
    - [inspect the user](#inspect-the-user)
- [Commands](#commands)
    - [check running proses](#check-running-proses)
    - [Docker commands](#docker-commands)
    - [add secret fully as env](#add-secret-fully-as-env)
    - [Create inline secrets](#create-inline-secrets)
    - [Get Cluster Info](#get-cluster-info)
    - [create a pod and expose it with given port using one command](#create-a-pod-and-expose-it-with-given-port-using-one-command)
    - [Run a Pod](#run-a-pod)
    - [Create a Pod from YAML](#create-a-pod-from-yaml)
    - [Generate YAML Templates](#generate-yaml-templates)
    - [Create yaml from existing object](#create-yaml-from-existing-object)
    - [Explain a Specific Keyword in Definition File](#explain-a-specific-keyword-in-definition-file)
    - [Extract Pod Definition to File](#extract-pod-definition-to-file)
          - [For more details, refer:](#for-more-details-refer)
    - [Edit Pod Properties](#edit-pod-properties)
    - [Validate Yamls](#validate-yamls)
    - [scale up/dow replica sets on the fly](#scale-updow-replica-sets-on-the-fly)
    - [Create namespace](#create-namespace)
    - [delete namespace](#delete-namespace)
      - [Set default namespace](#set-default-namespace)
    - [view resource Quota usage](#view-resource-quota-usage)
    - [Accessing resource in another namespace](#accessing-resource-in-another-namespace)
    - [switch to a namespace permanently](#switch-to-a-namespace-permanently)
    - [Services](#services)
    - [create symbolic link](#create-symbolic-link)
- [Explanations](#explanations)
  - [Service accounts](#service-accounts)
  - [set pod security container level](#set-pod-security-container-level)
    - [Examples Replica-set](#examples-replica-set)
- [Kubernetes Deployments](#kubernetes-deployments)
  - [Overview](#overview)
  - [Key Concepts](#key-concepts)
  - [Deployment YAML Example](#deployment-yaml-example)
- [Kubernetes Namespaces](#kubernetes-namespaces)
  - [Overview](#overview-1)
  - [Namespace YAML Example](#namespace-yaml-example)
- [Kubernetes  configMap call in a pod](#kubernetes--configmap-call-in-a-pod)
- [Kubernetes Resource Allocation](#kubernetes-resource-allocation)
  - [ResourceQuota](#resourcequota)
    - [Create a ResourceQuota](#create-a-resourcequota)
    - [Adding resource limit to pods](#adding-resource-limit-to-pods)



# 🌟 Certified Kubernetes Application Developer (CKAD) 🌟

## 📚 Resources
- **[Certified Kubernetes Application Developer](https://www.cncf.io/certification/ckad/)**: Official certification page with all the details.
- **[Candidate Handbook](https://www.cncf.io/certification/candidate-handbook)**: Comprehensive guide for exam preparation.
- **[Exam Tips](https://docs.linuxfoundation.org/tc-docs/certification/tips-cka-and-ckad)**: Essential tips to ace your exam.

## 🎁 Special Offer
**Use the code `20KLOUD` while registering for the CKA or CKAD exams at the Linux Foundation to receive a 20% discount!** 🎉

Good luck with your certification journey! 🚀

# Important links
```bash
https://github.com/tektoncd/pipeline/blob/main/docs/auth.md#unsuccessful-cred-copy-warning
https://github.com/tektoncd/experimental/blob/f60e1cd8ce22ed745e335f6f547bb9a44580dc7c/pipeline-in-pod/OWNERS
```
# Cosign
```bash
https://edu.chainguard.dev/open-source/sigstore/cosign/an-introduction-to-cosign/
```
# regctl
```bash
export DOCKER_CONFIG=/mnt/c/Data/pi-2024/temp/dockerconf
# this will refer docker config
regctl image  digest crnxscicdmvp001.azurecr.io/nexus/health:0.1.2

```

# Kubernetes Commands and Explanations

## Node Workers
- **Node Workers**: Physical VM or server in the Kubernetes cluster.

---
# Command docker
### inspect the user
```bash
docker inspect nginx --format='{{.Config.User}}'
```
# Commands
### check running proses
```bash
ps aux
```
### Docker commands
```bash
# run ubuntu image and exit
docker run ubuntu
# list running containers
docker ps
# list all containers
docker ps -a
# override commands in image
docker run -it ubuntu /bin/bash

docker run  <image name build with sleep> sleep 5

Note:
CMD sleep 5 where runtime we will override full command
ENTRYPOINT["sleep"] runtime we can append to the command like time to sleep
combine both to get default sleep value
ENTRYPOINT["sleep"]
CMD["5"]
override entrypoint at runtime
docker run --entrypoint sleep 2.0 ubuntu-sleeper 10

```
### add secret fully as env
```bash
spec:
  containers:
  - name: webapp-container
    image: webapp-image
    envFrom:
    - secretRef:
        name: webapp-secret
```
### Create inline secrets
```bash
kubectl create secret generic \
     db-secret --from-literal=DB_Host=aasww \
               --from-literal=DB_User=asdasd \
               --from-literal=DB_Password=cGFzc3dvcmQxMjM=
```
### Get Cluster Info
```bash
kubectl cluster-info
kubectl get nodes
```
### create a pod and expose it with given port using one command
```bash
kubectl run httpd --image httpd:alpine --expose=true --port 80
```
### Run a Pod
```bash
kubectl run nginx --image=nginx
kubectl get pods
```
### Create a Pod from YAML
```bash
kubectl create -f <yaml pod or deployment>
```
### Generate YAML Templates
```bash
kubectl run my-pod --image=nginx --dry-run=client -o yaml
```
```bash
kubectl create deployment nginx-deployment --image=nginx --dry-run=client -o yaml > nginx-deployment.yaml

```
### Create yaml from existing object
```bash
kubectl get <object-type> <object-name> -o yaml > <output-file>.yaml
```
### Explain a Specific Keyword in Definition File
```bash
kubectl explain pod.spec.containers.image
kubectl explain pod.spec.containers  --recursive
```
### Extract Pod Definition to File
```bash
kubectl get pod <pod-name> -o yaml > pod-definition.yaml
```
Options:
- **`-o json`**: Makes the output JSON-formatted.
- **`-o name`**: Displays only the name of the resource.
- **`-o wide`**: Provides additional information in a plain-text format.
- **`-o yaml`**: Formats the output in YAML.

###### For more details, refer:

https://kubernetes.io/docs/reference/kubectl/overview/

https://kubernetes.io/docs/reference/kubectl/cheatsheet/

### Edit Pod Properties
```bash
kubectl edit pod <pod-name>
```
### Validate Yamls
```bash
 kubectl apply -f replicaset-definition-1.yaml --dry-run=client
```
### scale up/dow replica sets on the fly
```bash
 kubectl scale --replicas=5 rs/new-replica-set
 or
 kubectl edit replicaset
rs/<name of the replica set>
```
### Create namespace
```bash
kubectl create namespace <namespace-name>
```

### delete namespace
```bash
kubectl delete namespace <namespace-name>

```
#### Set default namespace
```bash
kubectl config get-contexts
kubectl config use-context context-2
kubectl config set-context --current --namespace=<namespace-name>



```

### view resource Quota usage
```bash
kubectl describe resourcequota my-resource-quota -n my-namespace
```

### Accessing resource in another namespace
```bash
service create DNS will get add to it
db-service.dev.svc.cluster.local
cluster.local= default domain name
svc = subdomain for servic
dev = namespace
db-service= service name
```
### switch to a namespace permanently
```bash
  kubectl config set-context $(kubectl config current-context) --namespace=dev
```

### Services
```bash
kubectl expose pod redis --port=6379 --name redis-service --dry-run=client -o yaml

Create a Service named nginx of type NodePort to expose pod nginx's port 80 on port 30080 on the nodes:

kubectl expose pod nginx --port=80 --name nginx-service --type=NodePort --dry-run=client -o yaml

(This will automatically use the pod's labels as selectors, but you cannot specify the node port. You have to generate a definition file and then add the node port in manually before creating the service with the pod.)

```
### create symbolic link
```bash
sudo ln -s $(which kubectl) /usr/local/bin/k
```
# Explanations
## Service accounts
```bash
kubectl create serviceaccount <service account name>
```
```yaml
Note :
Service account token use external app to work with apis ect.
but new version this token not create auto and also now having expiration time to it token is a secret
if app in k8 cluster
use mount the secret as a volume

  containers:
   serviceAccountName: dashboard-sa < to use service account >
   automountServiceAccountToken: false < disable the mount >
   decode token
   jq -R 'split(".") | select(length > 0) | .[0],.[1] | @base64d | fromjson' <<< <token>
 for new version secret not mount directly now it is projected volume
   volumes:
    projected:
      sources:
      - serviceAccountToken:
            expirationSeconds: 456
            path: token
                   - key:

v1.24 <no longer create token>
  kubectl create token <sa>



```



## set pod security container level
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ubuntu-sleeper
  namespace: default
  resourceVersion: "840"
  uid: 9d465e6f-0f5a-4f61-991a-bf75e4eb98cc
spec:
  containers:
  - command:
    - sleep
    - "4800"
    image: ubuntu
    securityContext:
     runAsUser: 1010
     capabilities:
      add : [SYS_TIME]
    imagePullPolicy: Always
    ```


## Kubernetes Pod Controllers

Pod Controllers are responsible for managing the lifecycle and scaling of Pods in a Kubernetes cluster. They ensure that the desired number of Pods is running and handle various tasks like scaling, updating, and rolling back Pods.

## Types of Pod Controllers

### 1. ReplicaSet

- **Purpose**: Ensures that a specified number of Pod replicas are running at any given time.
- **Usage**: Commonly used by Deployments to maintain the desired state of Pods.
- **Key Commands**:
```bash
  kubectl get replicasets
  kubectl describe replicasets <replicaset-name>
  kubectl delete replicasets <replicaset-name>
  kubectl create replicaset <replicaset-name> --image=<container-image> --replicas=<
```
### Examples Replica-set

Here's an example of a ReplicaSet YAML configuration:

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: my-app-replicaset
  labels:
    app: my-app-replicaset
spec:
  template:
    metadata:
      name: my-pod
      labels:
        app: my-app
    spec:
      containers:
        - name: my-container
          image: nginx
  replicas: 3
  selector:
    matchLabels:
      app: my-app
```


# Kubernetes Deployments

## Overview

A **Deployment** in Kubernetes is a controller that manages the deployment and scaling of a set of Pods. It ensures that the desired number of Pods are running and provides capabilities for rolling updates, rollbacks, and scaling.

## Key Concepts

- **ReplicaSet**: A Deployment manages one or more ReplicaSets, which in turn manage the Pods.
- **Rolling Updates**: Deployments allow for zero-downtime deployments by gradually updating Pods with new versions.
- **Rollbacks**: If something goes wrong with a new deployment, you can roll back to a previous stable version.
- **Scaling**: You can scale the number of Pods up or down as needed.

## Deployment YAML Example

Here’s an example of a Kubernetes Deployment YAML configuration:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-deployment
  labels:
    app: my-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
        - name: my-container
          image: nginx
          ports:
            - containerPort: 80

```


# Kubernetes Namespaces

## Overview

In Kubernetes, a **Namespace** is a way to divide cluster resources between multiple users or teams. Namespaces help manage and organize resources in a large cluster, providing a scope for names and enabling resource isolation. They are useful for:

- **Organizing Resources**: Grouping related resources together.
- **Resource Isolation**: Limiting access to resources within a namespace.
- **Quotas and Limits**: Applying resource quotas and limits on a per-namespace basis.
- **Access Control**: Implementing role-based access control (RBAC) policies specific to namespaces.

## Namespace YAML Example
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: my-namespace
  labels:
    name: my-namespace

```
# Kubernetes  configMap call in a pod
```yaml
spec:
  containers:
  - env:
    - name: APP_COLOR
      valueFrom:
            configMapKeyRef:
                name: webapp-config-map
                key: APP_COLOR
```
# Kubernetes Resource Allocation

## ResourceQuota

A `ResourceQuota` is used to limit the amount of resources that can be consumed by a namespace. It helps to ensure fair usage of cluster resources and prevents any single namespace from using more than its allocated share.

### Create a ResourceQuota

To create a `ResourceQuota`, you need to define it in a YAML file. Below is an example YAML configuration:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: my-resource-quota
  namespace: my-namespace
spec:
  hard:
    cpu: "4"
    memory: 16Gi
    pods: "10"
    services: "5"
    persistentvolumeclaims: "10"
```
### Adding resource limit to pods
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: my-namespace
spec:
  containers:
    - name: my-container
      image: nginx
      resources:
        requests:
          memory: "512Mi"
          cpu: "500m"
        limits:
          memory: "1Gi"
          cpu: "1000m"
```