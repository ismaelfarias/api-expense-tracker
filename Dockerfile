FROM python:3.12-alpine3.21

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /app

EXPOSE 8000

CMD [ "fastapi", "run", "main.py", "--port", "8000" ]