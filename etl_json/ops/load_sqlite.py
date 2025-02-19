from dagster import op
from etl_json.resources.sqllite_connection import sqlite_resource

@op(required_resource_keys={"sqlite_resource"})
def load_data(context, data):
    conn = context.resources.sqlite_resource
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            age_category TEXT
        )
    """)

    for item in data:
        cursor.execute("INSERT INTO my_table (id, name, age, age_category) VALUES (?, ?, ?, ?)",
                       (item["id"], item["name"], item["age"], item["age_category"]))
    
    conn.commit()
    cursor.close()
