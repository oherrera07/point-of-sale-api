FROM python:3.9-alpine
WORKDIR /home/app
ENV FLASK_APP setup.py
ENV FLASK_RUN_HOST 0.0.0.0
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]
