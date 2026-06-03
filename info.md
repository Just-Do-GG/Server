# Server

Monolith backend with built-in BackOffice.

## Stack
- Python 3.13+ / FastAPI
- PostgreSQL (async via asyncpg)
- Redis (caching, sessions)
- SQLAlchemy 2.0 (async) + Alembic
- Docker + docker-compose

## Структура
```
app/
├── api/         # Routes (v1, admin)
├── core/        # Config, DB, security
├── models/      # SQLAlchemy models
├── schemas/     # Pydantic schemas
├── services/    # Business logic
└── backoffice/  # Веб-адмінка (React)
```
