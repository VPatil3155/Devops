Write-Host "Starting Kubernetes Automation..."

# Step 1: Start Minikube
minikube start --driver=docker

# Step 2: Build Docker Image
docker build -t auto-k8s-app .

# Step 3: Load Image into Minikube
minikube image load auto-k8s-app

# Step 4: Deploy to Kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Step 5: Wait for pods
Start-Sleep -Seconds 10

# Step 6: Show status
kubectl get pods
kubectl get services

# Step 7: Open application
minikube service auto-service

Write-Host "Deployment Completed!"