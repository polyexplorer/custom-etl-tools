from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
import sqlalchemy as sa
from sqlalchemy import create_engine

# Define the database credentials and instance information

# Create the connection string
# PSQL_CONNECTION_STRING = f"mysql+mysqldb://{user}:{password}@/{database}?unix_socket=/cloudsql/{project_id}:{instance_name}"

# # Create the engine
# engine = create_engine(connection_string)