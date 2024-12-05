# Setup Environment

## Software Requirements

📌 Computer with OS: [Ubuntu 22.04 Desktop](https://releases.ubuntu.com/jammy/).
Computer with `am64` architecture.

## Setup

Install all the required tooling:

```
sudo apt update && sudo apt install -y git ansible
cd ~ && git clone https://github.com/EOLab-HSRW/lacoro-2024-ros-workshop.git
ansible-playbook local.yml --ask-become
```
