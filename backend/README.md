# Todo App - Django Backend

A Django-based Todo application backend with user authentication and todo management.

## Features

- User registration and authentication
- Create, read, update, delete todos
- User-specific todo lists
- Secure and production-ready

## Prerequisites

- Python 3.8+
- pip

## Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create .env File

Copy `.env.example` to `.env` and update with your values:

```bash
cp .env.example .env
```

Update the following in `.env`:

```
DEBUG=False
SECRET_KEY=your-strong-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com
CORS_ALLOWED_ORIGINS=http://localhost:3000,https://your-vercel-frontend.vercel.app
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 7. Run Development Server

```bash
python manage.py runserver
```

Server will be available at `http://localhost:8000`

## Deployment on Railway

### 1. Connect to Railway

- Go to [Railway.app](https://railway.app)
- Click "New Project"
- Select "Deploy from GitHub"
- Connect your GitHub repo containing this backend folder

### 2. Set Environment Variables on Railway

Add these environment variables in Railway dashboard:

- `PYTHON_VERSION`: 3.11
- `SECRET_KEY`: Generate a strong secret key
- `DEBUG`: False
- `ALLOWED_HOSTS`: your-railway-domain.railway.app
- `CORS_ALLOWED_ORIGINS`: https://your-vercel-frontend.vercel.app

### 3. Deploy

Railway will automatically:

- Install dependencies from `requirements.txt`
- Run migrations
- Start the app using `Procfile`

### 4. Get Your Backend URL

Once deployed, Railway provides a public URL like:

```
https://todp-production.railway.app
```

## API Endpoints

### Authentication

- `POST /signup/` - Register new user
- `POST /index/` - Login
- `GET /logout/` - Logout

### Todos

- `GET /todo/` - Get all todos (requires login)
- `POST /todo/` - Create new todo (requires login)
- `GET /edit_todo/<id>/` - Edit todo page (requires login)
- `POST /edit_todo/<id>/` - Update todo (requires login)
- `GET /delete_todo/<id>/` - Delete todo (requires login)

## Frontend Integration

Update your frontend's API base URL to match your deployed backend:

```javascript
const API_URL = "https://your-railway-backend.railway.app";

// Example API call
fetch(`${API_URL}/todo/`, {
  method: "GET",
  credentials: "include",
});
```

## Database

Currently uses SQLite. For production with multiple instances, consider PostgreSQL:

```bash
pip install psycopg2-binary
```

Update `DATABASES` in settings.py to use PostgreSQL.

## Security Tips

1. ✅ Change `SECRET_KEY` to a strong random string
2. ✅ Set `DEBUG = False` in production
3. ✅ Update `ALLOWED_HOSTS` with your domain
4. ✅ Use HTTPS in production
5. ✅ Keep dependencies updated: `pip list --outdated`

## Troubleshooting

**Issue**: `ModuleNotFoundError: No module named 'django'`

- Solution: Activate virtual environment and run `pip install -r requirements.txt`

**Issue**: `DisallowedHost` error

- Solution: Add your domain to `ALLOWED_HOSTS` in settings.py or `.env`

**Issue**: CORS errors from frontend

- Solution: Update `CORS_ALLOWED_ORIGINS` in settings.py with your frontend URL

## Support

For issues and questions, please open an issue on GitHub.

## License

MIT License
