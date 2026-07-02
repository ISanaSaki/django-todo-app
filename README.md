# Django Todo App

A simple Todo application built with Django, featuring user authentication and per-user task management.

## Features

- User registration and login
- Create, read, update, and delete todos
- Each user sees only their own todos
- Protected routes (login required)

## Tech Stack

- Python 3.12
- Django 6.0.5
- SQLite (development)

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ISanaSaki/django-todo-app.git
cd django-todo-app
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in your values:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

To generate a secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000`

## Project Structure

```
├── accounts/        # User registration and authentication
├── home/            # Todo CRUD logic
├── templates/       # HTML templates
├── .env.example     # Environment variable template
├── manage.py
└── requirements.txt
```
