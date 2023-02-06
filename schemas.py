from pydantic import BaseModel,  Field
from datetime import datetime


class Blacklisted(BaseModel):
    id: int  = None
    email: str
    reason: str
    game_id: int
    date: datetime = None

    class Config:
        orm_mode = True


class Agreggate(BaseModel):
    most_common_reason: str
    times_reported: int
    games_reported: int
    

class PlayerReport(BaseModel):
    all_times: dict
    last_90_days: Agreggate
    all_data: list[Blacklisted]