FROM python:3.11.6-bullseye

WORKDIR /bot

COPY . /bot

RUN pip install .

CMD ["python", "main.py"]
