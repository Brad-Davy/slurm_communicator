# Use a lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure logs show immediately
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

