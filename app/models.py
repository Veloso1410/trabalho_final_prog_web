# IMPORT 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TABLE CREATION
class Weapon(Base):
    __tablename__ = "weapons"
    numero_de_serie = Column(Integer, primary_key=True, index=True)
    classe = Column(String, index=True)
    calibre = Column(String, index=True)
    modelo = Column(String, index=True)
    marca = Column(String, index=True)
    capacidade = Column(Integer, index=True)
