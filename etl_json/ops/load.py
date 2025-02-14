import psycopg2
from dagster import op, job

@op
def load(data):

    if data != None:
        
        conn = psycopg2.connect(
            dbname="test_db",  
            user="postgres",  
            password="postgres", 
            host="localhost", 
            port="5432"  
        )
        
        cur = conn.cursor()
        
        
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL
            )
        """)

        
        for record in data:
            cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (record["name"], record["age"]))

    
        conn.commit()

    
        cur.close()
        conn.close()

    else:
        raise ValueError("Data is empty")
