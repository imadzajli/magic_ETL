import pandas as pd
import sys, os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))
sys.path.append(project_root)

from logger import get_logger

path = "/home/imadxt/Downloads/cities.csv"

logger = get_logger()

class csv_magic:

    def __init__(self,path):
        self.path = path
        try:
            self.df = pd.read_csv(path)
        except:
            logger.error(f"error reading csv file {path}")
            sys.exit(0)
    
    def csv_to_df(self):
        return self.df





t = csv_magic(path)

df = t.csv_to_df()
