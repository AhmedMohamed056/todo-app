# 📝 Todo App with Flask, MongoDB, and Docker

A modern and responsive **ToDo List** web application built with **Flask** and **MongoDB**, styled with clean HTML/CSS, and containerized using **Docker & Docker Compose**.

---<img width="1920" height="1000" alt="Screenshot 2025-10-21 at 17-05-43 📝 Todo List" src="https://github.com/user-attachments/assets/24aa275a-7af1-4953-8b48-77782004558b" />

<img width="1920" height="963" alt="Screenshot 2025-10-21 at 17-04-42 Edit Task" src="https://github.com/user-attachments/assets/5640fa6d-d310-4faa-95be-312a6dc9a724" />



## ✨ Features

- ✅ Add, edit, delete, and complete tasks
- ⏱️ Track task status (`now`, `later`, `done`)
- 🎯 Set task priority (`High`, `Medium`, `Low`)
- 📅 Optional due date
- 🧠 Intuitive, responsive design with beautiful UI
- 🐳 Easily deployable via Docker or Docker Compose

---

## 📦 Project Structure

```bash
.
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── Dockerfile             # Image configuration
├── docker-compose.yml     # Service orchestration
├── templates/
│   ├── index.html         # Main UI
│   └── edit.html          # Edit task page
└── static/                # (Optional) CSS/JS assets
```
## You can run the app instantly using the pre-built image
- docker run -d -p 5000:5000 ahmedmohamed056/todo-app-flaskapp

## Then open your browser and go to
- http://localhost:5000

## If you prefer building and running the app locally:

- git clone https://github.com/AhmedMohamed056/todo-app.git
- cd todo-app

## Build & start services
- docker-compose up --build

## Make sure requirements.txt includes
- flask
- pymongo

## If you're running it locally (without Docker), install with
- pip install -r requirements.txt

