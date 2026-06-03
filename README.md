# ☸️ K8s GitOps Platform — Cluster Dashboard

> A complete cloud-native platform demonstrating end-to-end GitOps. A full-stack Kubernetes cluster dashboard (Flask backend + HTML/Nginx frontend) is containerized, pushed to Docker Hub via GitHub Actions, and deployed to a Kubernetes cluster — visualizing live cluster stats like nodes, pods, and deployments.

![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![ArgoCD](https://img.shields.io/badge/Argo_CD-EF7B4D?style=flat&logo=argo&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)

## 📋 Overview

This project demonstrates how modern teams ship software: code is pushed to Git, automatically built into container images, and deployed to Kubernetes. The deployed app is a **cluster dashboard** that displays live Kubernetes metrics — node count, pod status, and deployments — through a clean web UI served by a Flask backend.

## 🧩 Architecture

```
Code Push → GitHub Actions → Docker Hub → ArgoCD → Kubernetes (KIND) → Grafana
   commit       build & push     registry     sync       run workloads    monitor
```

## 🛠️ Tech Stack

- **Orchestration:** Kubernetes (KIND)
- **GitOps / CD:** ArgoCD
- **CI:** GitHub Actions
- **Containerization:** Docker + Docker Hub
- **Monitoring:** Grafana + Prometheus
- **Backend:** Python Flask
- **Frontend:** HTML / Nginx

## 📁 Project Structure

```
gitops-project/
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # CI: builds & pushes backend + frontend images
├── backend/
│   ├── app.py                     # Flask backend (cluster stats API)
│   ├── requirements.txt           # Python dependencies
│   └── Dockerfile                 # Backend container image
├── frontend/
│   ├── index.html                 # Dashboard UI
│   └── Dockerfile                 # Nginx container image
├── k8s/
│   ├── namespace.yaml             # Dedicated namespace
│   ├── backend-deployment.yaml    # Backend deployment + service
│   ├── frontend-deployment.yaml   # Frontend deployment + service
│   └── rbac.yaml                  # Role-Based Access Control
├── write_html.py                  # Generates the frontend dashboard HTML
└── README.md
```

## ⚙️ CI/CD Pipeline

On every push to `main` (`.github/workflows/ci-cd.yml`):

1. **Checkout code**
2. **Login to Docker Hub** (authenticated via GitHub Secrets)
3. **Build & push backend image** → `k8s-dashboard-backend:latest`
4. **Build & push frontend image** → `k8s-dashboard-frontend:latest`

ArgoCD then detects the updated manifests in Git and syncs them to the cluster automatically.

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/isuruchathushka724-dev/gitops-project
cd gitops-project

# Create a local Kubernetes cluster
kind create cluster

# Apply the Kubernetes manifests
kubectl apply -f k8s/

# Access the dashboard
kubectl port-forward svc/frontend-service 3000:80 -n dashboard
```

Then open `http://localhost:3000` to view the cluster dashboard.

## 🔐 Best Practices Used

- **GitOps workflow** — Git as the single source of truth for deployments
- **RBAC** configured for least-privilege access control
- **Dedicated namespace** for clean resource isolation
- **Secrets** stored in GitHub Secrets — never hardcoded
- **Separate CI stages** for backend and frontend images

## 🔐 Required Secrets

| Secret            | Description             |
| ----------------- | ----------------------- |
| `DOCKERHUB_TOKEN` | Docker Hub access token |

## 👨‍💻 Author

**Isuru Chathushka** — Undergraduate @ Horizon Campus LK
🔗 [LinkedIn](https://www.linkedin.com/in/isuru-chathushka)
