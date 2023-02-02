from sqlalchemy.orm import Session

from . import models, schemas


def is_blacklisted(db: Session, email: string):
    return db.query(models.Blacklisted).filter(models.Blacklisted.email == email).all()


def all_blacklisted(db: Session):
    return db.query(models.Blacklisted).all()

def post_blacklisted(db: Session, posted: schemas.Blacklisted):
    blacklisted = models.Blacklisted(email=posted.email, reason=posted.reason, game_id=posted.game_id)
    db.add(blacklisted)
    db.commit()
    db.refresh(blacklisted)
    return blacklisted