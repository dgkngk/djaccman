FROM python:3.12-slim
LABEL authors="dgkngk"

WORKDIR .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN python manage.py createsuperuser --username "$DJANGO_SUPERUSER_USERNAME" --email "$DJANGO_SUPERUSER_EMAIL" --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]