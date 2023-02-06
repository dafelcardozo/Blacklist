from pydantic import BaseModel,  Field


class Blacklisted(BaseModel):
    id: int  = None
    email: str
    reason: str
    game_id: int

    class Config:
        orm_mode = True