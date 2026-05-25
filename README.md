# ✈️ Avia Company — Flight Booking REST API

Django REST API for managing flights, bookings, aircraft and payments.

## Tech Stack
- Python 3.12, Django 6.0, Django REST Framework
- JWT auth (SimpleJWT), PostgreSQL, Swagger UI

## Features
- User registration & JWT authentication
- Flight search by city and date
- Seat booking with passenger details
- Aircraft and payment management
- Swagger docs at `/api/docs/`

## Quick Start
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py fill_db
python manage.py runserver
```
