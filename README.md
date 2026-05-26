# K8s GitOps Platform

## Architecture

Code Push -> GitHub Actions -> DockerHub -> ArgoCD -> Kubernetes -> Grafana

## Tech Stack

- Kubernetes (KIND)
- ArgoCD GitOps
- GitHub Actions CI/CD
- Docker + DockerHub
- Grafana + Prometheus
- Python Flask + Nginx

## Quick Start

kind create cluster --config kind-cluster.yaml
kubectl apply -f k8s/
kubectl port-forward svc/frontend-service 3000:80 -n dashboard
