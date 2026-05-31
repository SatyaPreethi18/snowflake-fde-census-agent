import os
import snowflake.connector
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA"),
    )


def run_query(query: str):
    conn = get_connection()

    try:
        cur = conn.cursor()
        cur.execute(query)

        return cur.fetch_pandas_all()

    finally:
        cur.close()
        conn.close()