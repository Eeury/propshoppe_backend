
FROM python:3.10-slim

WORKDIR /app


COPY . .


RUN pip install --upgrade pip
RUN pip install -r requirements.txt



ENV PYTHONUNBUFFERED=1


CMD ["gunicorn", "prop_shoppe.wsgi:application", "--bind", "0.0.0.0:8000"]
