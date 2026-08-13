FROM python:3.11-slim

WORKDIR /app/backend

# Copy requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend application
COPY backend/ .

# Collect static files
RUN python manage.py collectstatic --noinput || true

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PORT=8000

# Run gunicorn
CMD ["gunicorn", "todp.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
