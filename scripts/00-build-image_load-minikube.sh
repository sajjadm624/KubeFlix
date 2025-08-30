#!/bin/bash

images=(
  "movie-service:latest ./apps/movie-service"
  "auth-service:latest ./apps/auth-service"
  "user-service:latest ./apps/user-service"
)

eval $(minikube -p minikube docker-env)

# Iterate over each image configuration
for image in "${images[@]}"; do
  # Split the image configuration into name and directory
  image_name=$(echo "$image" | awk '{print $1}')
  docker_dir=$(echo "$image" | awk '{print $2}')

  echo "Building image: $image_name from directory: $docker_dir"

  # Build the Docker image
  docker build -t "$image_name" "$docker_dir" || {echo "Failed to build image: $image_name" exit 1}

done

exit 1

#Load in minikube

minikube image load movie-service:latest
minikube image load auth-service:latest
minikube image load user-service:latest

docker images
