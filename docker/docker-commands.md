# Docker CheatSheet

## Container Management

| Command                                   | Purpose
| --                                        | --
| `docker ps`                               | list running containers
| `docker ps -a`                            | list all containers 
| `docker create <image>`                   | create container from given image without running
| `docker rename <container> <new-name>`    | rename container
| `docker rm <container>`                   | delete container if not running
| `docker rm -f <container>`                | delete container event if running
| `docker logs <container>`                 | view logs of running container
| `docker events <container>`               | view real-time events for a container
| `docker update <container>`               | update configuration of one or more containers
| `docker port <container>`                 | view port mapping of a container
| `docker top <container>`                  | show running processes in a container
| `docker stats <container>`                | view live resource usage statistics for a container
| `docker diff <container>`                 | show changes to files or directories on the filesystem
| `docker cp <file-path> CONTAINER:<path>`  | copy a local file to a directory in a container

## Services

| Command                                               | Purpose
| --                                                    | --
| `docker service create --replicas=100 <image>`        | create 100 services of the image

## Running Container

| Command                                               | Purpose
| --                                                    | --
| `docker run <image> <command>`                        | run a command in a container based on an image
| `docker run --name <container-name> <image>`          | create, start, and provide a custom name for the container
| `docker run -p <host-port>:<container-port> <image>`  | run container from image by mapping a host port to a container port
| `docker run --rm <image>`                             | run a container and remove it after it stops
| `docker run -d <image>`                               | run a detached (background) container
| `docker run -it <image>`                              | start an interactive process, such as a shell, in a container
| `docker start <container>`                            | start a container
| `docker stop <container>`                             | stop running container
| `docker restart <container>`                          | restart running container
| `docker pause <container>`                            | pause processes in a running container
| `docker unpause <container>`                          | resume processes in a running container
| `docker wait <container>`                             | block a container until others stop (after which it prints their exit codes)
| `docker kill <container>`                             | kill a container by sending a SIGKILL to a running container
| `docker attach <container>`                           | attach local standard input, output, and error streams to a running container
| `docker exec -it <container> <shell>`                 | run a shell inside a running container

## Image Management

| Command                                               | Purpose
| --                                                    | --
| `docker build <dockerfile-path>`                      | create an image from a Dockerfile
| `docker build .`                                      | build an image from a Dockerfile located in the current directory
| `docker build -t <name>:<tag> <dockerfile-path>`      | create an image from a Dockerfile and tag it
| `docker build -f <file-path>`                         | specify a file to build from
| `docker pull <image>`                                 | pull an image from a registry
| `docker push <image>`                                 | push an image to a registry
| `docker import <url/file>`                            | create an image from a tarball
| `docker commit <container> <new-image>`               | create an image from a container
| `docker tag <image> <image>:<tag>`                    | tag an image
| `docker images`                                       | show all locally stored top-level images
| `docker history <image>`                              | show history for an image
| `docker rmi <image>`                                  | remove an image
| `docker load --image <tar-file>`                      | load an image from a tar archive or stdin
| `docker save <image> &gt; <tar-file>`                 | save an image to a tar archive file
| `docker image prune`                                  | remove unused images


## Networking

| Command                                               | Purpose
| --                                                    | --
| `docker network ls`                                   | list available networks
| `docker network rm <network>`                         | remove one or more networks
| `docker network inspect <network>`                    | show information on one or more networks
| `docker network connect <network> <container>`        | connect a container to a network
| `docker network disconnect <network> <container>`     | disconnect a container from a network

## General Management

| Command                                               | Purpose
| --                                                    | --
| `docker login`                                        | log in to a Docker registry
| `docker logout`                                       | log out of a Docker registry
| `docker inspect <object>`                             | list low-level information on Docker objects
| `docker version`                                      | show the version of the local Docker installation
| `docker info`                                         | display information about the system
| `docker system prune`                                 | remove unused images, containers, and networks

## Plugin Management

| Command                                               | Purpose
| --                                                    | --
| `docker plugin enable <plugin>`                       | enable a Docker plugin
| `docker plugin disable <plugin>`                      | disable a Docker plugin
| `docker plugin create <plugin> <path-to-data>`        | create a plugin from config.json and rootfs
| `docker plugin inspect <plugin>`                      | view details about a plugin
| `docker plugin rm <plugin>`                           | remove a plugin
