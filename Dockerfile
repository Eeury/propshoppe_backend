
FROM python:3.10-slim


WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt


COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 10000

CMD ["gunicorn", "--bind", "0.0.0.0:${PORT:-10000}", "prop_shoppe.wsgi:application"]