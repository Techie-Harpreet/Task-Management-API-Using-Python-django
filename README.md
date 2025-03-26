# Task Management API

## Overview
This project is a **Task Management API** built using **Django** and **Django Rest Framework (DRF)**. The API allows users to:
- Create tasks
- Assign tasks to multiple users
- Retrieve tasks assigned to specific users
- Retrieve all registered users
- Use authentication for secure access

## Features
✅ **Create Task** - Allows users to create a new task with a name and description.
✅ **Assign Task** - Assign a task to multiple users.
✅ **Get User Tasks** - Retrieve all tasks assigned to a specific user.
✅ **Get All Users** - Retrieve a list of all registered users.
✅ **Authentication** - Uses Token Authentication to secure endpoints.

## Tech Stack
- **Django** - Backend framework
- **Django Rest Framework (DRF)** - API framework
- **SQLite** (default) or any other relational database

---

## Installation Guide
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/task-manager.git
cd task-manager
```

### 2️⃣ Create a Virtual Environment & Activate
```bash
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations
```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional for Admin Access)
```bash
python manage.py createsuperuser
```

### 6️⃣ Start the Server
```bash
python manage.py runserver
```

---

## API Endpoints

### **Authentication**
🔐 **Obtain Auth Token**  
**POST** `/api/token/`
```json
{
    "username": "harpreet",
    "password": "yourpassword"
}
```
🔹 **Response:**
```json
{
    "token": "your-auth-token"
}
```

### **Task Management**
📌 **Create Task**  
**POST** `/api/tasks/create/`
```json
{
    "name": "Complete Django Assignment",
    "description": "Finish the DRF API task",
    "task_type": "coding"
}
```
🔹 **Response:**
```json
{
    "id": 1,
    "name": "Complete Django Assignment",
    "description": "Finish the DRF API task",
    "status": "pending"
}
```

📌 **Assign Task to Users**  
**POST** `/api/tasks/{task_id}/assign/`
```json
{
    "assigned_users": [1, 2]
}
```
🔹 **Response:**
```json
{
    "message": "Task assigned successfully."
}
```

📌 **Get All Tasks**  
**GET** `/api/tasks/`
🔹 **Response:**
```json
[
    {
        "id": 1,
        "name": "Complete Django Assignment",
        "description": "Finish the DRF API task",
        "status": "pending",
        "assigned_users": [1, 2]
    }
]
```

📌 **Get Tasks Assigned to a Specific User**  
**GET** `/api/tasks/user/{user_id}/`
🔹 **Response:**
```json
[
    {
        "id": 1,
        "name": "Complete Django Assignment",
        "description": "Finish the DRF API task",
        "status": "pending",
        "assigned_users": [1, 2]
    }
]
```

### **User Management**
📌 **Get All Users**  
**GET** `/api/users/`
🔹 **Response:**
```json
[
    {
        "id": 1,
        "name": "harpreet",
        "email": "harpreet@example.com"
    },
    {
        "id": 2,
        "name": "mustafa",
        "email": "mustafa@example.com"
    }
]
```

---

## Authentication Setup
This API uses **Token Authentication**. Follow these steps:

1️⃣ **Get Token:**  
Send a **POST** request to `/api/token/` with username and password.

2️⃣ **Use Token in Requests:**  
Add the token in the `Authorization` header of all protected API calls:
```bash
Authorization: Token your-auth-token
```

---

## Notes
- Ensure you are authenticated before accessing protected endpoints.
- Only assigned users can see their tasks.
- Admin users can create and assign tasks.


