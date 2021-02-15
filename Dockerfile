FROM python:3.7

WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY app.py /app/app.py

RUN pip install -r /app/requirements.txt

CMD PYTHONPATH=$PYTHONPATH:/app FLASK_APP=app.py flask run --host=0.0.0.0