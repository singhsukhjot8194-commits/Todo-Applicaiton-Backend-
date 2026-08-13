FROM python:3.11-slim

WORKDIR /app/backend

# Copy requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the backend application
COPY backend/ .

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV DEBUG=False

# Collect static files (ignore errors)
RUN python manage.py collectstatic --noinput 2>/dev/null || true

# Run gunicorn
CMD ["gunicorn", "todp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "2"]
