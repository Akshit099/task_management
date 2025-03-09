# Simple Task Management API

This is a simple Task Management API built using Flask and MySQL, designed to allow users to create, read, update, and delete tasks.

## Developer

Developed by Akshit Rawat

## Features
- Create a new task
- Retrieve all tasks
- Get a specific task by ID
- Update a task
- Delete a task

## Prerequisites
Ensure you have the following installed:
- Python (3.x)
- XAMPP (for MySQL database)
- Required Python packages

## Setup Instructions

### 1. Start MySQL in XAMPP
- Open **XAMPP Control Panel**
- Click **Start** for **Apache** and **MySQL**
- Open **phpMyAdmin** (http://localhost/phpmyadmin)

### 2. Create MySQL Database
1. Open **phpMyAdmin**
2. Click **New**, enter database name (e.g., `task_db`), and click **Create**

### 3. Install Required Packages
Run the following command in your terminal:
```bash
pip install -Ur requirements.txt
```

### 4. Configure Database in `app.py`
Update the Flask database configuration:
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/task_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

### 5. Run the Flask Application
```bash
python app.py
```
The API will be available at: `http://127.0.0.1:5000/`

## API Endpoints

| Method | Endpoint            | Description          |
|--------|---------------------|----------------------|
| POST   | `/tasks`            | Create a new task   |
| GET    | `/tasks`            | Retrieve all tasks  |
| GET    | `/tasks/<id>`       | Get a task by ID    |
| PUT    | `/tasks/<id>`       | Update a task       |
| DELETE | `/tasks/<id>`       | Delete a task       |

## Example Task JSON
```json
{
  "title": "Buy Groceries",
  "description": "Milk, Eggs, Bread",
  "due_date": "2025-03-10",
  "status": "Pending"
}
```

## Testing
Use **Postman** or **cURL** to test the API.

## License
This project is open-source and free to use.

