
<!-- ================= HEADER ================= -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:064e3b,50:15803d,100:86efac&height=220&section=header&text=VRIKHSHAM&fontSize=65&fontColor=ffffff&fontAlignY=38&desc=Nature%2C%20Powered%20by%20Intelligence&descAlignY=60&descSize=20" width="100%" />

<br/>

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=600&size=23&duration=3000&pause=1000&color=16A34A&center=true&vCenter=true&width=750&lines=Your+Intelligent+Plant+Care+Companion+%F0%9F%8C%B1;Grow+Smarter%2C+Live+Greener+%F0%9F%8C%BF;AI-Powered+Plant+Health+Assistant+%F0%9F%A4%96;Making+Plant+Care+Simple+and+Smart+%F0%9F%8C%8D" alt="Typing SVG" />

<br/><br/>

<p>
  <img src="https://img.shields.io/badge/Project-VRIKHSHAM-15803d?style=for-the-badge&logo=leaflet&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
</p>

**An intelligent platform designed to make plant care easier, smarter, and more accessible.**

</div>

---

<!-- ================= ABOUT ================= -->

## 🌿 About VRIKHSHAM

**VRIKHSHAM** is an AI-powered plant care and garden management web application designed to help people understand, monitor, and care for their plants.

The platform aims to combine Artificial Intelligence with modern web technologies to provide intelligent plant identification, plant health analysis, personalized care recommendations, and smart garden management.

Our mission is simple:

> Make plant care smarter through technology and make the world greener through awareness.

---

## ✨ Key Features

<table>
<tr>
<td width="50%">

### 🤖 AI Plant Doctor
- Identify plants using images.
- Analyze possible plant diseases.
- Get intelligent treatment suggestions.

</td>
<td width="50%">

### 🌱 AI Plant Care Assistant
- Personalized plant care guidance.
- Watering and sunlight recommendations.
- Soil and fertilizer suggestions.

</td>
</tr>
<tr>
<td width="50%">

### 🪴 My Garden
- Add and manage personal plants.
- Store plant information.
- Monitor plant health.

</td>
<td width="50%">

### ⏰ Smart Reminders
- Watering reminders.
- Fertilizer schedules.
- Plant maintenance notifications.

</td>
</tr>
<tr>
<td width="50%">

### 📊 Plant Health History
- Maintain plant health records.
- Track previous observations.
- Monitor plant progress.

</td>
<td width="50%">

### 🌍 Multilingual Experience
- English support.
- Hindi support.
- Bengali support.

</td>
</tr>
</table>

---

## 🖼️ Project Preview

<div align="center">

<!-- Replace these placeholders with your actual screenshots later -->

| Homepage | Plant Doctor |
|:---:|:---:|
| Add homepage screenshot here | Add Plant Doctor screenshot here |

| My Garden | Smart Reminders |
|:---:|:---:|
| Add My Garden screenshot here | Add Reminders screenshot here |

</div>

---

## 🛠️ Technology Stack

<div align="center">

| Technology | Purpose |
|:---|:---|
| Python | Backend programming |
| Flask | Web application framework |
| PostgreSQL | Relational database |
| Flask-SQLAlchemy | Database ORM |
| HTML5 | Page structure |
| CSS3 | Styling and responsive design |
| JavaScript | Frontend interactions |
| Gemini API | Planned AI integration |
| Git & GitHub | Version control |

</div>

---

## 📂 Project Structure

```text
VRIKHSHAM/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── .env
├── .gitignore
│
├── routes/
│   ├── __init__.py
│   ├── main.py
│   └── auth.py
│
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── plant.py
│   ├── garden.py
│   └── reminder.py
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── plant_doctor.html
│   ├── plant_care.html
│   ├── my_garden.html
│   ├── reminders.html
│   ├── health_history.html
│   ├── register.html
│   └── login.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
│
└── uploads/
```

---

## ⚙️ Installation & Setup

Follow these steps to run VRIKHSHAM locally.

### 1. Clone the repository

```bash
git clone https://github.com/MRIDUL11-prog/VRIKHSHAM.git
```

### 2. Navigate to the project folder

```bash
cd VRIKHSHAM
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the root directory.

```env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/vriksham_db
```

Replace `YOUR_PASSWORD` with your local PostgreSQL password.

**Important:** Never upload your `.env` file or expose your database credentials.

### 7. Create the PostgreSQL database

Open pgAdmin 4 and create a database named:

```text
vriksham_db
```

### 8. Run the application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000/
```

---

## 🚀 Development Roadmap

| Phase | Development | Status |
|:---|:---|:---|
| Day 1 | Project setup and Flask configuration | ✅ Completed |
| Day 2 | Frontend pages and navigation | ✅ Completed |
| Day 3 | PostgreSQL and database models | ✅ Completed |
| Day 4 | User registration and login | ✅ Completed |
| Day 5 | Authentication and user-specific data | ✅ Completed |
| Days 6–8 | My Garden Management | 🔄 Planned |
| Days 9–11 | Smart Reminders | 📌 Upcoming |
| Days 12–14 | Plant Health History | 📌 Upcoming |
| Days 15–18 | AI Plant Doctor | 📌 Upcoming |
| Days 19–21 | AI Plant Care Assistant | 📌 Upcoming |
| Days 22–24 | Admin Dashboard | 📌 Upcoming |
| Days 25–27 | Advanced Features | 📌 Upcoming |
| Days 28–30 | Testing and Deployment | 📌 Upcoming |

---

## 🔐 Security

VRIKHSHAM follows important security practices:

- Password hashing for user authentication.
- Environment variables for sensitive configuration.
- User-specific database queries.
- Git ignore rules for private files.
- Session-based authentication.

Security will continue to improve throughout development.

---

## 🌟 Future Vision

Our future goals include:

- Advanced AI-based plant disease detection.
- Personalized plant care recommendations.
- Weather-aware watering suggestions.
- Automated notification system.
- Interactive garden dashboard.
- Mobile-friendly experience.
- Multilingual support.

---

## 🤝 Contributing

Contributions, ideas, and suggestions are welcome!

If you would like to contribute:

1. Fork this repository.
2. Create a new feature branch.
3. Make your changes.
4. Commit your changes.
5. Submit a Pull Request.

---

## 👨‍💻 Developer

<div align="center">

### Developed with 💚 by

**MRIDUL SAHA**

BCA Student | Aspiring Software Developer

<a href="https://github.com/MRIDUL11-prog">
  <img src="https://img.shields.io/badge/GitHub-MRIDUL11--prog-181717?style=for-the-badge&logo=github" />
</a>

</div>

---

<div align="center">

### 🌱 Grow Smarter. Live Greener.

**VRIKHSHAM — Nature, Powered by Intelligence.**

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:86efac,50:15803d,100:064e3b&height=120&section=footer" width="100%" />

</div>
