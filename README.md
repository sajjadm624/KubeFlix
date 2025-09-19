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

## CI/CD Progress (GitHub Actions)

The GitHub Actions pipeline is being integrated for automated Docker build, test, and deployment:

**Pipeline Plan:**

1. Setup GH Actions workflow skeleton ✅
2. Build pipeline: Docker build + push ✅
3. Test pipeline locally (cache & build) ✅
4. Connect pipeline to Minikube images ⚠️ (in progress)
5. Debug pipeline + push images ⚠️ (in progress)
6. Confirm pipeline success ⚠️ (pending)

> Current status: Docker images are successfully built and pushed. Workflow skeleton is set up, and local tests are complete. Integration with Minikube and full automation is underway.

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

## Service Endpoints (FastAPI)

### User Service
```bash
GET /users             # List all users
GET /users/{id}        # Get user by ID
POST /users            # Create new user
GET /health            # Liveness & readiness probe 
```

### Auth Service
```bash
POST /login            # Generate JWT token
GET /secure-data       # Access protected route with JWT
GET /health            # Liveness & readiness probe 
```

### Movie Service
```bash
GET /movies                   # List all movies
GET /movies/{id}              # Get movie by ID
GET /search?title=<title>     # Search movies by title
GET /recommendations?count=N  # Random movie recommendations
GET /genres                    # List available genres
GET /top-rated?limit=N        # Top-rated movies
POST /add-movie               # Add new movie
GET /health                   # Liveness & readiness probe
```

## Health Checks
All services implement:

    - Liveness Prob: Restarts the pod if unhealthy
    - Readiness Probe: Ensures traffic only goes to ready pods
    - Configured via Helm templates

# Full Rebuild (Dev / Reset)
bash ./scripts/down-destroy-build-load-helm-launch.sh
/# Stops port-forwarding, cleans old resources,
/# rebuilds images, deploys Helm charts, and starts forwarding
