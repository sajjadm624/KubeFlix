#!/bin/bash

# Kill any existing port-forward processes (optional safety step)
pkill -f "kubectl port-forward" 2>/dev/null

# Forward ports with individual logs
nohup kubectl port-forward svc/user-service-user-service -n kubeflix 5000:5000 > ./scripts/port-forward-user.log 2>&1 &
nohup kubectl port-forward svc/auth-service-auth-svc -n kubeflix 5001:80 > ./scripts/port-forward-auth.log 2>&1 &
nohup kubectl port-forward svc/movie-service-movie-svc -n kubeflix 5002:5002 > ./scripts/port-forward-movie.log 2>&1 &

echo "✅ YoHoHoHo, The app is running!!! Just Browse:"
echo "http://127.0.0.1:5000/ (user-service)"
echo "http://127.0.0.1:5001/ (auth-service)"
echo "http://127.0.0.1:5002/ (movie-service)"
