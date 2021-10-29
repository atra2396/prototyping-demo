FROM python:3.9-slim
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT uvicorn api:app --host 0.0.0.0