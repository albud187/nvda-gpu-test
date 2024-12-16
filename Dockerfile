FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

# Install dependencies
RUN apt-get update \
    && apt-get install -y \
    wget curl unzip \
    lsb-release \
    build-essential \
    nano \
    mesa-utils \
    python3-pip \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

RUN apt update \
    && apt install nvtop
    
# Clean up
RUN rm -rf /var/lib/apt/lists/*

# Set up entrypoint
ENTRYPOINT ["/bin/bash"]
