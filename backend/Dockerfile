FROM python:3.12.5
WORKDIR /src


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
