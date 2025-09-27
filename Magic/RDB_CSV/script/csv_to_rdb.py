import sys
import os
import json
import time

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../.."))
sys.path.append(project_root)

from utils.csv_utils import *
from utils.rdb_connection import *
from utils.logger import get_logger

logger = get_logger()

class ETL_csv_2_rdb:

    def __init__(self):
        with open("../config.json","rb") as f:
            self.config = json.load(f)
            f.close()
        try:
            csv_util_obj = csv_magic(self.config["csv_path"])
        except:
            logger.error(f"csv_path is missing or wrong")
            sys.exit(0)
        

        self.csv_util = csv_util_obj

        try:
            keys = self.config.keys()
            if "host" not in keys:
                logger.error(f"missing required config 'host' in config.json")
                sys.exit(0)
            if "port" not in keys:
                logger.error(f"missing required config : 'port' in config.json")
                sys.exit(0)
            if "connection_type" not in keys:
                logger.error(f"missing required config : 'connection_type' in config.json")
                sys.exit(0)
            if "user" not in keys:
                logger.error(f"missing required config : 'user' in config.json")
                sys.exit(0)
            if "password" not in keys:
                logger.error(f"missing required config : 'password' in config.json")
                sys.exit(0)
            if "database" not in keys:
                logger.error(f"missing required config : 'database' in config.json")
                sys.exit(0)
            rdb_util_obj = Connection(
                host = self.config["host"]
                port = self.config["port"]
                password = self.config["password"]
                user  = self.config["user"]
                database = self.config["database"]
                connection_type = self.config["connection_type"]
            )

        self.rdb_util = rdb_util_obj
        self.df = None
        self.cnx = None
        

    def load(self):
        cnx = self.rdb_util_obj.get_connection()
        self.cnx = cnx
        # you can define your loading plan after defining the transform path
        
        
    
    def transform(self):
        # to complete by you :)
        pass

    def extract(self):
        df = self.csv_util.csv_to_df()
        self.df = df
    
    def run_etl(self):
        self.extract()
        while True:
            self.transform()
        self.load()