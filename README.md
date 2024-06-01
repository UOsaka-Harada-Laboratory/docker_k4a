# docker_k4a

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.svg)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![repo size](https://img.shields.io/github/repo-size/Osaka-University-Harada-Laboratory/docker_k4a)

Docker of a development environment for Microsoft Azure Kinect (k4a).

## Requirements (tested)

- [Ubuntu 20.04 PC](https://ubuntu.com/certified/laptops?q=&limit=20&vendor=Dell&vendor=Lenovo&vendor=HP&release=20.04+LTS) (22.04 is not supported)
  - NVIDIA GeForce RTX3080
    - NVIDIA Driver 470.141.03
  - docker 20.10.12
  - docker-compose 1.29.2
  - nvidia-docker2 2.8.0-1
- Microsoft Azure Kinect
  - [Azure-Kinect-Sensor-SDK](https://github.com/microsoft/Azure-Kinect-Sensor-SDK)  
  - [Azure_Kinect_ROS_Driver](https://github.com/microsoft/Azure_Kinect_ROS_Driver)  

## Installation
```bash
git clone https://github.com/takuya-ki/docker_k4a.git --recursive --depth 1 && cd docker_k4a && COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker-compose build --no-cache --parallel
```

## Usage
#### Host machine
```bash
docker-compose up
```
```bash
xhost + && docker exec -it k4a_container bash
```

#### Docker container
```bash
roslaunch k4a test_k4a.launch
```
```bash
roslaunch k4a k4a_pcd_rviz.launch
```
For other scripts, please see the bash history in the container.

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
