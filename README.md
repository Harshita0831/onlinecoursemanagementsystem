# Online Course Management System (OCMS)

A full-stack **Django web application** that enables instructors to create courses and students to enroll, track progress, and review content.  
The system follows a **modular architecture** with separate apps for accounts, courses, enrollments, reviews, and analytics.

---

#  Features

## Authentication & Roles
- Custom user model
- Roles: **Student, Instructor, Admin**
- Secure login system
- Role-based access control

##  Course Management
- Create and manage courses
- Category-based organization
- Modules and lectures structure
- Publish/unpublish courses

##  Enrollment System
- Student enrollment tracking
- Course completion status
- Lecture progress monitoring

## Reviews & Ratings
- Students can rate courses (1–5)
- Feedback system
- One review per student per course

## Dashboard
- Platform analytics
- Course and enrollment metrics
- Performance insights

---

# System Architecture

##  High-Level Flow
Client (Browser)
↓
Django Templates + Static Files
↓
Views (Business Logic)
↓
Models (ORM)
↓
Database

---

#  Project Structure
onlinecourse/
│
├── accounts/ # User authentication & roles
├── courses/ # Course, category, module, lecture
├── enrollments/ # Enrollment & progress
├── reviews/ # Ratings & feedback
├── dashboard/ # Analytics
│
├── templates/ # HTML templates
├── static/ # CSS, JS, images
│
├── manage.py
├── db.sqlite3
└── README.md

---

# 🧩 Application Modules

## Accounts App
Handles authentication and user roles.

**Responsibilities**
- Custom user model  
- Login & session management  
- Role-based permissions  

---

## Courses App
Manages learning content.

**Entities**
- Category  
- Course  
- Module  
- Lecture  

Provides hierarchical course structure.

---

## Enrollments App
Tracks student participation and progress.

**Features**
- Enrollment management  
- Progress tracking  
- Completion status  

---

## Reviews App
Handles feedback and ratings.

**Features**
- Course reviews  
- Rating system  
- Feedback storage  

---

## Dashboard App
Provides analytics and insights.

**Metrics**
- Total users  
- Total courses  
- Enrollment statistics  
- Popular courses  

---

# Database Design

The database follows a **normalized relational schema** with clear relationships:

- User → Course (Instructor)
- Course → Module → Lecture
- Student → Enrollment → Progress
- Course → Reviews

---

# Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** SQLite (Development) / PostgreSQL (Production)  
- **Version Control:** Git & GitHub  

---

# Installation & Setup

## 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/onlinecourse.git
cd onlinecourse
