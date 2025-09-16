# VERO Backend

Backend service for **VERO**, a project I'm building with friends.  
Built in **Python (Django)** with a **Postgres** database and deployed on **Render**.

## 🚀 Tech Stack
- Python 3 / Django
- PostgreSQL (managed on Render)
- Gunicorn (production server)
- Deployed via Render (Web Service + Postgres)
- Frontend built separately using **v0 (Vercel, React + Tailwind)**

## 🌐 Live Endpoints
- `/` → Health check (`VERO API is live ✅`)
- `/ping/` → Test endpoint (returns JSON `{"message": "pong 🏓"}`)
- `/admin/` → Django Admin (with Postgres)

## 🔑 Highlights
- Secure environment variables on Render (`SECRET_KEY`, `DATABASE_URL`, etc.)
- Django admin + superuser configured
- Postgres migrations applied in production
- Ready for user authentication endpoints (signup/login) and connection to the v0 frontend