#!/bin/bash

python3 -m venv .venv

source .venv/bin/activate

python3 -m pip install -r requirements.txt

flask db create
flask db seed_users
flask db seed_tables
