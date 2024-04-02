FROM python:latest

WORKDIR /bot

COPY . /bot

RUN pip install -r ./requirements.txt

CMD ["python", "main.py"]
