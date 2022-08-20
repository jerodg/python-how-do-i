# Ubuntu 20.04 Base Docker Image Optimized for Containers (Development)
#   w/ Shared & Optimized Python 3.8.2
# Copyright © 2020 Jerod Gawne <https://github.com/jerodg>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

FROM jerodg/base:ubuntu-20.04_2020.04.20


# Prequisites
RUN apt-get update
RUN apt-get -y install tzdata
RUN echo "UTC" > /etc/timezone
RUN rm -f /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata


# Python
RUN apt-get -y install \
    binutils \
    build-essential \
    cython3 \
    debhelper-compat \
    dh-python \
    freetds-dev \
    libb2-dev \
    libbz2-dev \
    libdb5.3-dev \
    libexpat1-dev \
    libffi-dev \
    libgdbm-dev \
    libkrb5-dev \
    liblzma-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libzfslinux-dev \
    python3-all-dev \
    python3-pytest-xvfb \
    python3-pyvirtualdisplay \
    python3-setuptools \
    python3-testresources \
    python3-xvfbwrapper \
    uuid-dev \
    wget \
    xvfb \
    xz-utils \
    zlib1g-dev

# # Get Source
WORKDIR /tmp
RUN wget https://www.python.org/ftp/python/3.8.2/Python-3.8.2.tgz
RUN tar xf Python-3.8.2.tgz

# Build Source
WORKDIR /tmp/Python-3.8.2
RUN ./configure --enable-optimizations --enable-shared
RUN make -j$(($(nproc) / 2) - 1)
RUN make -j$(($(nproc) / 2) - 1) install

# Configure Shared Link Library
RUN strip /usr/local/lib/libpython3.8.so.1.0
RUN ldconfig

# Configure Symbolic Links
WORKDIR /usr/local/bin
RUN ln -s /usr/local/bin/python3.8 python
RUN ln -s /usr/local/bin/pip3.8 pip

# Update Core Python Packages
RUN pip install --upgrade pip setuptools

# Cleanup
RUN rm -rf /tmp/*
RUN apt-get autoclean
RUN apt-get autoremove

LABEL org.opencontainers.image.vendor="Mhi Inc."
LABEL org.opencontainers.image.url=https://jerodg.dev
LABEL org.opencontainers.image.title="Ubuntu 20.04 w/Python 3.8.2"
LABEL org.opencontainers.image.description="Ubuntu 20.04 Base Docker Image Optimized for Containers w/Python 3.8.2"
LABEL org.opencontainers.image.version=1.1.0
LABEL org.opencontainers.image.documentation=https://github.com/jerodg

# Use For Development; Keeps the Container Running
# ENTRYPOINT ["/bin/bash", "-c", "while true; do sleep 1; done"]
