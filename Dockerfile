FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
CMD ["flask", "run"]
