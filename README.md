# task-api

A production-grade REST API built with FastAPI and PostgreSQL, designed to demonstrate backend engineering best practices: clean architecture, request validation, authentication, caching, idempotency, and observability.

## Stack

- **FastAPI** — async Python web framework
- **PostgreSQL** — primary data store
- **Redis** — caching and idempotency
- **Pydantic** — request/response validation
- **Docker** — containerization
- **pytest** — testing

## Project Structure
```
app/
├── api/v1/routes/   # HTTP layer — route definitions only, no business logic
├── core/            # Configuration and shared utilities
├── models/          # SQLAlchemy ORM models
├── schemas/         # Pydantic request/response schemas
├── services/        # Business logic layer
├── repositories/    # Data access layer — all DB queries live here
└── main.py          # App entrypoint
tests/               # Test suite
```

## Running Locally
```bash
git clone git@github.com:alexkak/task-api.git
cd task-api

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Edit .env with your values

uvicorn app.main:app --reload
```

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/api/v1/health` | Health check |

## API Docs

Interactive docs available at `http://localhost:8000/docs` when running locally.