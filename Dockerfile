FROM python:latest

WORKDIR /bot

COPY . /bot

RUN pip install .

CMD ["python", "main.py"]
