# ALX Travel App - Database Seeder

This Django management command populates the database with realistic sample data for **Listings**, **Bookings**, and **Reviews**. It allows developers and testers to quickly work with a populated database without manual data entry.

---

## Overview

The seeder uses **Faker** to generate random but realistic data, simulating real-world travel booking scenarios. This is useful for testing APIs, frontend development, and development workflows.

---

## Usage

1. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
