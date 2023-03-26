from pydantic import BaseModel


class TextBase(BaseModel):
    text: str


class Text(TextBase):
    id: int

    class Config:
        orm_mode = True


class TextPost(TextBase):
    pass


class TextGet(TextBase):
    id: int


class TextRemove(BaseModel):
    pass


class TextUpdate(BaseModel):
    new_text: str
    id: int
