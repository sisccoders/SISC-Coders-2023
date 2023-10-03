# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set environment variables to non-interactive (this prevents some prompts)
ENV DEBIAN_FRONTEND=non-interactive

# Run package updates and install packages
RUN apt-get update \
    && apt-get install -y \
    wget \
    python3 \
    python3-pip \
    openjdk-11-jdk \
    git \
    g++ \
    gcc \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install .NET SDK for C#
RUN apt-get update \
    && apt-get install -y \
    apt-transport-https \
    && wget https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb \
    && dpkg -i packages-microsoft-prod.deb \
    && apt-get update \
    && apt-get install -y dotnet-sdk-6.0 \
    && rm -rf /var/lib/apt/lists/*

RUN echo "alias python=python3" >> ~/.bashrc

# Set up the working directory
WORKDIR /workspace

# Set the default shell to bash
CMD ["/bin/bash"]
