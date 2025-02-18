# Makefile

# Define the image name
IMAGE_NAME = flask-app

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -p 5000:5000 $(IMAGE_NAME)

# Remove the Docker container (optional, for cleanup)
clean:
	docker rm -f $(docker ps -a -q)

# Remove the Docker image (optional, for cleanup)
clean-image:
	docker rmi $(IMAGE_NAME)

# Rebuild and run the Docker container
rebuild:
	clean build run

build-and-run: build run
