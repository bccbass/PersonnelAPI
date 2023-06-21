#!/bin/bash

source .venv/bin/activate

flask db create
flask db seed_users
flask db seed_tables
