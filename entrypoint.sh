#!/bin/sh

echo "🚀 Starting Django setup..."

echo "🔁 Applying database migrations..."
python manage.py migrate --noinput

echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo "👤 Creating superuser (if not exists)..."
python manage.py createsuperuser_with_defaults || true

echo "🔥 Starting Gunicorn server..."
exec gunicorn backend.wsgi:application --bind 0.0.0.0:8000
