
# Docker Multi-Container Application

A multi-container application powered by Docker Compose, featuring a Python backend, Nginx frontend, and PostgreSQL database.

## Project Overview

This project uses Docker Compose to build and run three services:

- Frontend: Nginx
- Backend: Python 3.12 with Gunicorn
- Database: PostgreSQL 16

All services run inside Docker containers and communicate through Docker networks.

## Technologies Used

- Docker
- Docker Desktop
- Docker Compose
- Python 3.12
- Gunicorn
- Nginx
- PostgreSQL 16
- PowerShell

## Project Structure

```text
docker-multi-container/
│
├── backend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   └── nginx.conf
│
├── docs/
├── screenshots/
├── scripts/
│
├── .env.example
├── .gitignore
├── compose.yaml
└── README.md
```

## Prerequisites

Before starting, install:

1. Docker Desktop
2. Git
3. Windows PowerShell

Make sure Docker Desktop is running before executing Docker commands.

## Installation and Setup

### Step 1: Clone the Repository

```powershell
git clone YOUR_GITHUB_REPOSITORY_URL
```

Navigate into the project directory:

```powershell
cd docker-multi-container
```

### Step 2: Configure Environment Variables

Create your `.env` file:

```powershell
Copy-Item .env.example .env
```

Open the environment file:

```powershell
notepad .env
```

Configure your own passwords and environment variables.

**Important:** Never upload your `.env` file or passwords to GitHub.

### Step 3: Verify Docker Installation

Check Docker version:

```powershell
docker --version
```

Check Docker Compose:

```powershell
docker compose version
```

Check Docker Engine:

```powershell
docker version
```

### Step 4: Build and Start Containers

Run:

```powershell
docker compose up -d --build
```

This command builds the application images and starts all containers in detached mode.

### Step 5: Check Container Status

```powershell
docker compose ps
```

Expected containers:

| Container | Service |
|---|---|
| app-frontend | Frontend |
| app-backend | Backend |
| app-db | PostgreSQL |

### Step 6: Access the Application

Open your browser:

**Frontend:**

http://localhost:8080

**Backend:**

The backend listens internally on port 5000.

**Database:**

PostgreSQL listens internally on port 5432.

The backend and database ports are not published to the Windows host in the current configuration.

## Useful Docker Commands

### View Running Containers

```powershell
docker ps
```

### View All Containers

```powershell
docker ps -a
```

### View Docker Images

```powershell
docker images
```

### View Container Logs

```powershell
docker compose logs
```

### View Last 100 Lines

```powershell
docker compose logs --tail=100
```

### Follow Live Logs

```powershell
docker compose logs -f
```

Press `Ctrl + C` to stop viewing logs.

### View Individual Service Logs

```powershell
docker compose logs frontend
docker compose logs backend
docker compose logs db
```

### Restart All Services

```powershell
docker compose restart
```

### Restart Individual Services

```powershell
docker compose restart frontend
docker compose restart backend
docker compose restart db
```

### Stop All Containers

```powershell
docker compose stop
```

### Start Stopped Containers

```powershell
docker compose start
```

### Stop and Remove Containers

```powershell
docker compose down
```

This preserves the database volume.

### Rebuild and Restart Everything

```powershell
docker compose up -d --build
```

## Troubleshooting

### Problem 1: Docker Engine Is Not Running

Error:

```text
failed to connect to the docker API
```

Solution:

1. Open Docker Desktop.
2. Wait for Docker Engine to start.
3. Run:

```powershell
docker version
```

### Problem 2: No Configuration File Provided

Error:

```text
no configuration file provided: not found
```

Solution:

Navigate to the directory containing `compose.yaml`:

```powershell
cd path\to\docker-multi-container
```

### Problem 3: Environment File Not Found

Error:

```text
.env.example does not exist
```

Solution:

Check your current directory:

```powershell
dir -Force
```

Navigate to the actual project folder before creating `.env`.

### Problem 4: Check Container Health

```powershell
docker compose ps
```

View logs:

```powershell
docker compose logs --tail=100
```

## Security Notes

- Never commit `.env` to GitHub.
- Use strong database passwords.
- Keep `.env.example` free of real credentials.
- Do not expose database ports publicly without proper security.
- Keep Docker Desktop updated.

## Upload Project to GitHub

Check Git status:

```powershell
git status
```

Add project files:

```powershell
git add .
```

Commit changes:

```powershell
git commit -m "Add Docker multi-container application"
```

Push to GitHub:

```powershell
git push origin main
```

Make sure `.env` is excluded through `.gitignore` before pushing.

## Current Project Status

The application has been successfully built and started using Docker Compose.

| Component | Technology | Status |
|---|---|---|
| Frontend | Nginx | Running |
| Backend | Python / Gunicorn | Healthy |
| Database | PostgreSQL 16 | Healthy |

## Application URL

http://localhost:8080

## Author

Your Name

GitHub: https://github.com/your-username

