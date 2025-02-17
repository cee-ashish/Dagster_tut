from dagster import op

@op(required_resource_keys={"db"})
def load(context, data):
    """Load data into the SQLite database using Dagster's resource."""
    if not data:
        raise ValueError("Data is empty")

    conn = context.resources.db.get_connection()  # Get connection from resource
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    """)

    # Insert data
    for record in data:
        cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", (record["name"], record["age"]))
    
    conn.commit()
    cur.close()
