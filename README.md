<div align="center">

# 🎓 MSTI Institute
### Modern Student Training Institute Management System

<img src="https://img.shields.io/badge/MSTI-Institute-4A90E2?style=for-the-badge&logo=academia&logoColor=white" alt="MSTI Badge"/>

[![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com/)
[![HTML](https://img.shields.io/badge/HTML-91. 9%25-E34F26? style=flat-square&logo=html5&logoColor=white)](https://github.com/mogesh-developer/MSTI_Institute)
[![CSS](https://img.shields.io/badge/CSS-4.2%25-1572B6? style=flat-square&logo=css3&logoColor=white)](https://github.com/mogesh-developer/MSTI_Institute)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg? style=flat-square)](LICENSE)

**A comprehensive web-based educational management platform built with Flask, SQLAlchemy, and modern web technologies**

[🚀 Quick Start](#-quick-start) • [📸 Screenshots](#-screenshots) • [🎓 Features](#-features) • [📖 Documentation](#-documentation) • [🤝 Contributing](#-contributing)

---

</div>

## 📋 Table of Contents

- [🎯 About](#-about)
- [✨ Features](#-features)
- [🎓 Available Courses](#-available-courses)
- [🛠️ Tech Stack](#️-tech-stack)
- [🚀 Quick Start](#-quick-start)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
- [📖 Documentation](#-documentation)
  - [Project Structure](#project-structure)
  - [API Routes](#api-routes)
  - [Database Schema](#database-schema)
- [🎮 Usage Guide](#-usage-guide)
- [📸 Screenshots](#-screenshots)
- [🔒 Security](#-security)
- [🐛 Troubleshooting](#-troubleshooting)
- [🗺️ Roadmap](#️-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📧 Contact](#-contact)
- [🙏 Acknowledgments](#-acknowledgments)

---

## 🎯 About

**MSTI Institute** is a full-stack web application designed to streamline the management of educational institutes. Built with Flask and MySQL, it provides a robust platform for students to browse courses, apply for programs, and manage their enrollments, while giving administrators complete oversight of the student body and course applications.

### 🌟 Why Choose MSTI Institute?

| Feature | Benefit |
|---------|---------|
| 🚀 **Fast Setup** | Get started in minutes with simple installation |
| 📱 **Responsive Design** | Works flawlessly on desktop, tablet, and mobile |
| 🔐 **Secure Authentication** | Password hashing with Werkzeug security |
| 🎨 **Modern UI/UX** | Clean, intuitive interface for all users |
| 📊 **Admin Dashboard** | Complete oversight of students and applications |
| 🔄 **Real-time Updates** | Instant feedback with Flask flash messages |
| 🎓 **Course Management** | Easy course application and removal |
| ⚡ **Lightweight** | Minimal dependencies, maximum performance |

---

## ✨ Features

### 👨‍🎓 Student Portal
- ✅ **User Registration & Authentication** - Secure signup and login system
- ✅ **Browse Courses** - Explore 9+ diploma programs
- ✅ **Course Application** - Apply for courses with one click
- ✅ **Personal Dashboard** - View and manage enrolled courses
- ✅ **Remove Enrollments** - Unenroll from courses easily
- ✅ **Session Management** - Secure session handling

### 👨‍💼 Admin Panel
- ✅ **Secure Admin Access** - Separate admin authentication
- ✅ **Student Management** - View all registered students
- ✅ **Application Tracking** - Monitor course applications
- ✅ **Dashboard Analytics** - Overview of system activity
- ✅ **User Monitoring** - Track student course selections

### 🎨 User Experience
- ✅ **Responsive Design** - Mobile-first approach
- ✅ **Flash Notifications** - Real-time user feedback
- ✅ **Clean Navigation** - Intuitive menu structure
- ✅ **About & Contact Pages** - Information and support

---

## 🎓 Available Courses

MSTI Institute offers diploma programs in various fields:

| Course Code | Course Name | Description |
|-------------|-------------|-------------|
| **DHM** | Diploma in Hotel Management | Comprehensive hospitality training |
| **DGDA** | Diploma in Graphic Design & Animation | Creative design and animation skills |
| **DXRT** | Diploma in X-Ray Technology | Medical imaging technology |
| **DMLTA** | Diploma in Medical Lab Technology | Clinical laboratory procedures |
| **DNA** | Diploma in Nursing Assistant | Healthcare and patient care |
| **DHMCT** | Diploma in Hotel Management & Catering Technology | Culinary and hospitality arts |
| **DPSM** | Diploma in Pharmaceutical Sales & Marketing | Pharma business and marketing |
| **DCT** | Diploma in Computer Technology | IT fundamentals and applications |
| **DIFP** | Diploma in Interior & Fashion Photography | Photography and visual arts |

> 💡 Each course has a dedicated information page with detailed curriculum and requirements

---

## 🛠️ Tech Stack

### Backend
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1? style=for-the-badge&logo=mysql&logoColor=white)

- **Flask 3.1.0** - Micro web framework
- **Flask-SQLAlchemy 3.1.1** - ORM for database management
- **PyMySQL 1.1.0** - MySQL database connector
- **Werkzeug 3.1.3** - WSGI utility library with password hashing
- **Gunicorn 20.1.0** - Production WSGI server

### Frontend
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

- **HTML5** - Modern semantic markup
- **CSS3** - Responsive styling and animations
- **JavaScript** - Interactive client-side functionality
- **Jinja2 3.1.6** - Template engine

### Additional Tools
- **Flask-WTF 1.2.2** - Form handling and CSRF protection
- **Email Validator 2.2.0** - Email validation
- **Blinker 1.9.0** - Signal support

---

## 🚀 Quick Start

### Prerequisites

Ensure you have the following installed on your system:

```bash
Python 3.9 or higher
MySQL Server 5.7+
Git
pip (Python package manager)
Virtual environment tool (venv)
```

### Installation

**1. Clone the Repository**

```bash
git clone https://github.com/mogesh-developer/MSTI_Institute.git
cd MSTI_Institute
```

**2. Create Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### Database Setup

**4. Configure MySQL**

```bash
# Start MySQL Server
# Windows: Start MySQL service from Services
# macOS:  brew services start mysql
# Linux: sudo systemctl start mysql
```

**5. Create Database**

```bash
# Run the database creation script
python create_database.py
```

Or manually create database: 

```sql
mysql -u root -p
CREATE DATABASE flask_auth_db;
```

**6. Update Configuration**

Edit `app.py` and update database credentials:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:YOUR_PASSWORD@localhost/flask_auth_db'
app.secret_key = 'your-secret-key-here'  # Change this!
```

**7. Initialize Database Tables**

```bash
# Tables are automatically created on first run
python app.py
```

**8. Run the Application**

```bash
# Development Mode
python app.py

# Production Mode
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

**9. Access the Application**

Open your browser and navigate to: 
```
http://localhost:5000
```

### 🎮 Demo Credentials

**Student Account:**
1. Register a new account at `/register`
2. Login with your credentials

**Admin Account:**
1. Create admin via:  `http://localhost:5000/admin/register? key=YOUR_SECRET_KEY`
2. Login at: `/admin/login`

> ⚠️ **Security Note:** Change the secret key in production and secure the admin registration route!

---

## 📖 Documentation

### Project Structure

```
MSTI_Institute/
│
├── app.py                      # Main Flask application
├── create_database.py          # Database initialization script
├── requirements.txt            # Python dependencies
├── MYSQL_SETUP.md             # MySQL setup guide
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── index.html             # Home/Dashboard page
│   ├── login.html             # Student login
│   ├── register.html          # Student registration
│   ├── dashboard.html         # Student dashboard
│   ├── admin_login.html       # Admin login
│   ├── admin_register.html    # Admin registration
│   ├── admin_dashboard.html   # Admin panel
│   ├── about.html             # About page
│   ├── contact.html           # Contact page
│   └── courses/               # Course detail pages
│       ├── dhm.html
│       ├── dgda. html
│       ├── dxrt.html
│       ├── dmlta.html
│       ├── dna. html
│       ├── dhmct.html
│       ├── dpsm.html
│       ├── dct.html
│       └── difp.html
│
└── static/                     # Static files
    ├── css/                   # Stylesheets
    ├── js/                    # JavaScript files
    └── images/                # Images and assets
```

### API Routes

#### Public Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Home page (redirects to dashboard if logged in) |
| `/register` | GET, POST | Student registration |
| `/login` | GET, POST | Student login |
| `/about` | GET | About page |
| `/contact` | GET | Contact information |

#### Student Routes (Protected)

| Route | Method | Description |
|-------|--------|-------------|
| `/dashboard` | GET | Student dashboard |
| `/user_dashboard` | GET | User-specific dashboard with courses |
| `/apply_course` | POST | Apply for a course |
| `/remove_course` | POST | Remove course enrollment |
| `/logout` | GET | Logout student |

#### Course Pages

| Route | Method | Description |
|-------|--------|-------------|
| `/dhm.html` | GET | Hotel Management course details |
| `/dgda` | GET | Graphic Design course |
| `/dxrt` | GET | X-Ray Technology course |
| `/dmlta` | GET | Medical Lab Technology course |
| `/dna` | GET | Nursing Assistant course |
| `/dhmct` | GET | Hotel Management & Catering course |
| `/dpsm` | GET | Pharmaceutical Sales course |
| `/dct` | GET | Computer Technology course |
| `/difp` | GET | Photography course |

#### Admin Routes (Protected)

| Route | Method | Description |
|-------|--------|-------------|
| `/admin/register` | GET, POST | Admin registration (secured) |
| `/admin/login` | GET, POST | Admin login |
| `/admin/dashboard` | GET | Admin panel with all users |
| `/admin/logout` | GET | Logout admin |

### Database Schema

#### Users Table

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    applied_courses TEXT DEFAULT ''
);
```

#### Admins Table

```sql
CREATE TABLE admins (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(80) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### User Model Methods

```python
class User(db.Model):
    # Get list of applied courses
    get_applied_courses_list()
    
    # Add a course to user's list
    add_course(course_name)
    
    # Remove a course from user's list
    remove_course(course_name)
```

---

## 🎮 Usage Guide

### For Students

1. **Registration**
   ```
   Navigate to /register
   → Enter username and password
   → Click "Register"
   → Redirected to login
   ```

2. **Login**
   ```
   Navigate to /login
   → Enter credentials
   → Access dashboard
   ```

3. **Apply for Course**
   ```
   Browse course pages
   → Click "Apply" button
   → Course added to dashboard
   → View in user_dashboard
   ```

4. **Manage Enrollments**
   ```
   Go to user_dashboard
   → View applied courses
   → Click "Remove" to unenroll
   ```

### For Administrators

1. **First-time Setup**
   ```
   Access /admin/register? key=SECRET
   → Create admin account
   → Login at /admin/login
   ```

2. **View Students**
   ```
   Login to admin panel
   → See all registered students
   → View their applied courses
   → Monitor system activity
   ```

---

## 📸 Screenshots

### 🏠 Home Page
> Add screenshot here:  Landing page with course offerings

### 📝 Student Registration
> Add screenshot here: Registration form

### 🎓 Student Dashboard
> Add screenshot here: User dashboard with applied courses

### 👨‍💼 Admin Dashboard
> Add screenshot here: Admin panel showing all students

### 📚 Course Details
> Add screenshot here: Individual course information page

---

## 🔒 Security

### Implemented Security Features

- ✅ **Password Hashing** - Werkzeug's `generate_password_hash()`
- ✅ **Session Management** - Flask secure sessions
- ✅ **CSRF Protection** - Flask-WTF integration ready
- ✅ **SQL Injection Prevention** - SQLAlchemy ORM
- ✅ **Admin Route Protection** - Session-based authorization

### Security Best Practices

⚠️ **Before deploying to production:**

1. **Change Secret Key**
   ```python
   app.secret_key = os.environ.get('SECRET_KEY') or 'your-production-secret-key'
   ```

2. **Secure Database Credentials**
   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
   ```

3. **Disable Debug Mode**
   ```python
   app.run(debug=False)
   ```

4. **Secure Admin Registration**
   ```python
   # Implement stronger authentication for admin registration
   # Or remove the route after creating admin accounts
   ```

5. **Use HTTPS**
   ```python
   # Configure SSL certificates
   # Use reverse proxy (Nginx) with SSL
   ```

6. **Environment Variables**
   ```bash
   # Create .env file
   SECRET_KEY=your-secret-key
   DATABASE_URL=mysql+pymysql://user:pass@localhost/db
   ```

---

## 🐛 Troubleshooting

### Common Issues

**Problem:  Database Connection Error**
```bash
sqlalchemy.exc.OperationalError: Can't connect to MySQL server
```
**Solution:**
- Ensure MySQL server is running
- Check database credentials in `app.py`
- Verify database `flask_auth_db` exists

---

**Problem: Module Not Found Error**
```bash
ModuleNotFoundError: No module named 'flask'
```
**Solution:**
```bash
pip install -r requirements.txt
# Or activate virtual environment
source venv/bin/activate  # Unix
venv\Scripts\activate     # Windows
```

---

**Problem: Template Not Found**
```bash
jinja2.exceptions.TemplateNotFound: index.html
```
**Solution:**
- Ensure `templates/` directory exists
- Check template file names match route render calls
- Verify Flask is looking in correct directory

---

**Problem: Port Already in Use**
```bash
OSError: [Errno 48] Address already in use
```
**Solution:**
```bash
# Find process using port 5000
lsof -i :5000  # Unix
netstat -ano | findstr :5000  # Windows

# Kill the process or use different port
python app.py --port 5001
```

---

**Problem: Admin Registration Not Working**
```
Admin registration page not accessible
```
**Solution:**
- Access with secret key:  `/admin/register?key=YOUR_KEY`
- Or modify route to remove key requirement temporarily

---

### Debug Mode

Enable detailed error messages:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

### Logging

Add logging for debugging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

---

## 🗺️ Roadmap

### 🚀 Version 2.0 (Planned)

- [ ] **Email Verification** - Verify student email addresses
- [ ] **Password Reset** - Forgot password functionality
- [ ] **Course Ratings** - Student feedback system
- [ ] **Payment Integration** - Course fee payment gateway
- [ ] **Certificate Generation** - Automated PDF certificates
- [ ] **Calendar Integration** - Class schedules and events
- [ ] **File Upload** - Student document submission
- [ ] **Notifications** - Email and in-app notifications

### 🎨 Version 2.5 (Future)

- [ ] **RESTful API** - Mobile app support
- [ ] **Multi-language Support** - Internationalization
- [ ] **Advanced Analytics** - Charts and reports
- [ ] **Live Chat** - Student support chat
- [ ] **Video Streaming** - Online classes integration
- [ ] **Forum System** - Student community
- [ ] **Mobile App** - iOS and Android applications

### 🔧 Technical Improvements

- [ ] **Docker Support** - Containerization
- [ ] **CI/CD Pipeline** - Automated testing and deployment
- [ ] **API Documentation** - Swagger/OpenAPI integration
- [ ] **Performance Optimization** - Caching with Redis
- [ ] **Database Migration** - Alembic integration
- [ ] **Unit Tests** - Pytest test suite
- [ ] **Load Balancing** - Multi-server support

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### How to Contribute

1. **Fork the Repository**
   ```bash
   Click 'Fork' button on GitHub
   ```

2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/MSTI_Institute.git
   cd MSTI_Institute
   ```

3. **Create a Branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```

4. **Make Your Changes**
   ```bash
   # Make your improvements
   # Follow coding standards
   # Test thoroughly
   ```

5. **Commit Your Changes**
   ```bash
   git add .
   git commit -m "Add amazing feature"
   ```

6. **Push to Your Fork**
   ```bash
   git push origin feature/amazing-feature
   ```

7. **Open a Pull Request**
   ```
   Go to original repo on GitHub
   → Click 'Pull Request'
   → Describe your changes
   → Submit PR
   ```

### Contribution Guidelines

- 📝 Follow PEP 8 style guide for Python code
- 💬 Write clear commit messages
- 📚 Update documentation for new features
- ✅ Test your changes thoroughly
- 🐛 Report bugs with detailed information
- 💡 Suggest features via Issues

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on what's best for the community

---

## 📄 License

This project is licensed under the **MIT License**. 

```
MIT License

Copyright (c) 2025 MSTI Institute

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
```

See [LICENSE](LICENSE) file for full details.

---

## 📧 Contact

### 👨‍💻 Developer

**Mogesh Developer**
- GitHub: [@mogesh-developer](https://github.com/mogesh-developer)
- Repository: [MSTI_Institute](https://github.com/mogesh-developer/MSTI_Institute)

### 🐛 Report Issues

Found a bug?  Have a suggestion? 
- [Open an Issue](https://github.com/mogesh-developer/MSTI_Institute/issues/new)
- [View Existing Issues](https://github.com/mogesh-developer/MSTI_Institute/issues)

### 💬 Discussion

- [Start a Discussion](https://github.com/mogesh-developer/MSTI_Institute/discussions)
- Share ideas and feedback

---

## 🙏 Acknowledgments

Special thanks to: 

- **Flask Team** - For the amazing web framework
- **SQLAlchemy** - For powerful ORM capabilities
- **MySQL** - For reliable database management
- **Open Source Community** - For continuous inspiration
- **Contributors** - Everyone who helps improve this project

### Built With

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [MySQL](https://www.mysql.com/) - Database system
- [Bootstrap](https://getbootstrap.com/) - UI components (if used)
- [Font Awesome](https://fontawesome.com/) - Icons (if used)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Made with ❤️ by [Mogesh Developer](https://github.com/mogesh-developer)**

![GitHub stars](https://img.shields.io/github/stars/mogesh-developer/MSTI_Institute?style=social)
![GitHub forks](https://img.shields.io/github/forks/mogesh-developer/MSTI_Institute?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/mogesh-developer/MSTI_Institute?style=social)

---

**[⬆ Back to Top](#-msti-institute)**

</div>
