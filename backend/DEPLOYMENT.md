# Deployment Steps - Quick Guide

## 📁 Folder Structure Created

Your backend folder is ready with this structure:

```
backend/
├── manage.py
├── requirements.txt
├── Procfile
├── runtime.txt
├── .env.example
├── .gitignore
├── README.md
└── todp/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── asgi.py
    ├── models.py
    ├── settings.py
    ├── urls.py
    ├── views.py
    ├── wsgi.py
    ├── migrations/
    ├── static/
    └── templates/
```

## 🚀 Quick Deployment Steps

### 1. **Add Backend Folder to GitHub** (5 mins)

```bash
# In your repo root
git add backend/
git commit -m "Add Django backend for deployment"
git push origin main
```

### 2. **Deploy on Railway** (10 mins)

1. Go to [railway.app](https://railway.app)
2. Login with GitHub
3. Click "New Project" → "Deploy from GitHub"
4. Select your repository
5. Railway auto-detects Django and creates deployment

### 3. **Set Environment Variables** (5 mins)

In Railway Dashboard → Variables:

- `PYTHON_VERSION`: 3.11
- `SECRET_KEY`: Generate a random key (use online generator)
- `DEBUG`: False
- `ALLOWED_HOSTS`: your-railway-app.railway.app
- `CORS_ALLOWED_ORIGINS`: https://your-vercel-frontend.vercel.app

### 4. **Deploy** (2 mins)

Click "Deploy" button → Wait 2-3 minutes → Get your backend URL

### 5. **Connect Frontend to Backend** (5 mins)

Update your Vercel frontend code to use the Railway backend URL.

---

**Total Time: ~30 minutes to full deployment!**

## 🔗 Connecting Frontend & Backend

Update your frontend JavaScript:

```javascript
// Set this to your Railway backend URL
const API_BASE = "https://your-railway-app.railway.app";

// Example: Fetch todos
fetch(`${API_BASE}/todo/`, {
  method: "GET",
  credentials: "include",
});
```

## ✅ Verification Checklist

- [ ] Backend folder added to GitHub
- [ ] Railway project created and connected
- [ ] Environment variables set in Railway
- [ ] Deployment completed (check Railway logs)
- [ ] Backend URL obtained
- [ ] Frontend updated with backend URL
- [ ] Test login/signup works
- [ ] Test create/edit/delete todos

---

**Need Help?** Check the README.md file for detailed troubleshooting.
