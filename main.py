from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from mangum import Mangum
from fastapi.exceptions import RequestValidationError
from exception_handlers import request_validation_exception_handler, http_exception_handler, unhandled_exception_handler
from middleware import log_request_middleware, catch_exceptions_middleware
from database import SessionLocal, engine
import crud, models, schemas
import os

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Trebu Blacklist",
    description="A demo project of my abilities with AWS, Rest and Python. It contains just to endpoints",
    version="1.0",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Felipe Cardozo",
        "url": "https://github.com/dafelcardozo/",
        "email": "dafelcardozo@gmai.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    })

app.middleware("http")(log_request_middleware)
app.middleware('http')(catch_exceptions_middleware)
app.add_exception_handler(RequestValidationError, request_validation_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blacklist", response_model=schemas.Blacklisted)
def post_blacklisted(user: schemas.Blacklisted, db: Session = Depends(get_db)):
    return crud.post_blacklisted(db, user)

@app.get("/blacklist/check/{email}", response_model=schemas.PlayerReport)
def check_blacklisted(email: str, db: Session = Depends(get_db)):
    return crud.is_blacklisted(db, email=email)

@app.get("/__debug", response_model=list[schemas.Blacklisted])
def debug_blacklisted(db: Session = Depends(get_db)):
    return crud.all_blacklisted(db)

handler = Mangum(app)
