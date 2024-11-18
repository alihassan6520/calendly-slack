#!/bin/bash

set -e

# Create a virtual environment without pip
virtualenv --without-pip virtualenv

# Upgrade pip to the latest version
pip install --upgrade pip -r requirements.txt --target virtualenv/lib/python3.9/site-packages

# Install required packages
