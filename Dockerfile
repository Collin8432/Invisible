FROM python:3.10-slim


WORKDIR .


COPY requirements.txt .


RUN pip3 install -r requirements.txt

 
COPY . .


CMD ["python", "waitress-serve --port=8080 --host=127.0.0.1 --call app:create_app"]
