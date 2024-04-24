FROM python:3.12-slim
LABEL authors="dgkngk"

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "makemigrations"]

CMD ["python", "manage.py", "migrate"]

CMD ["python", "manage.py", "createsuperuser", "--username", "$DJANGO_SUPERUSER_USERNAME", "--email", "$DJANGO_SUPERUSER_EMAIL"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]