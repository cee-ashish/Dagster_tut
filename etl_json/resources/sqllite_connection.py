import sqlite3
from dagster import resource

class SQLiteResource:
    """Resource to manage an SQLite connection."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = None

    def get_connection(self):
        """Return an SQLite connection."""
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def close_connection(self):
        """Close the connection if open."""
        if self.conn:
            self.conn.close()
            self.conn = None

@resource(config_schema={"db_path": str})
def sqlite_resource(init_context):
    """Dagster resource wrapper for SQLite."""
 
    return SQLiteResource(init_context.resource_config["db_path"])


from dagster import execute_job


# Define the required resource configuration


