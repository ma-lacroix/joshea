# Makefile

IMAGE_NAME = flask-app

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 5000:5000 $(IMAGE_NAME)

build-and-run: build run
