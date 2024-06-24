###################################################################
# IMPORT SESSION #
###################################################################

from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from app.database import engine, SessionLocal
from app.models import Base, Weapon
from app.crud import get_weapons, get_weapon, create_weapon, update_weapon, delete_weapon
from app.schemas import WeaponCreate, WeaponUpdate
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
import os

templates = Jinja2Templates(directory=os.path.join(os.getcwd(), "app/templates"))

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
###################################################################
# ENDPOINTS #
###################################################################

@app.get("/armas")
def homearmas(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("armas.html", {"request": request}) 
      
@app.get("/quemsomos")
def homequemsomos(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("quem_somos.html", {"request": request})

@app.get("/ondecomprar")
def homeondecomprar(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("onde_comprar.html", {"request": request})

@app.get("/licenca")
def homelicença(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("licenca.html", {"request": request})

@app.get("/")
def home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/adicionar")
def adicionar_arma(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("adicionar_arma.html", {"request": request})

@app.post("/adicionar")
def adicionar_arma(
    numero_de_serie: int = Form(...), 
    classe: str = Form(...), 
    calibre: str = Form(...), 
    modelo: str = Form(...), 
    marca: str = Form(...), 
    capacidade: int = Form(...), 
    db: Session = Depends(get_db)
):
    weapon_data = {
        "numero_de_serie": numero_de_serie,
        "classe": classe,
        "calibre": calibre,
        "modelo": modelo,
        "marca": marca,
        "capacidade": capacidade
    }
    
    create_weapon(db, weapon_data)

    return RedirectResponse(url="/armas", status_code=303)

@app.get("/editar/{numero_de_serie}")
def editar_arma(numero_de_serie: int, request: Request, db: Session = Depends(get_db)) -> HTMLResponse:
    weapon = get_weapon(db, numero_de_serie)
    if not weapon:
        pass
    return templates.TemplateResponse("editar_arma.html", {"request": request, "weapon": weapon})

@app.post("/editar/{numero_de_serie}")
def atualizar_arma(
    numero_de_serie: int,
    classe: str = Form(...),
    calibre: str = Form(...),
    modelo: str = Form(...),
    marca: str = Form(...),
    capacidade: int = Form(...),
    db: Session = Depends(get_db)
):
    weapon_data = {
        "classe": classe,
        "calibre": calibre,
        "modelo": modelo,
        "marca": marca,
        "capacidade": capacidade
    }

    weapon = update_weapon(db, numero_de_serie, weapon_data)

    if not weapon:
        
        pass

    return RedirectResponse(url="/armas", status_code=303)

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

@app.get("/weapons")
def read_weapons(db: Session = Depends(get_db)):
    return get_weapons(db)

@app.get("/weapons/{numero_de_serie}")
def read_weapon(numero_de_serie: int, db: Session = Depends(get_db)):
    weapon = get_weapon(db, numero_de_serie)
    if not weapon:
        raise HTTPException(status_code=404, detail="Weapon not found")
    return weapon

@app.post("/weapons")
def create_weapon_endpoint(weapon: WeaponCreate, db: Session = Depends(get_db)):
    weapon_data = weapon.dict()
    return create_weapon(db, weapon_data)

@app.put("/weapons/{numero_de_serie}")
def update_weapon_endpoint(numero_de_serie: int, weapon: WeaponUpdate, db: Session = Depends(get_db)):
    weapon_data = weapon.dict()
    return update_weapon(db, numero_de_serie, weapon_data)

@app.delete("/weapons/{numero_de_serie}")
def delete_weapon_endpoint(numero_de_serie: int, db: Session = Depends(get_db)):
    delete_weapon(db, numero_de_serie)
    return {"message": "Weapon deleted"}

import uvicorn

uvicorn.run(app, port=8888)
