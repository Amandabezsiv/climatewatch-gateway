FROM python:3.13-slim

WORKDIR /app

COPY requeriments.txt requeriments.txt
RUN pip install --no-cache-dir -r requeriments.txt

COPY . .

COPY .env .env

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]