# IMPORT
from pydantic import BaseModel

# CLASSES
class WeaponBody(BaseModel):
    numero_de_serie:int
    classe:str
    calibre:str
    modelo:str
    marca:str
    capacidade:int
    

class WeaponCreate(BaseModel):
    numero_de_serie:int
    classe:str
    calibre:str
    modelo:str
    marca:str
    capacidade:int

class WeaponUpdate(BaseModel):
    numero_de_serie:int
    classe:str
    calibre:str
    modelo:str
    marca:str
    capacidade:int
