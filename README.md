# KubeFlix Deployment Guide

This repository provides the setup and deployment for **KubeFlix**, a Kubernetes-based Netflix clone built with microservices. This guide outlines the steps to build, deploy, and manage the application on a local Kubernetes cluster (Minikube) or a kind cluster.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

- **Minikube** running a local Kubernetes cluster
- **Docker** CLI to build and load images
- **Helm** to manage Kubernetes deployments
- **kubectl** to interact with the Kubernetes cluster
- A Kubernetes namespace `kubeflix` (can be created using `kubectl create ns kubeflix`)

## Getting Started

These steps will guide you through deploying the KubeFlix application on your local Kubernetes cluster. 

1. **Stop any existing port-forwarding sessions**: Run the following script to kill any active `kubectl port-forward` processes that could interfere with your current session:
    ```bash
    bash ./scripts/down-kubeflix.sh
    ```
    This ensures there are no conflicts when setting up the new session.

2. **Clean up previous Kubernetes resources**: To ensure a clean slate, use this script to delete all existing deployments and services in the `kubeflix` namespace and clean up Docker images:
    ```bash
    bash ./scripts/destroy.sh
    ```
    Clears the slate for a fresh start.

3. **Build Docker images and load them into Minikube**: This script will build the Docker images for the `user-service`, `auth-service`, and `movie-service` from their respective directories and load them into the Minikube registry:
    ```bash
    bash ./scripts/00-build-image_load-minikube.sh
    ```
    Ensures that your custom Docker images are available within your Kubernetes environment.

4. **Deploy services to Kubernetes using Helm**: Next, deploy the services (`user-service`, `auth-service`, `movie-service`) using Helm:
    ```bash
    bash ./scripts/helm-install.sh
    ```
    This will install or upgrade the services in the `kubeflix` namespace, setting up their respective deployments, services, and configurations.

5. **Start port forwarding for local access**: Use this script to forward the necessary ports, allowing you to access the services locally:
    ```bash
    bash ./scripts/launch-kubeflix.sh
    ```
    After running this, you can access the following services locally:
    - `http://127.0.0.1:5000` → `user-service`
    - `http://127.0.0.1:5001` → `auth-service`
    - `http://127.0.0.1:5002` → `movie-service`

## Health Checks

Each service includes **liveness** and **readiness** probes, ensuring:
- **Liveness probes** restart the service if it becomes unhealthy.
- **Readiness probes** ensure traffic is only routed to services that are fully initialized and ready to handle requests.

These probes are configured via Helm templates and will be checked by Kubernetes regularly.

6. **Full Rebuild (for Development or Quick Reset)**: For a fresh start (rebuild all images and redeploy), use this combined script:
    ```bash
    bash ./scripts/down-destroy-build-load-helm-launch.sh
    ```
    This will:
    - Stop any existing port-forwarding
    - Destroy Kubernetes resources
    - Rebuild and load Docker images
    - Redeploy the Helm charts
    - Restart port-forwarding

7. **Upgrade Helm releases without rebuilding images**: If you've made changes to the Helm charts and want to apply them without rebuilding the Docker images, run:
    ```bash
    bash ./scripts/helm-upgrade.sh
    ```
    This will upgrade the existing services to reflect any Helm chart changes.

8. **Load Docker images to a kind cluster (Optional)**: If you're using a **kind** cluster instead of Minikube, use the following script to load your Docker images into the kind cluster:
    ```bash
    bash ./scripts/load_kind.sh
    ```

## Conclusion

Once all the steps are complete, your **KubeFlix** application will be up and running on your local Kubernetes environment. You can access the services locally, monitor their health, and interact with the application through the exposed ports.

Enjoy testing and extending your KubeFlix project!

## Additional Notes

- **Helm charts** are configured to deploy the services with the required Kubernetes resources, including deployments, services, and probes.
- **Port-forwarding** is used to expose the services locally for development and testing.
- If you wish to deploy this setup in a cloud environment or a production-grade cluster, additional configurations (e.g., ingress controllers, persistent volumes) may be required.
