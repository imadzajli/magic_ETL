import json
import mysql.connector
import psycopg2
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),"."))
sys.path.append(project_root)

from logger import get_logger

logger = get_logger()
connection_types = [
    "mysql",
    "psql"
]

class Connection:
    def __init__(self, connection_type, host, port, user, password, database):
        self.connection_type = connection_type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
    
    def get_connection(self):
        if self.connection_type == "mysql":
            logger.info(f"Trying to connect to mysql ...")
            try:
                cnx = mysql.connector.connect(
                    host = self.host,
                    port = self.port,
                    user = self.user,
                    password = self.password,
                    database = self.database
                )
                logger.info(f"successfully connected to mysql ...")
                return cnx
            except mysql.connector.errors.ProgrammingError as e:
                logger.error(f"Wrong connection data, check your configuration in config.json")
                sys.exit(0)
            except Exception as e:
                logger.error(e)
                sys.exit(0)
        elif self.connection_type == "psql":
            logger.info(f"Trying to connect to postgresql ...")
            try:
                cnx = psycopg2.connect(
                    host = self.host,
                    port = self.port,
                    user = self.user,
                    password = self.password,
                    database = self.database
                )
                logger.info(f"successfully connected to postgresql")
                return cnx
            except:
                logger.error(f"Failed to get postgres connection, check your data")
                sys.exit(0)

        else:
            logger.error(f"invalid connection type, only {connection_types} are available for now")
            sys.exit(0)
    
    def test_mysql_connection(self):
        cnx = self.get_connection()
        cur = cnx.cursor()
        if cur != None:
            logger.info(f"cursor ceated sucessfully : {cur}")
        else:
            logger.error(f"cursor not ceated ")
        cur.execute("SELECT CURDATE()")
        row = cur.fetchone()
        print(f"res : {row}")
        cur.close()
    
    def test_psql_connection(self):
        cnx = self.get_connection()
        cur = cnx.cursor()
        if cur != None:
            logger.info(f"cursor ceated sucessfully : {cur}")
        else:
            logger.error(f"cursor not ceated ")
        cur.execute("SELECT NOW()")
        row = cur.fetchone()
        print(f"res : {row}")
        cur.close()

    



