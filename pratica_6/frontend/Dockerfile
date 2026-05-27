FROM python:3.11-slim

WORKDIR /app

RUN pip install flask requests

COPY . .

EXPOSE 3000

CMD ["python", "app.py"]