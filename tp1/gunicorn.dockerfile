FROM python:3.6.4
WORKDIR /app/py
RUN pip install flask gunicorn
