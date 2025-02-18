FROM python:3.9

WORKDIR /joshea
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app
ENV FLASK_APP=app.main
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
