# Ticketing + CMDB (FastAPI) — Scaffold Step 1

This repository contains a small FastAPI project skeleton for a ticketing + CMDB service.

Files added in this step:

- `docker-compose.yml` — Postgres and FastAPI (tiangolo image) for quick run
- `app/main.py` — minimal FastAPI app with health endpoint
- `app/models.py` — SQLAlchemy models: Asset, Ticket, Comment
- `alembic/` — Alembic environment and initial migration
- `requirements.txt` — minimal Python deps

How to run (development):

1. Start services: `docker-compose up --build`
2. Visit `http://localhost:8000/health` to check health
