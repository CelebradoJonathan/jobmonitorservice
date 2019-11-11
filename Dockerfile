FROM python:3

RUN apt-get update -y
WORKDIR /app
COPY . /app
RUN pip install flask gunicorn
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "localhost:8000", "app:app"]