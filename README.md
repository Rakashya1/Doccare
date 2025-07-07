# 🩺 Doccare – Doctor Appointment & Prescription Management System

Doccare is a comprehensive web-based platform that simplifies appointment scheduling, prescription handling, and patient-doctor interaction. It features intuitive dashboards, calendar-based scheduling, and a powerful rich text editor for prescription creation.

---

## 🚀 Features

- **Doctor & Patient Dashboards** — Separate interfaces with role-specific controls
- **Appointment Booking** — Patients can book, view, and cancel appointments
- **Prescription Management** — Doctors can issue, edit, and view prescriptions
- **Calendar Integration** — FullCalendar-based visual schedule
- **Rich Text Editing** — CKEditor 4 for notes and prescriptions
- **Notifications** — In-app alerts for appointments and updates
- **Responsive UI** — Works seamlessly across all devices

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS, JavaScript, jQuery |
| **Editor** | [CKEditor 4](https://ckeditor.com/ckeditor-4/) |
| **Calendar** | [FullCalendar](https://fullcalendar.io/) |
| **Charts** | Morris.js |
| **UI Plugins** | Select2, Fancybox, Slick Carousel |

---

## 📁 Directory Structure

```plaintext
doccare/
├── static/
│   ├── assets/
│   │   ├── css/        → Stylesheets
│   │   ├── js/         → JavaScript files
│   │   └── plugins/    → FullCalendar, Fancybox, etc.
│   ├── ckeditor/       → CKEditor 4 and its plugins
│   └── dashboard/      → Admin and doctor dashboards
├── templates/          → HTML views
├── media/              → Uploaded files
└── requirements.txt    → Python dependencies
```

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/doccare.git
   cd doccare
   ```

2. **Set Up Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup**
   ```bash
   python manage.py migrate
   ```

5. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**
   
   Open your browser and navigate to: [http://localhost:8000/](http://localhost:8000/)

---

## 👤 User Roles

### Doctors
- Log in to access doctor dashboard
- View patient history and medical records
- Manage appointments and schedules
- Write and manage prescriptions

### Patients
- Register for new account
- Book appointments with available doctors
- View prescription history
- Manage personal health records

### Admins (Optional)
- Manage system-wide settings
- Oversee user accounts and permissions
- Monitor system data and analytics

---

## 📦 Dependencies & Licenses

### Third-Party Libraries
- **CKEditor 4** — GPL, LGPL, or MPL License
- **FullCalendar** — MIT License
- **Morris.js** — BSD License
- **Select2** — MIT License
- **Fancybox** — GPLv3 License
- **Slick Carousel** — MIT License

### Backend Dependencies
- **Django** — BSD License
- **Python** — Python Software Foundation License


---

## 🛡️ Production Deployment

For production environments, consider the following:

- **Environment Variables**: Use `.env` files with `python-decouple` for sensitive data
- **Database**: Configure PostgreSQL or MySQL instead of SQLite
- **Web Server**: Set up Nginx with Gunicorn/Uvicorn for better performance
- **Security**: Enable HTTPS, configure CORS, and implement proper authentication
- **Monitoring**: Set up logging and error tracking


---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

### Third-Party License Notice

Third-party libraries and plugins included in this project retain their own licenses:
- **CKEditor 4** and its plugins: GPL, LGPL, or MPL (see `static/ckeditor/ckeditor/README.md`)
- **FullCalendar**: MIT License
- **Morris.js, Select2, Fancybox, and others**: See respective documentation for license details

Please ensure compliance with all third-party licenses when using or distributing this project.

---

