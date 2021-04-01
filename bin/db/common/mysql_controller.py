__author__ = "Christian Ochoa"
__email__ = "calochoa@gmail.com"

import logging

from mysql.connector import MySQLConnection, Error
from bin.db.common.python_mysql_dbconfig import read_db_config


class MySQLController(object):

    def __init__(self, config_file='bin/conf/config.ini', section='mysql'):
        self.db_config = read_db_config(filename=config_file, section=section)

    def get_connection(self):
        try:
            logging.info("Connecting to MySQL database...")
            conn = MySQLConnection(**self.db_config)
            if conn.is_connected():
                logging.info("connection established")
            else:
                logging.info("connection failed")
            return conn
        except Error as e:
            logging.error("connection failed")
            logging.error(e)

    def close(self, cursor, conn):
        if cursor:
            cursor.close()
        if conn:
            conn.close()
            logging.info("connection closed")

    def query_multi_with_fetchall_as_dict(self, query):
        results = []
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            for result in cursor.execute(query, multi=True):
                if result.with_rows:
                    columns = [column[0] for column in cursor.description]
                    for row in result.fetchall():
                        results.append(dict(zip(columns, row)))
        except Error as e:
            logging.error(e)
        finally:
            self.close(cursor, conn)
            return results
