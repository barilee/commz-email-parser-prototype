
# Commz Email Parser Prototype

This is a working prototype for extracting structured data from emails and attached documents (e.g., invoices, resumes). It uses **FastAPI** for backend logic and **React (Vite)** for the frontend UI.

---

## 📦 Repo Structure

```
commz-email-parser-prototype/
├── backend/          # FastAPI backend
│   ├── main.py
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/         # React frontend (Vite)
│   ├── src/
│   ├── public/
│   └── .env.example
│
└── README.md
```

---

## 🚀 Local Setup

### 🔧 Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

> Copy `.env.example` to `.env` and set Gmail API credentials.

### 💻 Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

> Copy `.env.example` to `.env` and set:
```
VITE_API_BASE_URL=http://localhost:8000
```

---

## ☁️ Deployment

### 🧠 Backend → [Railway](https://railway.app)

1. New Project → Deploy from GitHub
2. Set root to `backend/`
3. Define build/start commands:
   - Build: `pip install -r requirements.txt`
   - Start: `uvicorn main:app --host 0.0.0.0 --port 8000`
4. Set environment variables from `.env`

### 🌐 Frontend → [Vercel](https://vercel.com)

1. New Project → Import from GitHub
2. Set root to `frontend/`
3. Add env:
   ```
   VITE_API_BASE_URL=https://your-backend-url.up.railway.app
   ```

---

## 👥 Team Setup

- Use **GitHub branches** like `feat/frontend-ui`, `feat/backend-parser`
- Use **issues & PRs** to track work and keep clean commit logs
- Add collaborators in GitHub under `Settings > Collaborators`

---

## ✅ First Push Instructions

```bash
git init
git remote add origin https://github.com/YOUR_USERNAME/commz-email-parser-prototype.git
git add .
git commit -m "chore: initial commit with backend and frontend scaffolding"
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

---

Happy Hacking! 🔧🚀
