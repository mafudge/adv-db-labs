FROM python:3.8-slim 

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ENV FLASK_APP=app.py

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "-m",  "flask", "run", "--host=0.0.0.0" ]