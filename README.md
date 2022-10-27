# docker_k4a

Docker of a development environment for Microsoft Azure Kinect (k4a)

## Requirements (tested)

- Ubuntu 20.04 (arch=amd64)
  - RTX3080
    - NVIDIA Driver 470.141.03
  - docker 20.10.12
  - docker-compose 1.29.2
  - nvidia-docker2 2.8.0-1
- Microsoft Azure Kinect
  - [Azure-Kinect-Sensor-SDK](https://github.com/microsoft/Azure-Kinect-Sensor-SDK)  
  - [Azure_Kinect_ROS_Driver](https://github.com/microsoft/Azure_Kinect_ROS_Driver)  

## Installation

    $ git clone https://github.com/takuya-ki/docker_k4a.git --recursive --depth 1

## Usage
#### Host machine
    $ cd docker_k4a
    $ COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build --no-cache --parallel
    $ docker-compose up
    $ xhost +
    $ docker exec -it k4a_container bash

#### Docker container
    Please see the bash history.

## Author / Contibutor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
