FROM python:3.9-alpine
COPY . /home/app
COPY requirements.txt /home/app/requirements.txt
WORKDIR /home/app
RUN pip install -r requirements.txt
CMD ["python", "setup.py"]


