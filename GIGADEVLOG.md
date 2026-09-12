# GIGADevlog

## Day 1 - 06.09.2026

### Session 1 (8:50-10:50)
1. Picked project idea and researched it
2. Planned out the project scope
3. Researched the architecture behind `LeapScope` and adjusted the initial project scope
4. Created `GIGAROADMAP.md`
5. Created `GIGAREADME.md`
6. Created `GIGADEVLOG.md`
7. Created GitHub `GIGARepository` and `GIGADescription` 
8. Connected `GIGARepository` to the `GIGAWorkspace`


### Session 2 (12:27-13:52)
1. Created `.gitignore` 
2. Created and activated `virtual environment`
3. Created `.env` and `.env.example`
4. Created and configured `pyproject.toml` + installed project dependencies
5. Created `app` and `tests` folders
6. Configured basic application settings inside `.env`
7. Pasted `.env` into `.env.example`
8. Created `core` subpackage for `app` and marked it with `__init__.py`
9. Created `config.py` module
10. Created and configured `Settings(BaseSettings)` class inside `config.py` for validated environment app settings
11. Created `get_settings()` with `@lru_cache` decorator for reusability
12. Created `database` subpackage for `app` and marked it with `__init__.py`
13. Created `base.py` and `session.py` modules for `database` subpackage
14. Created `DeclarativeBase` parent class inside `base.py` module
15. Configured SQLAlchemy engine inside `session.py` and Session Factory

### Session 3 (15:44-16:27)
1. Created `__init__.py` and `main.py` for `app`
2. Created `app lifespan` in advance
3. Created `app instance`
4. Created and set up `Dockerfile`
5. Created a GIGAHouse GIGADockerImage
6. Created `.dockerignore`
7. Created `api` service in `docker-compose.yml`
8. Created `db` service in `docker-compose.yml`
9. Created `test-db` service in `docker-compose.yml`


## Day 2 - 07.09.2026

### Session 1 (17:25-17:51)
- Configured PostgreSQL inside `.env`
- Generated secret password inside `.env` and put fake password inside `.env.example`
- Created database URL inside `.env.py` n used fake password inside the URL for `.env.example`
- Initialized `Alembic` inside GIGAHOUSE virtual environment
- Left sqlalchemy.url inside `alembic.ini` blank to avoid hard-coding and to have Alembic use the same database configuration as the application
- Connected `Alembic` to `SQLAlchemy` inside `alembic/env.py`

## Day 3 - 10.09.2026

### Session 1 (19:57-20:41)
- Added `healthcheck `for the api service inside `docker-compose.yml`
- Added `healthcheck `for the db service inside `docker-compose.yml`
- Added `healthcheck `for the test-db service inside `docker-compose.yml`
- Created `health.py` router
- Created `health` endpoint
- Created `readiness` endpoint
- Connected the `health` router to `main.py`
- Added pytests for:
    - health endpoint
    - readiness endpoint

## Day 4 - 12.09.2026

### Session 1 (07:18-07:54)
- Created `.github/workflows`
    - `.gitkeep`
    - `tests.yml`
- Configured GitHub Actions CI
- Verified that the CI test workflow runs successfully
- After 10 minutes of pondering why the alembic check CI test failed, I have finally found a typo inside `alembic/env.py`