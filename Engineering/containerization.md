# Containerization

- record dependencies and environment
- Docker

- image vs container
    - image is a file, container is a running instance of that file
    - DockerFile is a recipe for building an image
  

1. `docker build -t <image_name>:<tag> .`
    this create the image from the DockerFile in the current directory and tags it with the given name and tag.

2. `docker run -p <host_port>:<container_port> <image_name>:<tag>`
    this runs a container from the specified image and maps the container's port to the host's port.
   