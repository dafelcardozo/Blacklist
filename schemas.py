from pydantic import BaseModel

class Blacklisted(BaseModel):
    id: int | None = None
    email: str
    reason: str | None = None
    game_id: int

    class Config:
        orm_mode = True