FROM python:3.14.0a4-slim-bullseye
WORKDIR /src


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
