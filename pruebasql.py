# importammos las librerias
from sqlalchemy import Column,Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#creamos nuestra clase superior de los modelos
Base =  declarative_base()

#creamos una tabla y sus columnas
class usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    edad = Column(Integer,nullable=False)
    
#variables de ubicacion de la db    
DATABASE_URL = "sqlite:///database.db"

#creamos el motor para conecatar la db
engine = create_engine(DATABASE_URL, echo=True)

#creamos la sesion que usara db
SessionLocal = sessionmaker(bind=engine)

#creamos la db
Base.metadata.create_all(engine)


def crear_usuarios(name,passw):
    session=SessionLocal()
    new_user = usuario (nombre=name,edad = passw)
    session.add (new_user)
    session.commit()
    session.refresh(new_user)
    session.close()
    print(new_user)
    
def obtener_usuarios ():
    session = SessionLocal()
    users = session.query(usuario).all()
    session.close()
    return users
def eliminar_usuarios (user_id):
    session = SessionLocal()
    user = session.query(usuario).filter(usuario.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
    session.close()
def actualizar_usuarios (user_id, new_name, new_age):
    session = SessionLocal()
    user = session.query(usuario).filter(usuario.id == user_id).first()
    if user:
        user.nombre = new_name
        user.edad = new_age
        session.commit()
    session.close()
    
crear_usuarios("Juan",25)