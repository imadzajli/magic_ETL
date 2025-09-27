
The following tool provide you some most used ETL pipelines, each one is set on a unique directory under the main directory "Magic".

I will provide both basic ETL configuration (using only script running on a loop) and airflow configuation that you can use later on your project.

To run this project, just follow those instructions:

- First you should run setups script.

```bash
chmod +x setup.sh && ./setup.sh
```
!! if there is error while installing python libraries (add "--break-system-packages" after pip install requirements.txt)

This project is using a docker env, so you can control it from docker-compose file. There may be port error in case you already have a running service on that port, just change it and restart that service.

## Project archtexture

After running the setup.sh script you will have the exact architecture like the following:

```bash
├── config
├── dags
├── logs
│   ├── dag_processor_manager
│   └── scheduler
│       ├── 2025-09-25
│       ├── 2025-09-27
│       └── latest -> 2025-09-27
├── Magic
│   ├── RDB_CSV
│   │   ├── airflow
│   │   └── script
│   └── RDB_JSON
├── plugins
└── utils
    └── __pycache__
```

the config, dags, logs and plugins are needed for airflow service, the Magic conatins the source code (core code) for each ETL pipeline, an ETL pipeline is a folder inside magic folder, it contains 2 folders first is script folder and second is airflow folder. There is also utils folder for external useful code.

- Magic : Contains all ETL pipelines (base and sample format)

- script : Contains core code or base code for each ETL in the following format

```python
def extract(**args):
    # code here
def transform(**args):
    # code here
def load(**args):
    # code here
```

- airflow : contains the actual full working ETL, all those files are beeing used by airflow later after the full build is done. Each ETL base folder contains a different example (to use in everyday data engineer tasks).

- utils : Contains useful code written by me to be used each time instead of writting it again and again, such us connection hadling scripts, configuration files...

- config.json file : contains configuration needed to run the ETL correctly
 
