
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
 
