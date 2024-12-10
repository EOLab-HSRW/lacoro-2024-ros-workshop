# Setup Environment

## Software Requirements

📌 Computer with OS: [Ubuntu 22.04 Desktop](https://releases.ubuntu.com/jammy/).
Computer with `am64` architecture.

## Setup

Install all the required tooling:

```
sudo apt update && sudo apt install -y git ansible
mkdir -p ~/lss_ws/src && cd ~/lss_ws/src/
git clone https://github.com/EOLab-HSRW/lacoro-2024-ros-workshop.git && cd lacoro-2024-ros-workshop
ansible-playbook local.yml --ask-become
```
