import pyodbc
import sys
import os
import logging
from datetime import datetime

SRVR = "217.195.207.174"
USER = "PervaSozSQLuser"
PASS = "t3v04tX@08qx2hS31"
DBNM = "PervasozDatabase"
DRVR = "ODBC Driver 17 for SQL Server"

cst = f"DRIVER={DRVR};server={SRVR};DATABASE={DBNM};UID={USER};PWD={PASS}"
con = pyodbc.connect(cst)
cur = con.cursor()

# Create logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

# Set up logging configuration
log_filename = f"logs/migrate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
print(log_filename)
logging.basicConfig(filename=log_filename, level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Logging initialized.")
logging.info("Connection successful")

def migrate_authors(cur):
    cur.execute("SELECT * FROM Table_Yazarlar;")
    for raw_user in cur.fetchall():
        logging.info(f'migrating: {raw_user[1]}')

    
def migrate_entries(cur):
    pass


def migrate_entry_reports(cur):
    pass


migrate_authors(cur)
migrate_entries(cur)
migrate_entry_reports(cur)
cur.close()
con.close()
