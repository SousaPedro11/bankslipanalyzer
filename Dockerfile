FROM python:3.10-alpine

ENV TZ=America/Sao_Paulo

RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add build-base && \
    apk add gcc && \
    apk add libffi-dev && \
    apk add musl-dev && \
    apk add openssl-dev && \
    apk add git && \
    apk add zsh git-zsh-completion && \
    apk del build-base && \
    apk add python3-dev && \
    apk add postgresql-dev && \
    rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir --upgrade pip

RUN pip install --no-cache-dir autopep8 flake8

RUN pip install --no-cache-dir poetry

COPY . /code
WORKDIR /code

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONPATH=.

RUN poetry config virtualenvs.create false

RUN poetry install

EXPOSE 80
CMD ["python", "-m", "app"]
