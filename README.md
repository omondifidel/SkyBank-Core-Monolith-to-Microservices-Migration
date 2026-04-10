SkyBank-Core: Monolith-to-Microservices Migration

🚀 Project Overview
SkyBank is a production-grade digital banking dashboard engineered to demonstrate the transition from a monolithic architecture to a Decoupled Microservices Ecosystem.


This project solves the "Scaling Inefficiency" of monoliths by separating concerns into independent containers, allowing the UI to scale via Nginx while the transactional "Brain" scales via FastAPI.


🛠 Tech Stack

Frontend: Single Page Application (SPA) built with Tailwind CSS and vanilla JavaScript.

Backend: High-performance REST API built with FastAPI (Python 3.11).

Database: Persistent storage using PostgreSQL 15.

Orchestration: Docker & Docker Compose (Kubernetes-ready).

Reverse Proxy: Nginx for service routing and security.

🏗 Key Engineering Features

Multi-Stage Docker Builds: Optimized images using python-slim to reduce attack surface and build time.

Service Discovery: Internal container networking allowing the Backend to resolve the Database via Docker DNS.

Data Persistence: Automated database initialization via init.sql scripts and volume mounting.

Decoupled Architecture: Pure JSON API communication, enabling independent frontend/backend deployment cycles.

⚙️ How to Run

This project is designed to run in GitHub Codespaces or any Docker-enabled environment.

Clone the repository:

Bash
git clone https://github.com/YOUR_USERNAME/SkyBank-Microservices.git
cd SkyBank-Microservices
Launch the Microservices:

Bash
docker-compose up --build
Access the Dashboard:

Frontend: http://localhost:80 (or the provided Codespace URL)

Backend API Docs: http://localhost:8000/docs

