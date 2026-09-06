# GIGADevlog

## DAY 1 - 06.09.2026

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

### Session 3 (15:44-x)
1. Created `__init__.py` and `main.py` for `app`
2. Created `app lifespan` in advance
3. Created `app instance`
4. Created and set up `Dockerfile`
5. Created a GIGAHouse GIGADockerImage
