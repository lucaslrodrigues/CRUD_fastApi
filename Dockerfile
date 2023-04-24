FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

CMD ["make","run-server"]

EXPOSE 8001
EXPOSE 5433