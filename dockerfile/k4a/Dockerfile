FROM nvidia/opengl:1.2-glvnd-devel-ubuntu18.04

# setting environmental variables
ENV DEBIAN_FRONTEND noninteractive

RUN apt update -y && apt install -y --no-install-recommends curl lsb-release wget gnupg
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add -

RUN apt update -y && apt install -y --no-install-recommends tzdata
RUN apt update -y && apt install -y --no-install-recommends \
    ros-melodic-desktop-full \
    ros-melodic-uvc-camera \
    ros-melodic-image-view \
    ros-melodic-rgbd-launch \
    ros-melodic-pcl-ros \
    software-properties-common \
    python-catkin-tools \
    python3-setuptools \
    python-setuptools \
    build-essential \
    libsoundio-dev \
    python-rosdep \
    python3-venv \
    libudev-dev \
    ninja-build \
    python3-pip \
    python-pip \
    python3-tk \
    python3.8 \
    net-tools \
    pcl-tools \
    byobu \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /catkin_ws/src && \
	/bin/bash -c "cd /catkin_ws/src && source /opt/ros/melodic/setup.bash && catkin_init_workspace" && \
	/bin/bash -c "cd /catkin_ws && source /opt/ros/melodic/setup.bash && catkin build" && \
	echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc && \
	echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc && \
	echo "export ROS_PACKAGE_PATH=\${ROS_PACKAGE_PATH}:/catkin_ws" >> ~/.bashrc && \
	echo "export ROS_WORKSPACE=/catkin_ws" >> ~/.bashrc

# Azure Kinect
WORKDIR /
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN /bin/bash -c 'echo "deb [arch=amd64] https://packages.microsoft.com/ubuntu/18.04/prod bionic main" >> /etc/apt/sources.list'
RUN apt update -y && ACCEPT_EULA=Y apt install -y k4a-tools=1.4.2
RUN git clone https://github.com/microsoft/Azure-Kinect-Sensor-SDK -b v1.4.2 --recursive && cd Azure-Kinect-Sensor-SDK && git reset --hard cd2b3e9

WORKDIR /catkin_ws/src/
RUN git clone https://github.com/microsoft/Azure_Kinect_ROS_Driver -b melodic --recursive && cd Azure_Kinect_ROS_Driver && git reset --hard a3eed22

WORKDIR /
RUN wget https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4a1.4/libk4a1.4_1.4.2_amd64.deb
RUN wget https://packages.microsoft.com/ubuntu/18.04/prod/pool/main/libk/libk4a1.4-dev/libk4a1.4-dev_1.4.2_amd64.deb
RUN apt update -y && ACCEPT_EULA=Y apt install -y ./libk4a1.4_1.4.2_amd64.deb ./libk4a1.4-dev_1.4.2_amd64.deb

WORKDIR /Azure-Kinect-Sensor-SDK/
RUN mkdir build && cd build && cmake .. -GNinja && ninja && ninja install
RUN cp /usr/lib/x86_64-linux-gnu/libk4a1.4/libdepthengine.so.2.0 /Azure-Kinect-Sensor-SDK/build/bin/
RUN echo "/Azure-Kinect-Sensor-SDK/build/bin" >> /etc/ld.so.conf.d/libc.conf
RUN echo "export LD_LIBRARY_PATH=/Azure-Kinect-Sensor-SDK/build/bin/:/opt/ros/melodic/lib/:$LD_LIBRARY_PATH" >> ~/.bashrc

WORKDIR /Azure-Kinect-Sensor-SDK/src/python/k4a/
RUN cp /usr/lib/x86_64-linux-gnu/libk4a.so ./src/k4a/_libs/ 
RUN cp /usr/lib/x86_64-linux-gnu/libk4a.so.1.4 ./src/k4a/_libs/
RUN cp /usr/lib/x86_64-linux-gnu/libk4a.so.1.4.2 ./src/k4a/_libs/
RUN cp /usr/lib/x86_64-linux-gnu/libk4a1.4/libdepthengine.so.2.0 ./src/k4a/_libs/
ADD build_wheel_rev.csh .
RUN /bin/bash -c 'source ./build_wheel_rev.csh'
RUN chmod +x examples/*
RUN pip3 install --upgrade pip && pip3 install opencv-contrib-python open3d

# Generates bash commands
WORKDIR /
RUN echo "k4aviewer" >> ~/.bash_history
RUN echo "roslaunch k4a test_k4a.launch" >> ~/.bash_history
RUN echo "roslaunch k4a k4a_pcd_rviz.launch" >> ~/.bash_history
RUN echo "rosrun pcl_ros pointcloud_to_pcd input:=/camera/depth/color/points _prefix:=/catkin_ws/src/realsense-ros/pcd/vel_" >> ~/.bash_history
RUN echo "rosrun pcl_ros pointcloud_to_pcd input:=/points2 _prefix:=/catkin_ws/src/db-manip-stack/object_recognition/pcd/vel_" >> ~/.bash_history
RUN echo "cd /catkin_ws/src/k4a/scripts" >> ~/.bash_history
RUN echo "python3 disp_rgbd.py" >> ~/.bash_history
RUN echo "python3 save_pcd.py" >> ~/.bash_history
RUN echo "python3 read_pcd.py" >> ~/.bash_history
RUN echo "python3 /Azure-Kinect-Sensor-SDK/src/python/k4a/examples/simple_viewer.py" >> ~/.bash_history
RUN echo "python3 /Azure-Kinect-Sensor-SDK/src/python/k4a/examples/point_cloud_capture.py" >> ~/.bash_history
RUN echo "python3 /Azure-Kinect-Sensor-SDK/src/python/k4a/examples/image_transformations.py" >> ~/.bash_history
RUN echo "python3 /Azure-Kinect-Sensor-SDK/src/python/k4a/examples/the_basics.py" >> ~/.bash_history
