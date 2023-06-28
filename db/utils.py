import os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
import psycopg2
from psycopg2 import sql

def get_postgres_datatype(value):
    conn = psycopg2.connect(
        database=os.environ.get("SOURCE_DB"), user=os.environ.get("SOURCE_USER"), password=os.environ.get("SOURCE_PASS"), host=os.environ.get("SOURCE_HOST"), port=os.environ.get("SOURCE_PORT"))
    cursor = conn.cursor()
    cursor.execute("SELECT pg_typeof(%s)", (value,))
    datatype = cursor.fetchone()[0].replace("unknown","varchar(255)")
    cursor.close()
    conn.close()
    return datatype


def create_or_replace_table(table_name,data_sample):
    assert isinstance(data_sample,dict), "Please provide a valid dict as a sample"
    conn = psycopg2.connect(
        database=os.environ.get("SOURCE_DB"), user=os.environ.get("SOURCE_USER"), password=os.environ.get("SOURCE_PASS"), host=os.environ.get("SOURCE_HOST"), port=os.environ.get("SOURCE_PORT"))
    cursor = conn.cursor()
    column_rows = ",\n\t".join([f"{col_name} {dtype}" for col_name, dtype in zip(data_sample.keys(),[get_postgres_datatype(x) for x in data_sample.values()]) ])
    syntax = sql.SQL("""CREATE TABLE IF NOT EXISTS {table_name} (
    id SERIAL PRIMARY KEY,
    {column_rows}
);
""".format(table_name=table_name,column_rows=column_rows))
    print(f"Create Table Query: {syntax}")
    cursor.execute(syntax)
    conn.commit()
    cursor.close()
    conn.close()