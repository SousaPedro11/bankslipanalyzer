FROM python:3.10-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONPATH=/code
ENV TZ=America/Sao_Paulo

RUN cp /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone

WORKDIR /code

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

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /code/

RUN poetry install --no-root

COPY . /code/

CMD ["python", "-m", "app"]