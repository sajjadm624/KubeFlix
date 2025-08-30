# KubeFlix: Kubernetes Netflix Clone

**KubeFlix** is a microservices-based Netflix clone built with FastAPI and deployed on Kubernetes using Helm. This project demonstrates building, deploying, and managing multiple microservices on a local Kubernetes cluster (Minikube) with full CI/CD-ready deployment practices.

---

## Project Overview

KubeFlix consists of **three main microservices**:

| Service       | Port | Description                                      |
|---------------|------|--------------------------------------------------|
| `user-service`| 5000 | Manages users and user data                      |
| `auth-service`| 5001 | Provides authentication and JWT-based security |
| `movie-service`| 5002 | Manages movie data and search/recommendations  |

All services are deployed as Kubernetes pods, managed via Helm charts, and include **liveness** and **readiness** probes.

---

## Architecture

         +----------------+
         |  Minikube /    |
         |  Kubernetes    |
         +----------------+
           |       |       |
           |       |       |
     +-----v--+ +--v-----+ +------v------+
     |user-svc| |auth-svc| |movie-svc    |
     +--------+ +--------+ +-------------+
         |          |            |
    REST APIs   JWT Auth      Movie APIs


- Each microservice runs in its own Kubernetes deployment.
- Communication between services is via REST.
- JWT tokens from `auth-service` secure protected routes.

---

## Helm Charts

Each service has a dedicated Helm chart:

| Chart             | Namespace | Replicas | Service Type |
|------------------|-----------|----------|--------------|
| `user-service`    | kubeflix  | 2        | ClusterIP    |
| `auth-service`    | kubeflix  | 2        | ClusterIP    |
| `movie-service`   | kubeflix  | 2        | ClusterIP    |

The charts include:
- Deployments with configurable replicas
- Services with ClusterIP type
- Liveness and readiness probes
- Resource requests and limits
- Environment variable support

---

## Prerequisites

- **Minikube** (or Kind cluster)
- **Docker** CLI
- **Helm**
- **kubectl**
- Kubernetes namespace `kubeflix`:

```bash kubectl create ns kubeflix


## Deployment Steps

- Stop existing port-forwarding:
   bash ./scripts/down-kubeflix.sh 

- Clean previous deployments:
   bash ./scripts/destroy.sh

- Build Docker images and load to Minikube:
   bash ./scripts/00-build-image_load-minikube.sh

- Deploy services using Helm:
   bash ./scripts/helm-install.sh

- Start port-forwarding for local access:
   bash ./scripts/launch-kubeflix.sh
```

## Access services locally:

- http://127.0.0.1:5000 → user-service

- http://127.0.0.1:5001 → auth-service

- http://127.0.0.1:5002 → movie-service