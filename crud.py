from sqlalchemy.orm import Session
from sqlalchemy import func, distinct
import schemas
from models import Blacklisted
from datetime import datetime, timedelta

"""
def is_blacklisted(db: Session, email: str):
    query = db.query(
        Blacklisted.reason, Blacklisted.email,
        func.count(Blacklisted.reason),
        func.count(distinct(Blacklisted.game_id))
    ).group_by(Blacklisted.reason, Blacklisted.email).having(Blacklisted.email == email)\
    .order_by(func.count(Blacklisted.reason))

    most_common_reason, _, count, count2 = query.first()
    all_times_report = dict(most_common_reason=most_common_reason, most_common_reason_count=count, games_reported=count2)
 
    query = db.query(
        Blacklisted.reason, Blacklisted.email,
        func.count(Blacklisted.reason),
        func.count(distinct(Blacklisted.game_id))
    )\
        .filter(Blacklisted.date >= (datetime.now() - timedelta(days=3)) )\
        .group_by(Blacklisted.reason, Blacklisted.email).having(Blacklisted.email == email)\
        .order_by(func.count(Blacklisted.reason))
    most_common_reason, _, count, count2 = query.first()
    last_90_days_report = dict(most_common_reason=most_common_reason, most_common_reason_count=count, games_reported=count2)
    all_data = db.query(Blacklisted).filter(Blacklisted.email == email).all()
    return dict(aggregates=dict(last_90_days=last_90_days_report, all_times_report=all_times_report), all_data=all_data)
"""
def is_blacklisted(db: Session, email: str) -> schemas.PlayerReport:
    query = db.query(
        Blacklisted.reason, Blacklisted.email,
        func.count(Blacklisted.reason),
        func.count(distinct(Blacklisted.game_id))
    ).group_by(Blacklisted.reason, Blacklisted.email).having(Blacklisted.email == email)\
    .order_by(func.count(Blacklisted.reason))

    most_common_reason, _, count, count2 = query.first()
    all_times_report = schemas.Agreggate(most_common_reason=most_common_reason, times_reported=count, games_reported=count2)
 
    query = db.query(
        Blacklisted.reason, Blacklisted.email,
        func.count(Blacklisted.reason),
        func.count(distinct(Blacklisted.game_id))
    )\
        .filter(Blacklisted.date >= (datetime.now() - timedelta(days=3)) )\
        .group_by(Blacklisted.reason, Blacklisted.email).having(Blacklisted.email == email)\
        .order_by(func.count(Blacklisted.reason))
    most_common_reason, _, count, count2 = query.first()
    last_90_days_report = schemas.Agreggate(most_common_reason=most_common_reason, times_reported=count, games_reported=count2)
    all_data = db.query(Blacklisted).filter(Blacklisted.email == email).all()
    return schemas.PlayerReport(last_90_days=last_90_days_report, all_times=all_times_report, all_data=all_data)

def all_blacklisted(db: Session):
    return db.query(Blacklisted).filter().all()

def post_blacklisted(db: Session, posted: schemas.Blacklisted):
    print("Post crud...")
    blacklisted = Blacklisted(email=posted.email, reason=posted.reason, game_id=posted.game_id, date=posted.date )
    db.add(blacklisted)
    db.commit()
    db.refresh(blacklisted)
    return blacklisted