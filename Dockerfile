FROM python:3.9-slim
RUN apt update && apt install -y curl
ADD requirements.txt /requirements.txt
ADD app.py /app.py
RUN pip install --upgrade pip
COPY config.py config.py
ADD app app
RUN pip install -r requirements.txt
# ADD . /app
ENV PORT 8080
CMD ["gunicorn", "app:app", "--config=config.py"]