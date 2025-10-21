# 📝 Todo App with Flask, MongoDB, and Docker

A modern and responsive **ToDo List** web application built with **Flask** and **MongoDB**, styled with clean HTML/CSS, and containerized using **Docker & Docker Compose**.

![App Screenshot](https://via.placeholder.com/900x500.png?text=Todo+App+Screenshot)

---

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

- git clone https://github.com/your-username/your-repo-name.git
- cd your-repo-name

## Build & start services
- docker-compose up --build

## Make sure requirements.txt includes
- flask
- pymongo

## If you're running it locally (without Docker), install with
- pip install -r requirements.txt

![App Screenshot](https://via.placeholder.com/900x500.png?text=Todo+App+Screenshot)
