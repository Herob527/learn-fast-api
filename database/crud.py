from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import models, schemas


def get_all_texts(db: Session):
    db_texts = db.query(models.Text).all()
    if db_texts is None:
        raise HTTPException(status_code=404, detail="No texts in database")

    return db_texts


def get_text(db: Session, text_id: int):
    db_text = db.query(models.Text).filter(models.Text.id == text_id).one()
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")
    return db_text


def create_text(db: Session, text: schemas.TextPost):
    db_text = models.Text(text=text.text)
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    return db_text


def remove_text(db: Session, text_id: int):
    db_text = db.query(models.Text).filter(models.Text.id == text_id).one()
    if db_text is None:
        raise HTTPException(status_code=404, detail="Text not found")

    db.delete(db_text)
    db.commit()
    return db_text


def update_text(db: Session, text: schemas.TextUpdate):
    db_text = db.query(models.Text).filter(models.Text.id == text.id)
    text_value = db_text.first()
    if text_value is None:
        raise HTTPException(status_code=404, detail="Text with given ID not found")

    db_text.update({"text": text.new_text})
    db.commit()
    return text_value
