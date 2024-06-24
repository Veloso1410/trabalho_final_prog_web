# IMPORT
from sqlalchemy.orm import Session
from .models import Weapon

# DATABASE FUNCTIONS
def get_weapons(db: Session):
    return db.query(Weapon).all()

def get_weapon(db: Session, numero_de_serie: int):
    return db.query(Weapon).filter(Weapon.numero_de_serie == numero_de_serie).first()

def create_weapon(db: Session, weapon_data: dict):
    weapon = Weapon(**weapon_data)
    db.add(weapon)
    db.commit()
    db.refresh(weapon)
    return weapon

def update_weapon(db: Session, numero_de_serie: int, weapon_data: dict):
    weapon = db.query(Weapon).filter(Weapon.numero_de_serie == numero_de_serie).first()
    if weapon:
        for key, value in weapon_data.items():
            setattr(weapon, key, value)
        db.commit()
        db.refresh(weapon)
    return weapon

def delete_weapon(db: Session, numero_de_serie: int):
    weapon = db.query(Weapon).filter(Weapon.numero_de_serie == numero_de_serie).first()
    if weapon:
        db.delete(weapon)
        db.commit()
