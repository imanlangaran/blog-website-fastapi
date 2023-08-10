from sqlalchemy.orm import Session
from db.models.blog import Blog

def list_blogs(db:Session):
    return db.query(Blog).filter(Blog.is_acvite==True).all()
    