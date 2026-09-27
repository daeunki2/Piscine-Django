#!/bin/bash

set -e

export DEBIAN_FRONTEND=noninteractive

echo "=== Updating packages ==="
apt-get update

echo "=== Installing basic tools ==="
apt-get install -y \
    curl \
    wget \
    gnupg \
    ca-certificates \
    git \
    vim \
    build-essential

echo "=== Installing Python environment ==="
apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev

echo "=== Installing XFCE desktop ==="
apt-get install -y \
    xfce4 \
    xfce4-goodies \
    lightdm

echo "=== Installing Korean input and fonts ==="
apt-get install -y \
    ibus \
    ibus-hangul \
    fonts-noto-cjk

echo "=== Installing Zsh ==="
apt-get install -y zsh

echo "=== Installing Google Chrome ==="

wget -qO- https://dl.google.com/linux/linux_signing_key.pub \
    | gpg --dearmor \
    > /usr/share/keyrings/google-chrome.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] https://dl.google.com/linux/chrome/deb/ stable main" \
    > /etc/apt/sources.list.d/google-chrome.list

apt-get update
apt-get install -y google-chrome-stable

echo "=== Configuring graphical boot ==="
systemctl set-default graphical.target
systemctl enable lightdm

echo "=== Setting Zsh as default shell for vagrant ==="
chsh -s "$(command -v zsh)" vagrant

echo "=== Finished ==="

python3 --version
pip3 --version
zsh --version
google-chrome --version
