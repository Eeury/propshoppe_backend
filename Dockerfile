FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt
COPY . .
RUN python manage.py collectstatic --noinput
ENV PYTHONUNBUFFERED=1
ENV PORT=10000
# Ensure you have a .dockerignore file to avoid copying unnecessary files like venv/, .git/, etc.
EXPOSE 10000
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT prop_shoppe.wsgi:application"]