from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#Creación del motor

#user: postgres
#password: password
#host: localhost
#port: 5432
#name_db: MISION_TIC

DATABASE_URL = "postgresql://postgres:1234@localhost:5432/MISION_TIC"
engine = create_engine(DATABASE_URL)

#Creación de Sesión y Dependencias
#autocommit=false para que los cambios no sean automaticos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Encargada de inyectar codigo
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Base para la entidad de datos
Base = declarative_base()
Base.metadata.schema = "cajerodb"


