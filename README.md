# Full Stack Task Manager Web Application Using Python (Flask)

A Flask-based task management web application that allows users to register, log in, and manage their personal tasks. Built as part of learning Python web development using Flask.

## Task

Advanced Level Flask Project

## Features

* User Registration and Login
* User Authentication using Flask-Login
* Add New Tasks
* Delete Tasks
* SQLite Database Integration
* Separate Tasks for Each User
* Flash Messages for User Feedback
* Clean and Responsive User Interface

## Tech Stack

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* HTML
* CSS

## How it Works

1. Users create an account through the registration page.
2. Registered users can log in securely.
3. Each user can add and manage their own tasks.
4. Tasks are stored in an SQLite database.
5. Users can delete completed tasks.
6. Logging out redirects users back to the login page.

## Requirements

Install the required libraries before running:

```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-login
```

## How to Run

1. Clone the repository.
2. Navigate to the project folder.
3. Activate the virtual environment (optional).
4. Run:

```bash
python app.py
```

5. Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Project Structure

```text
TaskManager/
│
├── app.py
├── instance/
│   └── tasks.db
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── static/
│   └── style.css
│
└── venv/
```

## Screenshots

## Login Page

  <img width="412" height="339" alt="image" src="https://github.com/user-attachments/assets/fb0f2975-ab50-4ebf-9f0e-b65065075fd8" />
## Register Page

  <img width="391" height="329" alt="image" src="https://github.com/user-attachments/assets/937fa9e3-fc7a-4410-9903-0d3e2fc7afcb" />
## Dashboard

  <img width="428" height="401" alt="image" src="https://github.com/user-attachments/assets/5b698275-a86f-48dc-86f1-e0090b979fe9" />
## Task Management Interface

  <img width="470" height="446" alt="image" src="https://github.com/user-attachments/assets/d23a2896-3abe-4619-bf39-969cb74bf76c" />

## Author

Mariha Zia

## Repository Naming

synent-task9-taskmanager-marihazia
