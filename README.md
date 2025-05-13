### Hexlet tests and linter status:
[![Actions Status](https://github.com/Ilia-Ivankov/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Ilia-Ivankov/python-project-52/actions)
### CI
[![Continuous Integration](https://github.com/Ilia-Ivankov/python-project-52/actions/workflows/ci.yml/badge.svg)](https://github.com/Ilia-Ivankov/python-project-52/actions/workflows/ci.yml)
### Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/aa4c6d38df7a5dcdf29a/maintainability)](https://codeclimate.com/github/Ilia-Ivankov/python-project-52/maintainability)
### Test coverage
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=Ilia-Ivankov_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=Ilia-Ivankov_python-project-52)
### This project is deployed on render
[![Render](https://render.com/images/render-logo-social-card.png)](https://python-project-52-2dgn.onrender.com)

# Task Manager

A modern, robust task management system built with Django and Python. This application provides a comprehensive solution for organizing, tracking, and managing tasks in a collaborative environment. The system implements user authentication, role-based access control, and flexible task organization using statuses and labels.

## Project Features

### User Management
- **Secure Authentication**: Complete user registration, login, and logout functionality
- **Profile Management**: Users can update their profile information
- **User Protection**: Users associated with tasks cannot be deleted, preventing data integrity issues
- **Access Control**: Role-based permissions ensure users can only modify their own information

### Task Management
- **Comprehensive Task Details**: Tasks include name, description, status, assignee, and labels
- **Task Ownership**: Each task has an owner who created it and an executor who is assigned to it
- **Advanced Filtering**: Filter tasks by status, executor, label, or by tasks created by the current user
- **CRUD Operations**: Create, view, update, and delete tasks with appropriate permissions

### Status Management
- **Custom Workflow States**: Create and manage task statuses to reflect your workflow needs
- **Status Protection**: Statuses in use by tasks cannot be deleted, maintaining data integrity
- **Status Tracking**: Each status tracks creation and update timestamps

### Label Management
- **Flexible Categorization**: Organize tasks with custom labels
- **Multiple Labels**: Assign multiple labels to each task for precise organization
- **Label Protection**: Labels used by tasks cannot be deleted, preserving task categorization

### Internationalization
- **Multilingual Support**: Interface available in multiple languages
- **Localized Content**: Date formats and messages adapt to the user's locale

## Technology Stack

### Backend
- **Python 3.10+**: Modern Python version with enhanced features
- **Django 5.2**: Latest stable Django framework for robust web development
- **Django ORM**: Sophisticated object-relational mapping for database interactions
- **PostgreSQL**: Production-grade relational database for data reliability
- **SQLite**: Lightweight database for development and testing

### Frontend
- **HTML5**: Modern markup language for web content
- **Bootstrap 5**: Responsive design framework with modern UI components
- **Django Templates**: Server-side rendering with Django's template engine

### Security
- **Authentication System**: Django's built-in authentication system with custom user model
- **Permission Checks**: Custom mixins ensuring proper access control
- **CSRF Protection**: Cross-Site Request Forgery protection
- **Environment Variables**: Secure configuration using environment variables
- **Password Hashing**: Secure password storage with Django's authentication system

### Testing
- **Django Test Framework**: Comprehensive testing tools for Django applications
- **Pytest**: Advanced testing framework for Python
- **Coverage Reports**: Test coverage analysis to ensure code quality

### CI/CD
- **GitHub Actions**: Automated testing, linting, and deployment workflows
- **SonarQube Integration**: Code quality and security analysis

### Monitoring & Error Tracking
- **Rollbar**: Real-time error tracking and monitoring

### Development Tools
- **Makefile**: Project automation for common tasks
- **UV**: Modern dependency management for Python
- **Flake8**: Code linting to maintain code quality
- **Whitenoise**: Static file serving for production
- **Gunicorn**: Production-ready WSGI server

## Project Structure

```
.
├── .github/                  # GitHub CI/CD workflows
│   └── workflows/
│       ├── ci.yml            # Continuous Integration workflow
│       └── hexlet-check.yml  # Hexlet test workflow
├── locale/                   # Translation files for i18n
├── staticfiles/              # Static assets (CSS, JS, images)
├── task_manager/             # Main Django application
│   ├── templates/            # HTML templates
│   ├── tests/                # Unit and integration tests
│   │   └── settings_test.py  # Test-specific Django settings
│   ├── labels/               # Labels application
│   │   ├── migrations/       # Database migrations for labels
│   │   ├── models.py         # Label data models
│   │   ├── views.py          # Label views
│   │   ├── forms.py          # Label forms
│   │   └── urls.py           # Label URL routing
│   ├── statuses/             # Statuses application
│   │   ├── migrations/       # Database migrations for statuses
│   │   ├── models.py         # Status data models
│   │   ├── views.py          # Status views
│   │   ├── forms.py          # Status forms
│   │   └── urls.py           # Status URL routing
│   ├── tasks/                # Tasks application
│   │   ├── migrations/       # Database migrations for tasks
│   │   ├── models.py         # Task data models
│   │   ├── views.py          # Task views
│   │   ├── forms.py          # Task forms
│   │   └── urls.py           # Task URL routing
│   ├── users/                # Users application
│   │   ├── migrations/       # Database migrations for users
│   │   ├── models.py         # Custom user models
│   │   ├── views.py          # User views
│   │   ├── forms.py          # User forms
│   │   └── urls.py           # User URL routing
│   ├── mixins.py             # Custom mixins for views
│   ├── settings.py           # Django project settings
│   ├── urls.py               # Main URL routing
│   └── views.py              # Main application views
├── .gitignore                # Files ignored by Git
├── build.sh                  # Build script for setup
├── Makefile                  # Build automation commands
├── manage.py                 # Django management script
├── pyproject.toml            # Project metadata and dependencies
├── pytest.ini                # Pytest configuration
└── README.md                 # Project documentation
```

## Production Deployment

### Prerequisites
- Python 3.10 or higher
- PostgreSQL database server
- Gunicorn WSGI server
- Environment variables properly configured

### Deployment Steps
1. Clone the repository
2. Install dependencies with `make build`
3. Configure environment variables
4. Run database migrations with `make migrate`
5. Collect static files with `make collectstatic`
6. Start the server with `make render-start` (production) or `make run` (development)

### Environment Variables
The application requires the following environment variables:

```
# Django settings
SECRET_KEY=yoursecretkeyhere
DEBUG=True  # Set to False in production
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Rollbar settings (optional)
ROLLBAR_ACCESS_TOKEN=youraccesstokenhere

# Database settings (for PostgreSQL)
DATABASE_URL=postgres://user:password@localhost:5432/dbname
```

## Development Setup

### Local Setup

1. Clone the repository
```bash
git clone https://github.com/Ilia-Ivankov/python-project-52.git
cd python-project-52
```

2. Install dependencies
```bash
make build
```

3. Create `.env` file with required environment variables (see above)

4. Apply migrations and start the development server
```bash
make migrate
make run
```

The server will be available at http://localhost:8000

### Running Tests

The project includes comprehensive tests covering all major functionality:

```bash
# Run all tests
make test

# Generate coverage report
make coverage
```

For testing in CI/CD environments or without an `.env` file, tests use the configuration in `task_manager/tests/settings_test.py` that provides default values for required settings.

### Code Quality

Maintain code quality with the built-in linter:

```bash
make lint
```

## Data Models

### User Model
- Extension of Django's AbstractUser with additional fields
- Includes first name, last name, username
- Tracks creation and update timestamps
- Protected from deletion when associated with tasks

### Task Model
- Core entity containing task details
- Fields: name, description, status, owner, executor, labels
- Relationships with Status, User, and Label models
- Timestamps for creation and updates

### Status Model
- Represents the current state of a task
- Contains a unique name field
- Protected from deletion when in use by tasks
- Includes timestamps

### Label Model
- Used to categorize and tag tasks
- Contains a unique name field
- Can be assigned to multiple tasks
- Protected from deletion when in use
- Includes timestamps

## User Guide

### Getting Started

1. Register a new account
2. Login with your credentials
3. Set up task statuses to reflect your workflow (e.g., "To Do", "In Progress", "Done")
4. Create labels to categorize tasks (e.g., "Bug", "Feature", "Documentation")

### Creating and Managing Tasks

1. Navigate to the Tasks section
2. Create a new task with required details
3. Assign the task to a user
4. Add relevant labels
5. Set the appropriate status

### Using Filters

1. Go to the Tasks list
2. Use the filter form to narrow down tasks by:
   - Status
   - Executor (assignee)
   - Labels
   - Your tasks (tasks you created)

### User and Account Management

1. Update your profile information as needed
2. Maintain user accounts (administrators only)
3. Note that users associated with tasks cannot be deleted

## Example of work

[![asciicast](https://asciinema.org/a/At7RZiRLI1gH4d6J1eytvVKGj.svg)](https://asciinema.org/a/At7RZiRLI1gH4d6J1eytvVKGj)