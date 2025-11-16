# ALX Travel App

A Django-based backend application for managing travel listings, bookings, and reviews. This project demonstrates how to model relational data, create APIs with Django REST Framework, and seed the database with realistic sample data for development and testing.

---

## Features

- **Listings**: Add and manage travel properties with details like location, price, and availability.  
- **Bookings**: Users can book listings with check-in/out dates and guest details.  
- **Reviews**: Guests can leave ratings and comments on listings.  
- **API Endpoints**: CRUD operations for Listings, Bookings, and Reviews using Django REST Framework.  
- **Database Seeder**: Automatically populate the database with sample data using a management command.  

---

## Tech Stack

- **Backend**: Django, Django REST Framework  
- **Database**: SQLite/MySQL/PostgreSQL  
- **Data Generation**: Faker library for realistic sample data  
- **CORS**: Configured for API access from any origin  

---

## Usage

1. Clone the project and install dependencies.  
2. Configure environment variables in `.env`.  
3. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
