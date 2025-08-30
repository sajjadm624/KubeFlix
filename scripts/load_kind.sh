#!/bin/bash

# Save Docker images to tarballs
docker save movie-service:latest -o movie-service.tar
docker save auth-service:latest -o auth-service.tar
docker save user-service:latest -o user-service.tar

# Load tarballs into kind cluster
kind load image-archive --name kind movie-service.tar
kind load image-archive --name kind auth-service.tar
kind load image-archive --name kind user-service.tar

# Optional: Clean up
rm movie-service.tar auth-service.tar user-service.tar

# Show Docker images
docker images

