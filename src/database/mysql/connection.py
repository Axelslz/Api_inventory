from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user = 'root'
password = ''
host = 'localhost'
port = '3306'
database = 'microservicio_inventory'

# Construye la cadena de conexión para MySQL
DATABASE_URL = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}'

# Crea el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crea una base declarativa
Base = declarative_base()

# Crea un generador de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





