#  ResultPrep Task Manager

A full-stack Task Management Web Application built as part of the ResultPrep Systems Internship Assignment.

This project allows users to create, view, update, and delete tasks using a simple UI and REST API.

---

##  Tech Stack

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Backend
- Python
- Flask
- Flask-CORS

### Database
- MySQL (XAMPP)

---

##  Project Structure

resultprep-internship/
│
├── backend/
│ ├── app.py
│ ├── database.py
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│
└── README.md

---

##  Features

-  Create new tasks
-  View all tasks
-  Update task status (pending/completed)
-  Delete tasks
-  REST API integration
-  Frontend connected to backend via Fetch API

---

##  API Endpoints

| Method | Endpoint | Description |
|-------|--------|-------------|
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Create new task |
| PUT | `/tasks/<id>` | Update task status |
| DELETE | `/tasks/<id>` | Delete task |

---

##  Setup Instructions

### 1 Clone the repository

git clone https://github.com/Dharshan098/resultprep-task-manager.git
cd resultprep-task-manager

---

### 2️ Backend Setup

Server will run at:http://127.0.0.1:5000

---

### 3️ Database Setup (XAMPP)

- Start **Apache** and **MySQL** in XAMPP
- Open **phpMyAdmin**
- Create database:

- Create table:

```sql
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) DEFAULT 'pending'
);
```

### 4 Run Frontend

open
frontend/index.html



