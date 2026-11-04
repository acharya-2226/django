# 🌱 Django Learning Project

A beginner Django project built while learning the framework. It has two apps that cover URL routing, views, templates, models, forms, the admin panel, and basic database operations, styled with Bootstrap 5.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Apps and Features](#-apps-and-features)
- [URL Routes](#-url-routes)
- [Data Models](#-data-models)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [Concepts Practiced](#-concepts-practiced)
- [Notes](#-notes)
- [Author](#-author)

---

## 📖 Overview

The project (`firstdjangoproject`) contains two apps. `firstapp` covers templates and forms with country and province pages. `secondapp` adds a contact form that saves submissions to the database and lists them on the same page.

---

## 🧩 Apps and Features

### `firstapp`: Templates and Forms

| Feature | Description |
|---------|-------------|
| **Demo view** | A minimal view that returns a plain `HttpResponse` |
| **Country page** | Renders country details (name, continent, code) through a template with context data |
| **Province page** | Renders province details through a template |
| **Add Country form** | A Django `ModelForm`; on submit, the entered values are displayed back on the page |
| **Add Province form** | A `ModelForm` for the province name and chief minister |
| **Admin** | `country` and `Province` models are registered in Django Admin |

### `secondapp`: Contact Form with Database

| Feature | Description |
|---------|-------------|
| **Contact form** | A `ModelForm` with first name, last name, email, phone, address, and message |
| **Save to database** | A valid POST creates and saves a `Contact` record |
| **Submissions list** | All saved contacts are fetched from the database and shown below the form |

### Shared

- `templates/base.html` is a base layout with a Bootstrap navbar, and the page templates extend it using blocks for the title and custom CSS.
- Bootstrap 5 is served locally from `static/assets/`.

---

## 🗺️ URL Routes

All routes are prefixed by their app.

| URL | View | Purpose |
|-----|------|---------|
| `/admin/` | Django Admin | Manage records |
| `/firstapp/demo/` | `demo` | Plain text response |
| `/firstapp/country/` | `country` | Country details page |
| `/firstapp/province/` | `province` | Province details page |
| `/firstapp/add-country/` | `add_country` | Add Country form |
| `/firstapp/add-province/` | `add_province` | Add Province form |
| `/secondapp/contact-us/` | `contact_form` | Contact form and submissions list |

---

## 🗄️ Data Models

| Model | App | Fields |
|-------|-----|--------|
| `country` | `firstapp` | `country_name`, `country_code`, `continent` |
| `Province` | `firstapp` | `province_name`, `province_cm` (optional) |
| `Contact` | `secondapp` | `first_name`, `last_name`, `email` (unique), `phone_no`, `contact_date`, `address`, `message` |

---

## 🚀 Getting Started

**Requirements:** Python 3.10 or newer (needed by Django 5.2).

```bash
# Clone
git clone https://github.com/acharya-2226/django.git
cd django

# Create and activate a virtual environment
python -m venv env
env\Scripts\activate           # Windows
# source env/bin/activate      # macOS / Linux

# Install Django
pip install "Django>=5.2,<5.3"

# Set up the database
python manage.py migrate
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

Open **http://127.0.0.1:8000/firstapp/country/** or **http://127.0.0.1:8000/secondapp/contact-us/**.
The admin panel is at **http://127.0.0.1:8000/admin/**.

---

## 📁 Project Structure

```text
django/
├── manage.py
├── db.sqlite3                  # Local SQLite database
├── firstdjangoproject/         # Project settings and root URLs
│   ├── settings.py
│   └── urls.py
├── firstapp/                   # Country and province pages and forms
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── secondapp/                  # Contact form with database
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── templates/                  # base.html and page templates
└── static/assets/              # Bootstrap 5 CSS/JS and custom style.css and script.js
```

---

## 🎓 Concepts Practiced

- Creating a project and multiple apps
- URL routing with `include()` and named routes
- Function-based views and template rendering with context
- Template inheritance (`{% extends %}` and blocks)
- Serving static files
- Models, migrations, and the Django ORM
- `ModelForm` and handling GET and POST requests
- Registering models in Django Admin

---

## 📝 Notes

- This is a learning project configured for **local development** (`DEBUG = True`). Move the secret key to an environment variable and review the settings before deploying anywhere.
- The repository includes a sample `db.sqlite3`. Delete it and run `python manage.py migrate` to start with an empty database.

---

## 👤 Author

**Siddharth Acharya**
B.E. Computer Engineering, Himalaya College of Engineering (HCOE), Tribhuvan University
GitHub: [@acharya-2226](https://github.com/acharya-2226)
