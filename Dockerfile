FROM python:3.10-slim

ENV PYTHONBUFFERED 1

WORKDIR /home_library

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]