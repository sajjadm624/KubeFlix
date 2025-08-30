helm upgrade user-service ./k8s/helm/user-service -n kubeflix
helm upgrade auth-service ./k8s/helm/auth-service -n kubeflix
helm upgrade movie-service ./k8s/helm/movie-service -n kubeflix
