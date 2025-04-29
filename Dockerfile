# Use official Python image
FROM python:3.12-slim

# Install required system libraries
RUN apt-get update && apt-get install -y \
    gcc \
    libjpeg-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# 🔥 Create superuser with defaults
RUN python manage.py createsuperuser_with_defaults || true

# Expose port
EXPOSE 8000

# Command to run app
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
