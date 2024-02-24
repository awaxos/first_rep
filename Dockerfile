FROM python:3.11-alpine3.18

WORKDIR /app
COPY ./* /app

CMD ["python3", "project.py"]