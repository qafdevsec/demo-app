FROM python:3.9-slim
RUN apt update && apt install -y curl
COPY requirements.txt /requirements.txt
COPY app.py /app.py
RUN pip install --upgrade pip
COPY config.py config.py
COPY app app
RUN pip install -r requirements.txt
# ADD . /app
ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]