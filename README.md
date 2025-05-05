### Hexlet tests and linter status:
[![Actions Status](https://github.com/Ilia-Ivankov/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Ilia-Ivankov/python-project-52/actions)
### CI
[![Continuous Integration](https://github.com/Ilia-Ivankov/python-project-52/actions/workflows/ci.yml/badge.svg)](https://github.com/Ilia-Ivankov/python-project-52/actions/workflows/ci.yml)
### Maintainability

# Task Manager

A modern, scalable task management system built with Django and Python.

## Project features

- User authentication
- Task management
- Label management
- Status management
- User management

## Technology Stack

- **Backend**:
  - Python 3.10+
  - Django 5.2
  - PostgreSQL (production-grade database)
  - SQLite (development database)

- **Frontend**:
  - HTML5
  - Bootstrap 5 (responsive design)

- **Build & Automation**:
  - Makefile (for project automation)
  - uv (dependency management)

- **Testing**:
  - Django Test Framework

- **CI/CD**:
  - GitHub Actions (automated testing and deployment)

- **Other Tools**:
  - Flake8 (linting)
  - Whitenoise (static files)
  - Rollbar (error tracking)
  - Gunicorn (production server)
  - Django-filter (filtering)
  - Django-bootstrap5 (bootstrap)

You can see all tools in `pyproject.toml` file.

## Project Structure

```
.
├── .github/                  # GitHub CI/CD workflows
│   └── workflows/
│       └── hexlet-check.yml  # Hexlet test workflow
├── .venv/                    # Virtual environment (ignored in Git)
├── locale/                   # Translation files for i18n
├── staticfiles/              # Static assets (CSS, JS, images)
├── task_manager/             # Main Django application
│   ├── migrations/           # Database migrations
│   ├── static/               # App-specific static files
│   ├── templates/            # HTML templates
│   ├── tests/                # Unit and integration tests
│   ├── admin.py              # Django admin configuration
│   ├── apps.py               # App configuration
│   ├── models.py             # Database models
│   ├── urls.py               # URL routing
│   └── views.py              # Business logic
├── .env.example              # Environment variables template
├── .gitignore                # Files ignored by Git
├── build.sh                  # Build script
├── db.sqlite3                # Development database (ignored in Git)
├── Makefile                  # Build automation
├── manage.py                 # Django management script
├── pyproject.toml            # Project metadata and dependencies
├── README.md                 # Project documentation
└── setup.cfg                 # Additional configuration for linting
```

## Production Deployment

### Prerequisites
- PostgreSQL
- Gunicorn

### Makefile commands

```bash
make build # setups all
make test # runs tests
make lint # runs linting
make collectstatic # collects static files
make migrate # applies migrations
make run # starts the server
make render-start # starts the server(production)

```

## How to run the project

1. Clone the repository

```bash
git clone https://github.com/Ilia-Ivankov/python-project-52.git
```

2. Install dependencies

```bash
make build
```

3. Run the project

```bash
make run
```

Don't forget to create `.env` file and set `SECRET_KEY`, `ROLLBAR_TOKEN`, `DATABASE_URL`(for production), `DEBUG`(if True, u will see errors in browser), `ALLOWED_HOSTS`.

## How to use the project

1. Register
2. Login
3. Create a status
4. Create a label
5. Create a task
6. Edit a task
7. Delete a task
8. Delete a status
9. Delete a label
10. Filter tasks

And more...


