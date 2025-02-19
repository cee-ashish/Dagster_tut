from dagster import resource
import sqlite3

@resource
def sqlite_resource(init_context):
    db_path = "my_database.db"  
    conn = sqlite3.connect(db_path)
    return conn
