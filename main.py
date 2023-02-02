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
def post_blacklisted(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.post_blacklisted(db=db, user=user)


@app.get("/blacklist/", response_model=list[schemas.User])
def list_blacklisted(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.all_blacklisted(db, skip=skip, limit=limit)


@app.get("/blacklist/check/{email}", response_model=schemas.User)
def check_blacklisted(user_id: int, db: Session = Depends(get_db)):
    return crud.is_blacklisted(db, email=email)

