FROM python:3.11-alpine

WORKDIR /app

COPY . /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup


RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt --no-cache \
    && apk del .build-deps \
    && rm -rf /root/.cache

RUN chown -R appuser:appgroup /app

USER appuser

#порт для Flask
EXPOSE 5000


CMD ["python", "main.py"]