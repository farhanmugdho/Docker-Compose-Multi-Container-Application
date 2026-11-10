
# Docker Multi-Container Application – Setup Guide

## 1. Prerequisites

Install the following:

- Docker Desktop
- Git
- Windows PowerShell

Make sure Docker Desktop is running before executing Docker commands.

## 2. Navigate to the Project Directory

Open PowerShell and run:

```powershell
cd "$HOME\Desktop\docker-multi-container-extracted\docker-multi-container"
```

it depends on the pc, in my windows, this command worked

## 3. Check Project Files

```powershell
dir -Force
```

Expected project structure:

```text
docker-multi-container/
├── backend/
├── frontend/
├── docs/
├── screenshots/
├── scripts/
├── .env
├── .env.example
├── .gitignore
├── compose.yaml
└── README.md
```

## 4. Configure Environment Variables

Create the `.env` file from the example if it does not already exist:

```powershell
if (!(Test-Path .env)) {
    Copy-Item .env.example .env
}
```

Open the environment file:

```powershell
notepad .env
```

Configure your own passwords and required environment variables.

**Security:** Never commit your `.env` file or database passwords to GitHub. Commit `.env.example` with placeholder values instead.

## 5. Verify Docker Installation

Check Docker version:

```powershell
docker --version
```

Check Docker Compose version:

```powershell
docker compose version
```

Check Docker Engine connection:

```powershell
docker version
```

## 6. Build and Start Containers

Build images and start all services:

```powershell
docker compose up -d --build
```

This command builds and starts:

- Frontend (Nginx)
- Backend (Python/Gunicorn)
- Database (PostgreSQL)

## 7. Check Running Containers

```powershell
docker compose ps
```

Expected services:

| Container | Service |
|---|---|
| app-frontend | Frontend |
| app-backend | Backend |
| app-db | PostgreSQL |

## 8. View Container Logs (optional)

View all logs:

```powershell
docker compose logs
```

View the last 100 lines:

```powershell
docker compose logs --tail=100
```

Follow live logs:

```powershell
docker compose logs -f
```

Press `Ctrl + C` to stop viewing logs. Containers will continue running.

View logs for individual services:

```powershell
docker compose logs frontend
docker compose logs backend
docker compose logs db
```

## 9. Access the Application

**Frontend:**

[http://localhost:8080](http://localhost:8080)

**Backend:**

```text
Internal Docker address: http://backend:5000
```

The backend and database ports are not currently published to the Windows host.

## 10. Restart Containers 

Restart all services:

```powershell
docker compose restart
```

Restart an individual service:

```powershell
docker compose restart frontend
docker compose restart backend
docker compose restart db
```

## 11. Stop Containers

Stop all running services:

```powershell
docker compose stop
```

Start stopped services again:

```powershell
docker compose start
```

Stop and remove containers and networks:

```powershell
docker compose down
```

**Note:** `docker compose down` preserves the database volume by default.

## 12. Rebuild Containers

Rebuild and restart all services:

```powershell
docker compose up -d --build
```

## 13. Check Docker Resources

List running containers:

```powershell
docker ps
```

List all containers:

```powershell
docker ps -a
```

List Docker images:

```powershell
docker images
```

List Docker volumes:

```powershell
docker volume ls
```

## 14. Application URL

Once all containers are running successfully, open:

**http://localhost:8080**

---

## Project Status

Successfully built and tested using Docker Desktop and Docker Compose.

## Technologies Used

- Docker
- Docker Compose
- Python 3.12
- Gunicorn
- Nginx
- PostgreSQL 16
