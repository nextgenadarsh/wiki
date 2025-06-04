# Docker

> Getting started with docker

    `docker run -d -p 8080:80 docker/getting-started` OR
    `docker run -dp 8080:80 docker/getting-started`

- -d - Run the container in detached mode (in the background)
- -p 8080:80 - Map port 8080 of the host to port 80 in the container
- docker/getting-started - The image to use