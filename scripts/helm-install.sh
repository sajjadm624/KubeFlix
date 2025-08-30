helm upgrade --install user-service ./k8s/helm/user-service -n kubeflix
helm upgrade --install auth-service ./k8s/helm/auth-service -n kubeflix
helm upgrade --install movie-service ./k8s/helm/movie-service -n kubeflix
