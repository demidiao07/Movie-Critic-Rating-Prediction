import os
from dotenv import load_dotenv
import psycopg

load_dotenv()

def get_connection():
    try:
        conn = psycopg.connect(
            host=os.getenv("PGHOST"),
            dbname=os.getenv("PGDATABASE"),
            user=os.getenv("PGUSER"),
            password=os.getenv("PGPASSWORD"),
            port=os.getenv("PGPORT", 5432)
        )
        return conn
    except Exception as e:
        print("Database connection failed:", e)
        raise