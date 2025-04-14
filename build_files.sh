#!/bin/bash

# Install pip
curl https://bootstrap.pypa.io/get-pip.py | python3.9

# Install project dependencies
python3.9 -m pip install -r requirements.txt
daphne -b 0.0.0.0 -p 8001 backend.asgi:application
