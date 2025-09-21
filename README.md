# Scheduler Microservice (Django, Django Ninja)

A scalable microservice for job scheduling and asynchronous execution, offering modern RESTful APIs, easy orchestration with Docker Compose, and auto-generated documentation.

---

## Features

- Schedule, list (with pagination), and view jobs
- Asynchronous job execution with Celery
- Persistent job storage using PostgreSQL
- Redis as Celery broker
- Full Docker Compose orchestration
- Interactive Swagger/OpenAPI docs via Django Ninja UI

---

## Tech Stack

- **Backend:** Django, Django Ninja
- **Async Tasks:** Celery, Redis
- **Database:** PostgreSQL
- **Deployment:** Docker, Docker Compose

---

## Getting Started

### 1. Clone & Configure

```
git clone git@github.com:namansingh3502/job_schedular.git
cp .env.example .env      # Adjust database/redis settings as needed
```

---

### 2. Docker Compose Up

Start all services (API, Celery worker, PostgreSQL, Redis):

```
docker-compose up --build
```

- Django/Ninja API: [http://localhost:8000](http://localhost:8000)
- API Docs (Swagger): [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

---

### 4. API Reference

| Endpoint         | Method | Description                               |
|------------------|--------|-------------------------------------------|
| `/api/jobs`      | GET    | List jobs (supports pagination)           |
| `/api/jobs`      | POST   | Create and schedule a new job             |
| `/api/jobs/{id}` | GET    | Get job details by ID                     |
| `/api/docs`      | GET    | API Documentation (Swagger UI)            |

#### Example: Create Job

```
curl -X POST "http://localhost:8000/api/jobs" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "test-job",
    "interval_seconds": 600,
    "params": {"type": "dummy"}
  }'
```

#### Example: List Jobs (with Pagination)

```
curl -G "http://localhost:8000/api/jobs" \
  --data-urlencode "limit=20" \
  --data-urlencode "offset=0"
```

#### Example: Get Job by ID

```
curl -X GET "http://localhost:8000/api/jobs/1"
```


## Customization & Scaling

- Scale horizontally: increase replicas of `web` or `celery`; use a reverse proxy/load balancer for production.
- Adjust environment variables in `.env` to customize DB, Redis, or Celery settings.

---
