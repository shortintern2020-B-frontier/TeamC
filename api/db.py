import databases
import sqlalchemy

DATABASE = 'mysql'
USER = 'root'
PASSWORD = 'password'
HOST = '127.0.0.1'
PORT = '13306'
DB_NAME = 'yuru'

DATABASE_URL = '{}://{}:{}@{}:{}/{}'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

# databases
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG)

metadata = sqlalchemy.MetaData()
