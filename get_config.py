# Imports

import psycopg2
from psycopg2 import Error
import yaml
from datetime import datetime

# Get parameters from config file

with open("config.yml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)

p_dbname = cfg["postgre"]["dbname"]
p_port = cfg["postgre"]["port"]
p_user= cfg["postgre"]["user"]
p_host = cfg["postgre"]["host"]
p_password = cfg["postgre"]["password"]

try:

    # Connect to an existing database
    connection = psycopg2.connect(
                                    dbname = p_dbname,
                                    port = p_port,
                                    user= p_user,
                                    host = p_host,
                                    password = p_password
                                )

    # Create a cursor to perform database operations
    cursor = connection.cursor()

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)