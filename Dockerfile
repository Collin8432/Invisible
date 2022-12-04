FROM python:3.10-slim


WORKDIR .


COPY requirements.txt .


RUN python -m pip install -r requirements.txt


COPY . .


CMD ["python3", "app.py"]
