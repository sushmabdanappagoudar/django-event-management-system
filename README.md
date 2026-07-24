# 🎉 Django Event Management System

A web-based **Event Management System** developed using **Django** that allows users to register, log in, view events, and manage event information through a simple and user-friendly interface.

## 🚀 Project Overview

The Django Event Management System is designed to simplify event organization and management. It provides user authentication and event management features in a structured web application.

This project demonstrates the implementation of Django's **MVT architecture, authentication system, database models, URL routing, views, and templates**.

## ✨ Features


- 🔐 User Registration
- 🔑 User Login and Authentication
- 📅 View Available Events
- ➕ Add New Events
- 📝 Store Event Details
- 📍 Event Location Management
- 🗓️ Event Date Management
- 🛠️ Django Admin Panel
- 💾 SQLite Database Integration
- 📱 Simple and User-Friendly Interface

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Programming |
| Django | Web Framework |
| HTML | Web Page Structure |
| CSS | User Interface Styling |
| Bootstrap | Responsive UI Design |
| SQLite | Database |
| Git | Version Control |
| GitHub | Project Hosting |

## 📂 Project Structure

```text
django-event-management-system/
│
├── event_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── events/
│   ├── migrations/
│   ├── templates/
│   │   └── events/
│   │       ├── add_event.html
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── login.html
│   │       └── register.html
│   │
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
