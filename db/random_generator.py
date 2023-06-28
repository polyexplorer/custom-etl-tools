from faker import Faker
import random
import time 


from sqlalchemy import MetaData, Table, insert
from sqlalchemy.engine import reflection
from sqlalchemy.orm import sessionmaker, declarative_base

from source.psql_source import connect_tcp_socket
from utils import create_or_replace_table
from sqlalchemy import event
from sqlalchemy.engine import Engine
import time
import logging

# logging.basicConfig()
# logger = logging.getLogger("myapp.sqltime")
# logger.setLevel(logging.DEBUG)

# @event.listens_for(Engine, "before_cursor_execute")
# def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#     conn.info.setdefault('query_start_time', []).append(time.time())
#     logger.debug("Start Query: %s", statement)

# @event.listens_for(Engine, "after_cursor_execute")
# def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#     total = time.time() - conn.info['query_start_time'].pop(-1)
#     logger.debug("Query Complete!")
#     logger.debug("Total Time: %f", total)





def generate_dummy_data(num_rows):
    fake = Faker()
    dummy_data = []
    for _ in range(num_rows):
        dummy_data.append({
            'name': fake.name(),
            'age': random.randint(18, 99),
            'gender': random.choice(['M', 'F'])
        })
    return dummy_data


def insert_dummy_data(data,table_name):
    engine = connect_tcp_socket()
    metadata = MetaData()
    metadata.reflect(bind=engine,schema='public')
    create_or_replace_table(table_name,data[0])
    metadata = MetaData()
    metadata.reflect(bind=engine,schema='public')
    
    TableObj = Table(table_name,metadata,autoload_with=engine)
    connection = engine.connect()
    print("Creating Statements...")
    stmt = TableObj.insert()
    print("Created, Inserting...")
    connection.execute(stmt,data)
    connection.commit() 
    print("Inserted, closing connection...")
    connection.close()
    print("Done.")
    
def test():
    data = generate_dummy_data(100)
    print("Adding Data...")
    start_time = time.time()
    insert_dummy_data(data,'dummy_table_2')
    print("Added 100 rows in ",time.time() - start_time,"seconds.")
    
if __name__ == "__main__":
    test()