# https://hub.docker.com/layers/library/python/3.10.0-alpine3.15/images/sha256-af98bfb921cfd4a693b89fb37bc3df83beb54ce761dabaf89611a8a97c22d78e?context=explore
FROM python:3.10.0-alpine3.15

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src

EXPOSE 5000

# retries 5 times with 30s intervals and mark as fail if it fails to start
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1

ENTRYPOINT ["python", "./src/app.py"]
