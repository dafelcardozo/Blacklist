from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blacklist/", response_model=schemas.Blacklisted)
def post_blacklisted(user: schemas.Blacklisted, db: Session = Depends(get_db)):
    return crud.post_blacklisted(db, user)


@app.get("/blacklist/", response_model=list[schemas.Blacklisted])
def list_blacklisted(db: Session = Depends(get_db)):
    return crud.all_blacklisted(db)


@app.get("/blacklist/check/{email}", response_model=object)
def check_blacklisted(email: str, db: Session = Depends(get_db)):
    return crud.is_blacklisted(db, email=email)

