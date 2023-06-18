The repository demonstrates how to containerize machine learning applications using Docker, making it easy to package, deploy, and run them consistently across different environments.

# Docker Overview
### What is Docker?
Docker is a set of platform-as-a-service products that use OS-level virtualization to deliver software in packages called containers. The service has both free and premium tiers. The software that hosts the containers is called Docker Engine. Docker simplifies the process of managing and scaling applications, improving efficiency and collaboration in software development.

### Docker image
A Docker image is a lightweight, standalone, and executable software package that contains everything needed to run a piece of software, including the code, runtime, system tools, libraries, and dependencies. In simple words, it is a screenshot of entire program.

### Container
Containers are isolated environments that include the application and its dependencies, making it easier to ensure consistency and portability across different systems. In simple words, it is an environment where the images will be exceuted.

### Docker Hub
Docker Hub is a service provided by Docker for finding and sharing container images. There are Private repository too.

### Docker vs Virtual Machine
Both are used for virtualization.

![image](https://github.com/Susheel-1999/Docker-python_practices/assets/63583210/5deefb67-c3d8-4726-b69e-b637508aa1d4)

Docker - virtualize only application layer, smaller size, faster, Host OS dependent. <br>
VM - virtualize both application layer and OS kernel, larger size, slower, Host OS independent.

### Dockerfile - Building our own Docker Image
Blueprint for building image. It has separate syntax such as FROM, ENV, COPY, RUN, EXPOSE, CMD and More. The file name should be in a standard format like "Dockerfile".

### Docker Compose - Running multiple services
Compose is a tool for defining and running multi-container Docker applications. With Compose, we use a YAML file to configure our application's services.

### Docker Volumes
Data generate or used by the container will be deleted once the container is stopped. Docker volumes are a way to persist data and it is separate from the container's lifecycle.

### Docker Network
Used for creating communication within the images in the container.

# Docker Commands used
<i><b>To build a Docker image from a Dockerfile</b></i>: <br>
docker build -t [name]:[tag] [location of Dockerfile]

<i><b>To run a Docker image in detached mode</b></i>: <br>
docker run -d -p[host port]:[contianer port] [name]:[tag]

<i><b>If an image is already built and ran at least once, we can rerun the image using:</b></i>: <br>
docker start [docker container id/ docker image name]

<i><b>To stop the execution for Docker image</b></i>: <br>
docker stop [docker container id/ docker image name]

<i><b>To see the logs of the Docker image</b></i>: <br>
docker logs [docker container id/ docker image name]

<i><b>To delete a Docker image from the container</b></i>: <br>
docker remove [docker container id/ docker image name]

<i><b>To see the progress status of all Docker images</b></i>: <br>
docker ps -a

<i><b>To run the docker compose file</b></i>: <br>
docker compose -f docker_compose.yaml up -d

<i><b>To stop and remove docker compose file</b></i>: <br>
docker compose -f docker_compose.yaml down
