# EV Chain

EV Chain is a web-based Electric Vehicle Charging Center Management System designed to manage charging centers, bookings, feedback, and complaints across Admin, User, and Charging Center modules.

## 🚀 Project Overview

EV Chain provides a centralized platform for administrators, EV drivers, and charging center operators to collaborate and manage charging operations. It supports booking, complaint handling, feedback management, and approval workflows for charging centers.

## ✨ Features

- Admin approval and management of charging centers
- Charging center activation and blocking
- Booking approval/rejection workflow for charging centers
- User booking status tracking
- Complaint submission and reply management
- Feedback submission and review
- Role-based dashboards for Admin, User, and Charging Center operators

## 🧩 Modules

### ADMIN
- Accept/Reject Charging Centers
- Block/Unblock Charging Centers
- View Complaints and Send Replies
- View Feedback
- View Users

### USER
- View Charging Centers
- Book Charging Slots
- View Booking Status
- Send Complaints
- View Complaint Replies
- Send Feedback

### CHARGING CENTER
- View Bookings
- Accept/Reject Bookings
- View Users
- Send Complaints
- View Complaint Replies
- Send Feedback

## 🏗️ System Architecture

EV Chain is built with Django as the backend framework and relies on server-side rendered HTML templates. It includes:

- Django project configuration in `EV_Chain_project/`
- Main application logic in `EV_chain_app/`
- HTML templates in `templates/`
- Static assets in `EV_chain_app/static/`
- SQLite/MySQL database support via Django ORM

## 💻 Technologies Used

- Python
- Django
- SQLite3 / MySQL
- HTML
- CSS
- Bootstrap 5
- JavaScript
- Django Templates

## 🛠️ Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/<your-username>/ev-chain.git
cd EV_Chain_project
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

- Windows (PowerShell):
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
- Windows (cmd.exe):
  ```cmd
  .\venv\Scripts\activate
  ```

### 4. Install Requirements

```bash
pip install -r requirements.txt
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Start Server

```bash
python manage.py runserver
```

### 7. Default URL

Open the browser at:

```text
http://127.0.0.1:8000/
```

## 📁 Project Structure

- `EV_chain_app/` - Main Django application
- `EV_Chain_project/` - Django project settings and configuration
- `templates/` - HTML templates for views
- `db.sqlite3` - Local development database file
- `manage.py` - Django management utility

## 🚧 Future Enhancements

- Add user authentication roles with improved access control
- Add image upload support for charging center listings
- Add real-time booking availability and slot countdowns
- Add email notifications for booking and complaint updates
- Add REST API support for mobile or SPA clients

## 👤 Author

**NANDHANA M J**
- **Project Name:** EV Chain
- **Internship Project**
- **Technologies:** Python, Django, SQLite3, HTML, CSS, Bootstrap 5, JavaScript