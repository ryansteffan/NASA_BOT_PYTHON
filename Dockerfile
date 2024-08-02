FROM python:latest

WORKDIR /bot

RUN mkdir -p /var/log/supervisor && mkdir -p /bot/logs

RUN touch /bot/logs/nasa_bot.log

COPY ./conf /bot/conf

COPY ./src /bot/src

COPY ./main.py /bot

COPY ./requirements.txt /bot

COPY ./init.sh /init.sh

VOLUME /bot/conf/

RUN pip install -r ./requirements.txt && \
    apt update && \
    apt install -y supervisor

RUN chmod 755 /init.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/init.sh"]