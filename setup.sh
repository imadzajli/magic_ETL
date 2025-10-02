#!/bin/bash

mkdir -p ./dags ./logs ./plugins ./config

echo -e "AIRFLOW_UID=50000" > .env

docker compose up -d airflow-init

docker compose up -d




