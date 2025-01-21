# Setup a docker container

## Installing Docker

OS specific steps : <https://docs.docker.com/engine/install/>
Get started guide : <https://docs.docker.com/get-started/>

## What is a docker container?

A Docker container is a standalone, executable package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and config files.

## What is a docker image?

A running container uses an isolated filesystem. This isolated filesystem is provided by an image, and the image must contain everything needed to run an application - all dependencies, configurations, scripts, binaries, etc. The image also contains other configurations for the container, such as environment variables, a default command to run, and other metadata.

## What is a Dockerfile?

It is a file that contains the steps to make a docker image i.e., it lists all the
dependencies, configurations, etc.,.

## Create a Dockerfile

Dockerfile: <./Dockerfile>

## Build a docker image

-   View existing docker images: `docker image ls`
-   Delete docker image: `docker image rm <image-id>`

```
    # docker build -t <image-name>:<tag> <directory>
    docker build -t mlops-pipeline:v1 .
```

## Run a docker container

-   View running docker containers: `docker container ls`
-   Delete docker container: `docker container rm <container-id>`

``` sh
    # docker run -d -p <host_port>:<container_port> --name <container name> <image name with tag>
    docker run -d -p 8000:80 --name mlops-pipeline:container mlops-pipeline:v1
```
