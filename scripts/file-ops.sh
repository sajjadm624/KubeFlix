#!/bin/bash

# Define the base directory
BASE_DIR="user-service"

# Create the necessary directories
mkdir -p "$BASE_DIR/templates"

# Create the essential files
touch "$BASE_DIR/Chart.yaml" "$BASE_DIR/values.yaml"
touch "$BASE_DIR/templates/deployment.yaml" "$BASE_DIR/templates/service.yaml" "$BASE_DIR/templates/_helpers.tpl"

# Output the directory structure
echo "Created the following structure:"
tree "$BASE_DIR"