# syntax=docker/dockerfile:1

FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr (so logs show up immediately in Cloud Logging)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . .

# Run as a non-root user
RUN useradd --create-home appuser
USER appuser

# Cloud Run injects the PORT env var (defaults to 8080); gunicorn binds to it at runtime
ENV PORT=8080
EXPOSE 8080

# app:app -> app.py module, "app" Flask instance
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
