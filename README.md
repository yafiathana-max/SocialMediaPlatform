# Social Media Platform

A full-stack social media web application built with **Django**, allowing users to create profiles, publish posts, comment, like posts, and interact with other users.

## 🌐 Live Demo

**https://socialmediaplatform-yrui.onrender.com/**

## 💻 GitHub Repository

**https://github.com/yafiathana-max/SocialMediaPlatform**

## ✨ Features

* User registration and login
* User profiles
* Profile picture support
* Create and view posts
* Post comments
* Like and unlike posts
* Follow and unfollow users
* Followers and following counts
* Django admin panel
* Responsive web interface
* PostgreSQL database
* Production deployment on Render

## 🛠️ Technologies Used

* Python
* Django 6.1
* HTML5
* CSS3
* JavaScript
* SQLite for local development
* PostgreSQL for production
* Gunicorn
* WhiteNoise
* Render
* Git & GitHub

## 📂 Project Structure

```text
SocialMediaPlatform/
├── config/
├── posts/
├── social/
├── users/
├── static/
├── templates/
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore
```

## 🚀 Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/yafiathana-max/SocialMediaPlatform.git
cd SocialMediaPlatform
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## ☁️ Deployment

The application is deployed on **Render** using:

* Gunicorn as the production WSGI server
* WhiteNoise for static file serving
* PostgreSQL for the production database
* Environment variables for production configuration
* Automatic deployment from GitHub

## 🔮 Future Improvements

* Direct messaging
* Notifications
* Post image uploads
* Search functionality
* Pagination
* AJAX-based likes and comments
* REST API with Django REST Framework
* Improved mobile UI

## 👩‍💻 Author

**Thana Yafia**

GitHub:
https://github.com/yafiathana-max
