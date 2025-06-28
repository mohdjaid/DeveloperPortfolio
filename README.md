# DeveloperPortfolio
A full-stack web application that allows developers to register, submit, and manage their portfolios — including bio, skills, and projects.

Built with Django (REST API) + React.js (Frontend)


## Features

- User Registration & Login (JWT Auth)
- Create/Edit/Delete Developer Portfolio
- Submit:
  - Name, Email, Short Bio
  - Skills (add custom ones)
  - Projects (title, description, tech stack, GitHub/demo links)
- View Submissions
- Form validation & feedback messages
- Auth-protected frontend (React) using Axios

---

## Setup Instructions
-- Backend part
django-admin startproject portfolioproject
cd portfolioproject
python manage.py startapp portfolioApp
-- frontent
npm create vite@latest frontend
cd frontend
npm install
## Backend (Django + DRF)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt

# Migrate DB and start server
python manage.py migrate
python manage.py runserver
