# ☁️ Cloud Based Student Attendance Tracker
### Smart Attendance. Seamless Management. Secure Access.

<p align="center">
  <img src="https://img.shields.io/badge/Project-Final%20Year-blueviolet?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Under%20Development-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Access-Role%20Based-blue?style=for-the-badge" />
</p>

<p align="center">
  **A smart, secure, and cloud-based solution designed to simplify student attendance management through role-based access and centralized data handling.**
</p>

---

## 🌟 About The Project

The **Cloud Based Student Attendance Tracker** is a web-based application developed to modernize the traditional attendance management process.

The system provides a centralized platform where administrators, faculty members, and students can access attendance-related information according to their assigned roles.

It aims to reduce manual paperwork, improve accuracy, save time, and make attendance records easily accessible.

## 🎯 Project Objectives

- ☁️ Develop a centralized cloud-based attendance management system.
- 🔐 Implement secure authentication and role-based access control.
- 👨‍💼 Provide separate dashboards for Admin, Faculty, and Students.
- 📊 Simplify attendance tracking and report management.
- ⚡ Reduce manual work and human errors.
- 📱 Provide an easy-to-use and responsive interface.

## 👥 User Roles & Features

| Role | Responsibilities |
|---|---|
| 👨‍💼 Admin | Manage users, students, faculty, and overall attendance records. |
| 👩‍🏫 Faculty | Manage classes, mark attendance, and view attendance reports. |
| 🎓 Student | View personal attendance records and attendance percentage. |

## ✨ Key Features

- 🔑 Secure Login & Authentication
- 🛡️ Role-Based Access Control
- 📊 Admin Dashboard
- 👩‍🏫 Faculty Dashboard
- 🎓 Student Dashboard
- 📝 Attendance Management
- 📈 Attendance Reports
- ☁️ Centralized Data Management
- 🎨 User-Friendly Interface

## 🛠️ Technology Stack

### Frontend
- React.js
- JavaScript
- HTML5
- CSS3

### Backend
- Python
- FastAPI

### Database
- PostgreSQL

### Tools & Technologies
- Visual Studio Code
- Git & GitHub
- Postman
- pgAdmin

## 🏗️ System Architecture

```text
             USERS
               |
       -----------------
       |       |       |
     Admin  Faculty  Student
       |       |       |
       -----------------
               |
        React Frontend
               |
          REST API
               |
         FastAPI Backend
               |
          PostgreSQL
               |
       Attendance Database
```

## 📂 Project Structure

```text
Cloud-Attendance-Tracker/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── layouts/
│   │   ├── context/
│   │   └── services/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── routers/
│   ├── models/
│   ├── schemas/
│   └── requirements.txt
│
├── Documentation/
│
├── Presentation/
│
├── Screenshots/
│
└── README.md
```

*Note: Update the folder structure according to the actual project files.*

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Cloud-Based-Student-Attendance-Tracker.git
```

### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

### 3. Backend Setup

Open a new terminal:

```bash
cd backend
python -m venv venv
```

Activate virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

### 4. Database Configuration

- Install PostgreSQL.
- Create the project database.
- Configure database connection details in your local environment file.
- Start the backend server.

## 📸 Project Screenshots

Screenshots of the application will be added here.

| Login Page | Admin Dashboard |
|---|---|
| Coming Soon | Coming Soon |

| Faculty Dashboard | Student Dashboard |
|---|---|
| Coming Soon | Coming Soon |

## 📚 Documentation

Project-related documents will be available in the `Documentation/` directory.

- Project Abstract
- Project Synopsis
- Software Requirements Specification (SRS)
- Detailed Project Report
- Project Presentation

## 🔮 Future Enhancements

- 📲 Mobile-friendly attendance management.
- 📧 Automated attendance notifications.
- 📊 Advanced analytics and visual reports.
- 📥 Export attendance reports in PDF and Excel.
- 🔔 Low attendance alerts.
- ☁️ Improved cloud deployment and scalability.

## 👩‍💻 Development Team

| Team Member | Role |
|---|---|
| Durga | Project Development |
| Shital | Project Development |
| Jyoti | Project Development |
| Rutuja | Project Development |

**Project Guide:** Sonali Panchal

## 🎓 Academic Project

Developed as a **B.Tech Computer Science & Engineering Final Year Project**.

**Institution:** MGM's College of Engineering, Nanded, Maharashtra, India.

---

<p align="center">
  ### 💙 Making Attendance Management Smarter!
  <br/>
  <b>Built with dedication, teamwork, and technology.</b>
</p>
