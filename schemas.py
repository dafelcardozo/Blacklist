from pydantic import BaseModel

class Blacklisted(BaseModel):
    id: int
    email: str
    reason: str
    game_id: int

    class Config:
        orm_mode = True