# 🔗 LinkShort — Modern URL Shortener with Flask

LinkShort is a **full-stack URL shortener** built using **Flask**, featuring **user authentication**, **guest sessions**, and a **modern dark-mode UI**.
It allows users to shorten URLs instantly and access their links from anywhere by logging in.

---

## 🚀 Live Features

* 🔗 **Instant URL Shortening**
* 👤 **User Authentication** (Signup / Login / Logout)
* 🧑‍💻 **Guest Mode**

  * Shorten links without logging in
  * Recent links stored per session
* 💾 **Persistent History for Logged-in Users**
* 📋 **One-click Copy to Clipboard**
* 🎨 **Modern Dark UI (Responsive)**
* 🔐 **Secure Password Hashing**
* 🔄 **Automatic Redirects for Short URLs**

---

## 🧠 Project Concept

This project demonstrates:

* Real-world **Flask application structure**
* **Flask-Login** for authentication
* **Session-based vs Database-based state handling**
* Handling both **guest users** and **authenticated users**
* Responsive frontend using **HTML + CSS (Dark Mode)**
* Secure backend practices

---

## 🛠 Tech Stack

| Layer      | Technology                 |
| ---------- | -------------------------- |
| Backend    | Python, Flask              |
| Database   | SQLite, SQLAlchemy         |
| Auth       | Flask-Login                |
| Security   | Werkzeug Password Hashing  |
| Frontend   | HTML, CSS (Custom Dark UI) |
| Deployment | Local / Render-ready       |
| Versioning | Git & GitHub               |

---

## 📂 Project Structure

```
linkshort-flask/
│
├── app.py
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── login.html
│   └── signup.html
├── instance/
├── __pycache__/
└── .gitignore
```

---

## 🔑 How It Works

### 1️⃣ Guest User

* Shorten URLs without login
* Recent links stored in browser session
* Data cleared after session ends

### 2️⃣ Logged-in User

* Shortened links stored in database
* Access links from any device after login
* Persistent history

---

## 🖥 Screenshots

>
![Home Page](/screenshots/home.png)
![Login](/screenshots/login.png)


---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/mayurks23/linkshort-flask.git
cd linkshort-flask
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## 🔐 Security Highlights

* Passwords stored using **hashed encryption**
* Login-protected routes
* Secure session handling
* Unique short URL generation

---

## 💡 Future Improvements

* 📊 Click analytics
* 🏷 Custom aliases
* 📅 Link expiration
* 🌍 Custom domains
* 🚀 Production deployment

---

## 👨‍💻 Author

**Mayur Kumar Sourav**
📌 Data Science | Backend | Flask Projects

🔗 [LinkedIn](https://linkedin.com)
💻 [GitHub](https://github.com/mayurks23)
📧 Email: [hey5134mayur18@gmail.com](mailto:hey5134mayur18@gmail.com)

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it motivates me to build more!
