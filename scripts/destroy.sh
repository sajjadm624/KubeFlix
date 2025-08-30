#!/bin/bash

kubectl delete deployments --all -n kubeflix

kubectl delete svc --all -n kubeflix

docker system prune -a
