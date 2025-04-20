# docker_k4a

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.svg)](http://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![repo size](https://img.shields.io/github/repo-size/UOsaka-Harada-Laboratory/docker_k4a)

Docker of a development environment for Microsoft Azure Kinect (k4a).

## Dependency (tested as a host machine)

- [Ubuntu 22.04 PC](https://ubuntu.com/certified/laptops?q=&limit=20&vendor=Dell&vendor=Lenovo&vendor=HP&release=22.04+LTS)
  - NVIDIA GeForce RTX 3070
  - NVIDIA Driver 470.256.02
  - Docker 27.4.1
  - Docker Compose 2.32.1
  - NVIDIA Docker 2.13.0
- Microsoft Azure Kinect
  - [Azure-Kinect-Sensor-SDK](https://github.com/microsoft/Azure-Kinect-Sensor-SDK)  
  - [Azure_Kinect_ROS_Driver](https://github.com/microsoft/Azure_Kinect_ROS_Driver)  

## Installation
```bash
git clone git@github.com:UOsaka-Harada-Laboratory/docker_k4a.git --recursive --depth 1 && cd docker_k4a && COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose build --no-cache --parallel
```

## Usage
#### Host machine
```bash
docker compose up
```
```bash
xhost + && docker exec -it k4a_container bash
```

#### Docker container
- Please see the bash history in the container for more examples.
    ```bash
    roslaunch k4a test_k4a.launch
    ```
    ```bash
    roslaunch k4a k4a_pcd_rviz.launch
    ```

## Author / Contributor

[Takuya Kiyokawa](https://takuya-ki.github.io/)

## License

This software is released under the MIT License, see [LICENSE](./LICENSE).
