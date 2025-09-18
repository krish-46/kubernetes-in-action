FROM python:3.11-slim
WORKDIR /opt/app
COPY app.py .
RUN pip install --no-cache-dir flask
EXPOSE 8080
ENTRYPOINT ["python", "app.py"]
