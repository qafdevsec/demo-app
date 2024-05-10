FROM python:3.13.0b1-slim
RUN apt update && apt install -y curl
COPY requirements.txt /requirements.txt
COPY app.py /app.py
RUN pip install --upgrade pip
COPY config.py config.py
COPY app app
# COPY lmomesso/Lib/site-packages /usr/local/lib/python3.9/site-packages
RUN pip install -r requirements.txt
# ADD . /app
ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]