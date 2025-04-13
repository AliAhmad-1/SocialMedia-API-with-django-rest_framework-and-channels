#!/bin/bash

# Install pip
curl https://bootstrap.pypa.io/get-pip.py | python3.12.1

# Install project dependencies
python3.12.1 -m pip install -r requirements.txt

python3.12.1 manage.py collectstatic