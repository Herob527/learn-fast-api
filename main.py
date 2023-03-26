from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/text", response_model=schemas.Text)
def create_text(text: schemas.TextPost, db: Session = Depends(get_db)):
    return crud.create_text(db, text=text)


@app.get("/text", response_model=list[schemas.Text])
def get_all_texts(db: Session = Depends(get_db)):
    return crud.get_all_texts(db)


@app.get("/text/{text_id}", response_model=schemas.Text)
def get_text(text_id: int, db: Session = Depends(get_db)):
    return crud.get_text(db, text_id=text_id)


@app.delete("/text/{text_id}", response_model=schemas.Text)
def delete_text(text_id: int, db: Session = Depends(get_db)):
    return crud.remove_text(db, text_id=text_id)


@app.patch("/text", response_model=schemas.Text)
def update_text(text: schemas.TextUpdate, db: Session = Depends(get_db)):
    return crud.update_text(db, text=text)
