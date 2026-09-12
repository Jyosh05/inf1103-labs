FROM python:3.11-slim

WORKDIR /app

COPY Week2_Lab/auditor.py .

CMD ["python", "auditor.py"]