SCRIPTS_DIR="./scripts"

bash $SCRIPTS_DIR/down-kubeflix.sh
echo "Kubflixe is DOWN!"

bash $SCRIPTS_DIR/destroy.sh
echo "Kubeflix is Destroyed! YoHoHoHo!"

bash $SCRIPTS_DIR/00-build-image_load-minikube.sh
echo "Built Images for Kubeflix then load it to minikube."

echo "Helming Kubflix!! HEHEHEHE" 
bash $SCRIPTS_DIR/helm-install.sh
echo " A L L  S E R V I C E S  D E P L O Y E D  T O  K8S C L U S T E R."

bash $SCRIPTS_DIR/launch-kubeflix.sh
