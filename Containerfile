FROM docker.io/osrf/ros:humble-desktop-full

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    apt-transport-https \
    software-properties-common \
    gpg && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add the Microsoft GPG key and VS Code repository
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | gpg --dearmor > microsoft.gpg && \
    install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/ && \
    sh -c 'echo "deb [arch=amd64 signed-by=/usr/share/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list' && \
    rm microsoft.gpg

# Update package lists again and install VS Code
RUN apt-get update && apt-get install -y code && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y \
    python3-pip \
    ros-dev-tools \
    stm32flash

ENV HUSARION_ROS_BUILD=simulation

WORKDIR ~/ros2_ws

RUN mkdir -p src && \
    git clone https://github.com/husarion/rosbot_ros -b humble src/

RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> ~/.bashrc && \
    /bin/bash -c "source ~/.bashrc"

RUN vcs import src < src/rosbot/rosbot_hardware.repos && \
    vcs import src < src/rosbot/rosbot_simulation.repos

RUN if [ -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then \
        rm /etc/ros/rosdep/sources.list.d/20-default.list; \
    fi && \
    rosdep init && \
    rosdep update --rosdistro $ROS_DISTRO && \
    rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y

RUN /bin/bash -c "source /opt/ros/$ROS_DISTRO/setup.bash && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release"
