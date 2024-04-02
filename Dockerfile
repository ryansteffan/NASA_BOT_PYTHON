FROM python:latest

WORKDIR /bot

COPY ./conf /bot/conf

COPY ./src /bot/src

COPY ./main.py /bot

COPY ./requirements.txt /bot

VOLUME /bot/conf/

RUN pip install -r ./requirements.txt

CMD ["python", "main.py"]
