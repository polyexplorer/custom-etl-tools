import ssl
import os
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

import sqlalchemy
from sqlalchemy import create_engine

def connect_tcp_socket() -> sqlalchemy.engine.base.Engine:
    """Initializes a TCP connection pool for a Cloud SQL instance of Postgres."""
    db_host = os.environ.get("SOURCE_HOST")
    db_user = os.environ.get("SOURCE_USER")  # e.g. 'my-db-user'
    db_pass = os.environ.get("SOURCE_PASS")  # e.g. 'my-db-password'
    db_name = os.environ.get("SOURCE_DB")  # e.g. 'my-database'
    db_port = os.environ.get("SOURCE_PORT")  # e.g. 5432
    # return sqlalchemy.create_engine('postgresql://user:password@localhost/dbname', connect_args={'options': '-csearch_path=public'})
    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # postgresql+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL.create(
            drivername="postgresql+pg8000",
            username=db_user,
            password=db_pass,
            host=db_host,
            port=db_port,
            database=db_name,
        ),
        # ...
    )
    return pool


# Define the database credentials and instance information

# Create the connection string
# PSQL_CONNECTION_STRING = f"mysql+mysqldb://{user}:{password}@/{database}?unix_socket=/cloudsql/{project_id}:{instance_name}"

# # Create the engine
# engine = create_engine(connection_string)